import requests
from bs4 import BeautifulSoup as bs

baseUrl = "https://www.bikewale.com/"


def extractBike(brand, model):
    url = baseUrl + brand + "-bikes/" + model + "/"
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    data = {}

    def prodOnRoad():
        prod = soup.find('h1', {'class': 'inline-block margin-right15 page-header'}).getText()
        price = soup.find('span', {'class': 'font22 font-bold'}).getText()

        prod = prod.replace('  ', '')
        price = price.replace('  ', '')

        prod = prod.replace('\n', '')

        data['product'] = prod
        data['price'] = price

        s = []
        v = []

        for i in soup.findAll('table', {'id': 'model-key-highlights'}):
            for j in i.findAll('tbody'):
                for k in j.findAll('td', {'class': 'table-specs-title'}):
                    spec = k.contents[0]
                    spec = spec.replace('  ', '')
                    spec = spec.replace('\n', '')
                    s.append(spec)
                for l in j.findAll('td', {'class': 'text-bold'}):
                    value = l.getText()
                    value = value.replace('  ', '')
                    value = value.replace('\n', '')
                    v.append(value)
        if len(s) == len(v):
            for i in range(len(s)):
                data[s[i]] = v[i]

    def prodNoLaunch():
        prod = soup.find('h1', {'class': 'inline-block margin-right15'}).getText()
        price = soup.find('span', {'id': 'bike-price'}).getText()
        price = price.replace('\\xa0', '')

        prod = prod.replace('  ', '')
        price = price.replace('  ', '')

        prod = prod.replace('\n', '')

        data['product'] = prod
        data['price'] = price

        s = []
        v = []

        for i in soup.findAll('table', {'id': 'model-key-highlights'}):
            for j in i.findAll('tbody'):
                for k in j.findAll('td', {'class': 'table-specs-title'}):
                    spec = k.contents[0]
                    spec = spec.replace('  ', '')
                    spec = spec.replace('\n', '')
                    s.append(spec)
                for l in j.findAll('td', {'class': 'text-bold'}):
                    value = l.getText()
                    value = value.replace('  ', '')
                    value = value.replace('\n', '')
                    v.append(value)

        if len(s) == len(v):
            for i in range(len(s)):
                data[s[i]] = v[i]

    if soup.find('div', {'class': 'content-block'}) is not None:
        data["model"] = "not found"
        return data
    elif soup.find('span', {'class': 'model-ribbon upcoming-ribbon'}) is None:
        prodOnRoad()
    else:
        prodNoLaunch()
    return data