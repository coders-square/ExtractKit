<h1 align="center">ExtractKit</h1>

###what is this??

    This is a Easy Scrapper for scrapping essential data from web

##What can it Scrape?

* **[Price and Key Specs of car](#scrap-car-data)** 
* **[Price and Key Specs of bike](#scrap-bike-data)**, 
* **[Price and specs of mobiles](#scrap-mobile-specifications)** 
* **[Scrap Flipkart](#scrap-flipkart)** 
* **[Scarap Price and details of PC Building components](#scrap-pc-components)**
* **[Scrap Live News and other Archived News](#scrap-news-data)**

##How to use this??

So simple!! Just go and type

```
pip install ExtractKit
```
Bam!! You just installed a great scraping tool

##How to use in python??

    import ExtractKit as ekit #or whatever

##Detailed documentation

### Scrap Car Data
This scrapes car specification from [Carwale Website](https://www.carwale.com/)

To Scrap car Specification,

    from ExtractKit import carExtractor as car

    data = bike.extractBike('hyundai',"creta")
    print(data)

####extractCar(brand, model),

**Parameters,**
**brand** - string data type, enter the brand name of the car you want to search
**model** - string data type, enter the model name of the car you want to search

Result Data Looks like this:
```
    {
    'product': 'Hyundai Creta', 
    'price': '₹ 10.00 Lakh'
    }
```

### Scrap Bike Data
This scrapes bike specification from [Bikewale Website](https://www.bikewale.com/)

To Scrap Bike Specification,

    from ExtractKit import bikeExtractor as bike

    data = bike.extractBike('yamaha',"R15")
    print(data)

####extractBike(brand, model)

**Parameters,**
**brand** - string data type, enter the brand name of the bike you want to search
**model** - string data type, enter the model name of the bike you want to search

Result Data Looks like this:
```
    {
    "product": "Yamaha YZF R15 V3", 
    "price": "1,55,334", 
    "Engine Capacity": "155 cc", 
    "Mileage": "43 kmpl", 
    "Transmission": "6 Speed Manual ", 
    "Kerb Weight": "142 kg", 
    "Fuel Tank Capacity": "11 litres", 
    "Seat Height": "815 mm"
    }
```

### Scrap Mobile Specifications
This scraps data from [91 Mobiles Website](https://www.91mobiles.com/)

    from ExtractKit import gadgetsExtractor as gadgets
    x = gadgets.extractMobile('samsung','galaxy a52')
    print(x)

In extractMobile(brand, model),
* Brand and model must be passed as string

Result data looks like this:
```
{
    "name": "Samsung Galaxy A52",
    "price": " 23,499",
    "variants": [
        "128GB Storage, 8GB RAM\n"
    ],
    "specs": [
        [
            "RAM","6GB"
        ],
        [   
            "Processor","QualcommSnapdragon720G"
        ],
        [   
            "Rear Camera","64MP+12MP+5MP+5MP"
        ],
        [
            "Front Camera","32MP"
        ],
        [
            "Battery","4500mAh"
        ],
        [...]
        [...]
    ]
}
```

### Scrap Flipkart
This Scraps data from [flipkart.com](https://flipkart.com)

To Scrap Flipkart products,

    from ExtractKit import flipkartExtractor as flipkart
    x = flipkart.extractFlipkart('XBOX Series S')
    print(x)

In extractFlipkart(product),
* It must be a valid product.
* Product must be in string format.

Result data looks like this:

```
{
    "product": "MICROSOFT Xbox Series S 512 GB\u00a0\u00a0(White)",
    "price": "\u20b934,990",
    "url": "https://www.flipkart.com/microsoft-xbox-series-s-512-gb/p/itm13c51f9047da8?pid=GMCFVPFCNHHZQBNA&lid=LSTGMCFVPFCNHHZQBNAH2FMXL&marketplace=FLIPKART&q=XBOX+Series+S&store=4rr&srno=s_1_1&otracker=search&fm=organic&iid=a98ea799-22c1-440d-b211-9835eb1790eb.GMCFVPFCNHHZQBNA.SEARCH&ppt=None&ppn=None&ssid=l55b2xbdfk0000001625828211339&qH=fd75188725591a70"
}
```

You can also use extractFlipkartUrl(url) to scrap data from the given flipkart link

    from ExtractKit import flipkartExtractor as flipkart
    x = flipkart.extractFlipkartUrl('https://www.flipkart.com/cyberpunk-2077-limited-edition/p/itm6e7fc6515a3b3?pid=GAMG2Z8UGZHTYHAF&lid=LSTGAMG2Z8UGZHTYHAFHTIMQD&marketplace=FLIPKART&q=cyberpunk+2077&store=4rr%2Ffa6%2F27p%2Fmtr&spotlightTagId=TrendingId_4rr%2Ffa6%2F27p%2Fmtr&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_na&fm=SEARCH&iid=0fa0a337-bb8d-4126-9fe6-9421bcbdb3ee.GAMG2Z8UGZHTYHAF.SEARCH&ppt=sp&ppn=sp&ssid=rg6sh1i72o0000001625828417574&qH=65fc51bd3f81e7c2')
    print(x)

The result for this function is:
```
{
    "product": "Cyberpunk 2077 (Limited Edition) (for PS4)",
    "price": "₹2,899"
}
```

### Scrap PC Components

This Scraps data from [PC Studio](https://www.pcstudio.in/)

To Scrap PC Components,

    from ExtractKit import pcBuildExtractor as pcBuild
    x = pcBuild.extractProcessors()
    print(x)

Result data looks like this:
```
{
    "0": {
        "title": "AMD RYZEN 3 3200G OPEN BOX OEM PROCESSOR WITH RX VEGA 8 GRAPHICS (UP TO 4.0GHZ 6 MB CACHE) ",
        "price": "\u20b911,300.00",
        "details": "https://www.pcstudio.in/product/amd-ryzen-3-3200g-open-box-oem-processor-with-rx-vega-8-graphics-up-to-4-0ghz-6-mb-cache/",
        "img": "https://www.pcstudio.in/wp-content/uploads/2021/07/AMD-RYZEN-3-3200G-OPEN-BOX-OEM-PROCESSOR-WITH-RX-VEGA-8-GRAPHICS-1.jpg"
    },
    "1":{...},
    "2":{...},
}
```

other functions available are:
    
    print(pcBuild.extractProcessors())    #Extract Processors Data
    print(extractMotherboards())          #Extract Motherboard Data 
    print(extractRams())                  #Extract RAM Data
    print(extractStorage1())              #Extract Storages Data
    print(extractStorage2())              #Extract Storages Data too
    print(extractCabinets())              #Extract Cabinet Data
    print(extractCoolers())               #Extract Coolers Data
    print(extractGPUs())                  #Extract GPU Data
    print(extractPowerSupplys())          #Extract PowerSupplyUnit Data
    print(extractDisplays())              #Extract Display Data


### Scrap News Data
This scraps live and archive news data from [One India News](https://oneindia.com)

To Scrap news,

    from ExtractKit import newsExtractor as news

    data = news.extractlNewsArchives('english',2021,7,1)
    print(data)

**Parameters,**
**language** - string data type, enter the language in which you want to search
**Avaliable Languages are**
* tamil
* telugu
* malayalam
* bengali
* gujarati
* hindi
* kannada

**year** - integer data type, enter the year in which you want to search
**month** - integer data type, enter the month in which you want to search
**date** - integer data type, enter the date in which you want to search

Result Data Looks like this:
```
    {
    "language": "english",
    "1": {
        "category": "bengaluru",
        "news": "No interviews to fill up vacancies to post of assistant professors, principles in Karnataka\u2019s higher education"
    },
    "2":{...},
    "3":{...},
    ....
```

## Credits
<p align="left">  
<b>Karthik Raja K</b> &emsp;
<a href="https://instagram.com/mr.anonymous_official" target="blank"><img width=25 align="center" src="https://img.icons8.com/doodle/50/000000/instagram-new.png"/></a>  
<a href="https://github.com/mr-anonymous-official/" target="blank"><img width=25 align="center" src="https://img.icons8.com/doodle/50/000000/github.png"/></a>  
<a href="https://www.linkedin.com/in/karthikraja01/" target="blank"><img width=25 align="center" src="https://img.icons8.com/doodle/48/000000/linkedin--v2.png"/></a>  
</p>

<p align="left">  
<b>Vignesh R</b> &emsp;&emsp;&emsp;
<a href="https://instagram.com/vignesh_r_" target="blank"><img width=25 align="center" src="https://img.icons8.com/doodle/50/000000/instagram-new.png"/></a>  
<a href="https://github.com/codervignesh/" target="blank"><img width=25 align="center" src="https://img.icons8.com/doodle/50/000000/github.png"/></a>  
<a href="https://www.linkedin.com/in/vignesh-r-/" target="blank"><img width=25 align="center" src="https://img.icons8.com/doodle/48/000000/linkedin--v2.png"/></a>  
</p>

<br/>

### Source Code Available in [Github](https://github.com/coders-square/ExtractKit)