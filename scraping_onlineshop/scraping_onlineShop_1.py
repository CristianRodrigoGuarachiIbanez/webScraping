"""
Created on Fr Nov 9 2020
@author: Cristian Rodrigo Guarachi Ibanez
Scraping Online Shop
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
# headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
#fetch 
url= 'https://auprotec.com/'
r= requests.get(url, headers)
soup= BeautifulSoup(r.content, 'html.parser')

all_links_bruto= soup.find_all('a', class_="navigation--link link--go-forward")
#print(all_links_bruto)
# Extracting URLs from the attribute href in the <a> tags.
just_links= []
for tag in all_links_bruto:
    href= tag.get('href')
    just_links.append(href)
    #print(href)

print(just_links)

#anchor_elements = [element['href'] for element in soup.select('a[href]')]
#print(anchor_elements)

#just_links= all_links_bruto.get('href')
#print(just_links)

#print(all_links_bruto.href)
# for link in soup.findall('a'):
#     List+= link.get('href') + '\n'
#     print(List)

# for link in BeautifulSoup(str(base), "html.parser").findAll("li"):
#     if 'href' in link.attrs:
#         print(link['href'])


#============== parte II ====================

#for x in just_links:
    #r = requests.get(x, headers)
    #soup = beautifulsoup(r.content, 'html.parser')
    #buscar los links directo al producto
    #links_bruto = soup.find_all('a', class_="category--teaser--link")
    #print(links_bruto)
    #for tag in links_bruto:
        #print(tag.get('href'))
x= just_links[0] # GERADE WIRD NUR DURCH DAS ERSTE ELEMENT HERAUSGEZOGEN

#== pfad zu 2 unterteilter Kategorie
artik= ['auspufteile', 'bremsteile']
link_arti = [just_links[0] + '/' + str(i) for i in artik] #GERADE WIRD NUR DURCH DAS ERSTE ELEMENT von erster Ebene HERAUSGEZOGEN

#print(link_arti)
#for x in lb:
#    print(x.get('href'))


#==================== Parte III ================

artik_3= ['auspuffrohre-universal', 'auspuff-rohreboegen-universal','reduzierstuecke-universal', 'flansche-reparatursaetze', 'flexrohre', 'rohrevebinder-schellen', 'montageteile' ]
#link_arti3 = [link_arti[1] + '/' + str(i) for i in artik_3] #GERADE WIRD NUR DURCH DAS ERSTE ELEMENT HERAUSGEZOGEN
link_arti31= [link_arti[0] + '/' + str(i) for i in artik_3]#GERADE WIRD NUR DURCH DAS ERSTE ELEMENT HERAUSGEZOGEN
print( link_arti31)

#=================== Parte IV=====================

artik_4 = ['auspuffrohre-meterware', 'auspuffrohre-100-cm-aufgeweitet', 'auspuffrohre-40-cm-aufgeweitet']
link_arti4 = [link_arti31[0] + '/' + str(i) for i in artik_4] #GERADE WIRD NUR DURCH DAS ERSTE ELEMENT HERAUSGEZOGEN
print(link_arti4)

#======================= part X
#links

#url_link= link_arti4[1]
url_link = 'https://auprotec.com/auto-teile/auspuffteile/auspuffrohre-universal/auspuffrohre-meterware'
r2= requests.get(url_link, headers)
soupa= BeautifulSoup(r2.content, 'html.parser')

#url_bruto= soupa.find_all('a', class_="product--image")
url_bruto2= soupa.select(' a[href*="auspuffrohr"].product--title')
url_variantes=  [x.get('href') for x in url_bruto2]
print(url_variantes)

#=========================== variantes XI


r3= requests.get(url_variantes[0], headers)
sopa= BeautifulSoup(r3.content, 'html.parser')

#try

titel= sopa.find_all('h1', class_= 'product--title')
titulo=[x.text for x in titel]
print(titulo)

#try

details= sopa.select('ul > li.detail--bulletpoint.base-info--entry.entry-attribute')
detalles= [x.text for x in details]
print(detalles)

#try

descrip= sopa.select('div > p + p')
print(descrip)

