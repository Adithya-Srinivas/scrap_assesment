import requests
from bs4 import BeautifulSoup
import pymongo

case_studies = requests.get('https://www.astutewales.com/en/case-studies')
detail_page = requests.get('https://www.astutewales.com/en/case-studies.htm?id=101')

html_case_studies = BeautifulSoup(case_studies.text, "html.parser")
html_detail_page = BeautifulSoup(detail_page.text, "html.parser")

# Case_Studies

title = html_case_studies.select('h4.casestudy__title')

links_to_detail_page = []

for a in html_case_studies.find_all('a', href=True):
    if 'case-studies.' in a['href']:
        links_to_detail_page.append(a['href'])


# Detail_Page

Case_study_title = html_detail_page.select('h3.casestudy--single__title.t--lblue')
Challenge = html_detail_page.select('div.pod__text')
Solution = html_detail_page.select('div#pod-3086.pod.pod--col--2.pod--text')
Business = html_detail_page.select('p.casestudy--business')
Expertise = html_detail_page.select('p.casestudy--single__right')


def get_text(li):

    final_text = []
    for idx, item in enumerate(li):
        text = item.getText().strip().replace('\n', '')
        final_text.append(text)
    return final_text


# get_text(title)
# links_to_detail_page[]
# get_text(Case_study_title)
# get_text(Challenge)
# get_text(Solution)
# get_text(Business)
# get_text(Expertise)

##Mongo_db

client = pymongo.MongoClient(
   'mongodb+srv://Scrap:Scrap123@cluster0.vofcb.mongodb.net/assesments?retryWrites=true&w=majority')
db = client.assesments
collection = db.case_studies

def post():
   dic = {}
   for i in range(1):

       dic = {
           'title': get_text(Case_study_title)[i],
           'link': links_to_detail_page[i],
           'Challenge': get_text(Challenge)[i],
           'Solution': get_text(Solution)[i],
           'Business': get_text(Business)[i],
           'Expertise': get_text(Expertise)[i]
        }
       dic.update()
   return dic

collection.insert_one(post())






