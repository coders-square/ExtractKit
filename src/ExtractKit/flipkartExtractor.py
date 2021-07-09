from bs4 import BeautifulSoup as bs
import requests
Headers = { "User-Agent": 'Mozila/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36' }    

def extractFlipkart(product):
    data = {}
    URL = 'https://www.flipkart.com/search?q='+product
    page = requests.get(URL, headers=Headers)
    soup = bs(page.content, 'html.parser')
    url = []
    for link in soup.findAll('a',{'target':'_blank'}):
        url.append(link.get('href'))
    prod=url[1]
    prod="https://www.flipkart.com"+prod
    pg = requests.get(prod,headers=Headers)
    sp = bs(pg.content,'html.parser')
    price = sp.find('div',{'class': '_30jeq3 _16Jk6d'}).get_text()
    product = sp.find('span',{'class':'B_NuCI'}).get_text()
    data['product'] = product
    data['price'] = price
    data['url'] = prod
    return data

def extractFlipkartUrl(url):
    data = {}
    page = requests.get(url, headers=Headers)
    soup = bs(page.content, 'html.parser')
    price = soup.find('div',{'class': '_30jeq3 _16Jk6d'}).get_text()
    prod = soup.find('span',{'class':'B_NuCI'}).get_text()
    data['product'] = prod
    data['price'] = price
    return data