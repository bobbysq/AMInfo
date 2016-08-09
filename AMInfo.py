from bs4 import BeautifulSoup
import re
import urllib

product = raw_input("Andymark part number? ").zfill(4)

def andymark_item(partnumber):
    '''
    Looks up an Andymark part. Takes in a part ID (a string), returns an array listing URL, part name, and price.
    '''
    url = 'http://www.andymark.com/product-p/am-'+str(product)+'.htm'
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    price = soup.find_all("span", itemprop="price")
    if soup.title.get_text()=="AndyMark Robot Parts Kits Mecanum Omni Wheels":
        return(None) #404 checking
    else:
        name = re.sub(r'\([^)]*\)', '', soup.title.get_text())
        #print(price[0].text)
        money = float(price[0].text.encode('utf8','ignore').replace('$',''))
        return([url, name, money])
        #print(re.sub(r'\([^)]*\)', '', soup.title.get_text())) #kill the parenthesis
        #print(float(price[0].get_text()))

part = andymark_item(product)

if part:
    print(part[0])
    print(part[1])
    print("{0:.2f}".format(part[2]))
