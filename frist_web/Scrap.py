import requests
from bs4 import BeautifulSoup
import pymongo

res = requests.get('https://www.ukri.org/opportunity/')

info_html = BeautifulSoup(res.text, "html.parser")

table = info_html.select('.enter-header')

Fund_title = info_html.select("h3.entry-title.ukri-entry-title")
Summary_from_web = info_html.select("div.entry-content")
Award_Range = info_html.select("dd.govuk-table__cell.opportunity-cells")
opportunity_status = info_html.select('.open.opportunity-status__flag')


def get_text(li):
    final_text = []
    for idx, item in enumerate(li):
        text = item.getText().strip()
        final_text.append(text)
    return final_text


award_range = []
for i,item in enumerate(get_text(Award_Range)):
    if '£' in item:
        award_range.append(item)



##Mongo_db

client = pymongo.MongoClient(
   'mongodb+srv://Scrap:Scrap123@cluster0.vofcb.mongodb.net/assesments?retryWrites=true&w=majority')
db = client.assesments
collection = db.grant

def post():
   dic = {}
   for i in range(1,3):

       dic = {
           'title': get_text(Fund_title)[i],
           'status': get_text(opportunity_status)[i],
           'Summary': get_text(Summary_from_web)[i],
           'award': award_range[i]
        }
       dic.update()
   return dic



collection.insert_one(post())




