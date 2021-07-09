from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
from string import Template
engUrl = Template("https://oneindia.com/$yyyy/$mm/$dd/")
baseUrl = Template("https://$lang.oneindia.com/$yyyy/$mm/$dd/")

def extractNewsArchives(language, year, month, day):
    if int(month)>0 and int(month)<10:
        month = '0' + str(int(month))
    month = str(month)
    if int(day)>0 and int(day)<10:
        day = '0' + str(int(day))
    day = str(day)
    year = str(year)
    Headers = { "User-Agent": 'Mozila/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36' }
    if language is not 'english':
        url = baseUrl.safe_substitute(lang = language,yyyy = year,mm = month,dd = day)
    else:
        url = engUrl.safe_substitute(yyyy = year,mm = month,dd = day)
    page = requests.get(url,headers = Headers)
    soup = bs(page.content,'html.parser')
    data = {}
    data['language'] = language
    count = 1
    for i in soup.findAll('section'):
        for j in i.findAll('div',{'class':'content clearfix'}): # Collecting City Name
            for news in j.findAll('div',{'class':'dayIndexContent'}): # Collecting News and City
                for t in news.findAll('ul',{'class':'dayindexTitles'}):
                    for q in t.findAll('li'):
                        DATA = {}
                        CITY = q.a['href'].split('/')[-2]
                        NEWS = q.a.getText()
                        DATA['category'] = CITY
                        DATA['news'] = NEWS
                        data[count] = DATA
                        count = count + 1
    return data