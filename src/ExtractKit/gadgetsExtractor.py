import requests
from bs4 import BeautifulSoup as bs
import re
Headers = { "User-Agent": 'Mozila/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36' }

def extractMobile(brand, model):
    data = {}
    model = model.replace(' ','-')
    url = 'https://www.91mobiles.com/'+brand+'-'+model+'-price-in-india'
    page = requests.get(url, headers = Headers)
    soup = bs(page.content,'html.parser')
    try:
        price = soup.find('span',{'itemprop':'price'}).getText()
        name = soup.find('span',{'itemprop':'name'}).getText()
        data['name'] = name
        data['price'] = price
    except AttributeError:
        data['none'] = None
    variants = []
    urls = []
    for a in soup.findAll("li", {"data-href-url" : True}):
        urls.append(a['data-href-url'])
    def variant(soup):
        for varis in soup.find_all('ul',{'class','vrt_ul'}):
            x = varis.text
            x = re.sub('\n','',x,1)
            variants.append(x)
    variant(soup)
    data['variants'] = variants
    try:
        pros = variants[0].split('\n')
        print(pros)
    except:
        data['variants'] = None
    specifications = []
    property = []
    values = []
    def properties(soup):
        for props in soup.findAll('td',{'class':'spec_ttle'}):
            property.append(props.get_text())
    def valus(soup):
        for props in soup.findAll('td',{'class':'spec_des'}):
            some = props.get_text()
            vals = some.replace(' ','')
            final = vals.replace('\n','')
            values.append(final)
    properties(soup)
    valus(soup)
    for i in range(len(property)-1):
        specifications.append([property[i],values[i]])
    data['specs'] = specifications
    return data