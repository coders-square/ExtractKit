import requests
from bs4 import BeautifulSoup as bs
baseUrl = 'https://www.carwale.com/'

def extractCar(brand, model):
    data = {}
    model = model.replace(' ','-')
    url = baseUrl + brand +'-cars/'+model
    Headers = { "User-Agent": 'Mozila/5.0 (Windows NT 10.0; Win64; X64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36' }
    page = requests.get(url,headers = Headers)
    soup = bs(page.content,'html.parser')
    car_price = soup.find('span',{'class':'o-Hyyko o-bPYcRG o-eqqVmt'})
    carPrice = car_price.get_text()
    car_name = soup.find('h1',{'class':'o-dOKno o-bNCMFw o-eqqVmt o-tvvmc'})
    car_name.div.clear()
    carName = car_name.get_text()
    data['product'] = carName
    data['price'] = carPrice
    return data