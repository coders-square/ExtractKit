import requests
from bs4 import BeautifulSoup as bs
Headers = { "User-Agent": 'Mozila/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36' }
baseUrl = 'https://www.pcstudio.in/pc-build/'

def scrape(soup):
    title = []
    price = []
    details = []
    img = []
    for x in soup.findAll('div',{'class':'woopb-product-left'}):
        for y in x.findAll('figure',{'class':'woocommerce-product-gallery__wrapper'}):
            img.append(y.div.a['href'])
    for i in soup.findAll('div',{'class':'woopb-product-right'}):
        for j in i.findAll('div',{'class':'woopb-product-title'}):
            temp = j.get_text().replace('\n','')
            title.append(temp)
            details.append(j.a['href'])
        for k in i.findAll('div',{'class','woopb-product-price'}):
            price.append(k.get_text())
    data = {}
    for i in range(len(title)):
        spec = {}
        spec['title'] = title[i]
        spec['price'] = price[i]
        spec['details'] = details[i]
        spec['img'] = img[i]
        data[i] = spec
    return data

def extractProcessors():
    data = {}
    url = baseUrl + "?step=1"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractMotherboards():
    data = {}
    url = baseUrl + "?step=2"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractRams():
    data = {}
    url = baseUrl + "?step=3"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractStorage1():
    data = {}
    url = baseUrl + "?step=4"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractStorage2():
    data = {}
    url = baseUrl + "?step=5"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractCabinets():
    data = {}
    url = baseUrl + "?step=6"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractCoolers():
    data = {}
    url = baseUrl + "?step=7"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractGPUs():
    data = {}
    url = baseUrl + "?step=8"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractPowerSupplys():
    data = {}
    url = baseUrl + "?step=9"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data

def extractDisplays():
    data = {}
    url = baseUrl + "?step=10"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = scrape(soup)
    return data
