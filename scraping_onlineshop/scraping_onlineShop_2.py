"""
Created on Fr Nov 9 2020
@author: Cristian Rodrigo Guarachi Ibanez
Scraping Online Shop 2
"""
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from collections import defaultdict
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

print(just_links)

dict= {key: value for (key, value) in enumerate(just_links)}
print(dict)
#============== parte II ====================
for key, val in dict.items():
    #x= just_links[0] # GERADE WIRD NUR DURCH DAS ERSTE ELEMENT HERAUSGEZOGEN
    #== pfad zu 2 unterteilter Kategorie

    # dic= defaultdict(str)
    # dic[link]=just_links[link]

    if key == 0:
        artik0= ['auspuffteile', 'bremsteile']
        link_arti0 = {key: val + '/' + str(value).strip() for (key, value) in enumerate(artik0)} #GERADE WIRD NUR DURCH DAS ERSTE ELEMENT von erster Ebene HERAUSGEZOGEN
        #print(link_arti0)
        for a, b in link_arti0.items():
            auspuf=['auspuffrohre-universal', 'auspuff-rohrboegen-universal', 'reduzierstuecke-universal', 'flansche-reparatursaetze', 'flexrohre', 'rohrverbinder-schellen', 'montageteile' ]
            brems= ['bremsleitung-meterware', ' bremsleitungen-fertig-geboerdelt', 'bremsleitungen-im-set', 'bremsleitungsverschraubungen', 'entluefterschrauben', 'werkzeuge-hilfsmittel']
            if a ==0:
                auspuff= {x: b + '/' + str(z).strip() for (x, z) in enumerate(auspuf)}
            elif a ==1:
                bremsteile = {x: b + '/' + str(z).strip() for (x, z) in enumerate(brems)}
            for c, d in auspuff.items():
                if c ==0:

                    auspuff_univ=[ 'auspuffrohre-meterware', 'auspuffrohre-40-cm-aufgeweitet', 'auspuffrohre-100-cm-aufgeweitet']
                    auspuff_universal= {x:d + '/' + str(z).strip() for (x,z) in enumerate(auspuff_univ)}

                    for e, f in auspuff_universal.items():
                        if e==0:
                            meterware= f
                            try:
                                s = requests.get(meterware, headers)
                                soupa = BeautifulSoup(s.content, 'html.parser')
                                auspuff_meterware = soupa.select(' a[href*="https://"  ].product--title')
                                url_variantes1 = [x.get('href') for x in auspuff_meterware]
                                #print('das ist die Kategorie auspuff_meterware {links}'.format(links=url_variantes1))
                            except ValueError as e:
                                print(e)
                            meterware = {x: str(z).strip() for (x, z) in enumerate(url_variantes1)}
                        if e== 1:
                            c0_cm= f

                            try:
                                s2 = requests.get(c0_cm, headers)
                                soupa = BeautifulSoup(s2.content, 'html.parser')
                                auspuff_40_cm = soupa.select(' a[href*="https://"  ].product--title')
                                url_variantes11 = [x.get('href') for x in auspuff_40_cm]
                                #print('das ist die Kategorie auspuffrohre_40_cm {links}'.format(links=url_variantes11))
                            except ValueError as e:
                                print(e)
                            c0_cm = {x: str(z).strip() for (x, z) in enumerate(url_variantes11)}
                        if e==2:
                            c00_cm= f
                            try:
                                s3 = requests.get(c00_cm, headers)
                                soupa = BeautifulSoup(s3.content, 'html.parser')
                                auspuff_100_cm = soupa.select(' a[href*="https://"  ].product--title')
                                url_variantes111 = [x.get('href') for x in auspuff_100_cm]
                                #print('das ist die Kategorie auspuffrohre_100_cm {links}'.format(links=url_variantes111))
                            except ValueError as e:
                                print(e)
                            c00_cm = {x: str(z).strip() for (x, z) in enumerate(url_variantes111)}
                if c ==1:
                    a_ro= d
                    try:

                        r2 = requests.get(a_ro, headers)
                        soupa = BeautifulSoup(r2.content, 'html.parser')
                        auspuff_ro = soupa.select(' a[href*="https://"  ].product--title')
                        url_variantes = [x.get('href') for x in auspuff_ro ]
                        #print('das ist die Kategorie auspuffrohre_universal {links}'.format(links=url_variantes))
                    except ValueError as e:
                        print(e)
                    auspuff_rohre= {x: str(z).strip() for (x,z) in enumerate(url_variantes)}
                if c==2:
                    r_uni= d
                    #print(r_uni)
                    try:

                        r3 = requests.get(r_uni, headers)
                        soupa = BeautifulSoup(r3.content, 'html.parser')
                        reduzier_uni = soupa.select(' a[href*="https://"  ].product--title')
                        url_variantes2 = [x.get('href') for x in  reduzier_uni]
                        #print('das ist die Kategorie reduzierrohre_universal {links}'.format(links=url_variantes2))
                    except ValueError as e:
                        print(e)

                    reduzier_universal = {x: str(z).strip() for (x, z) in enumerate(url_variantes2)}
            # print(auspuff_rohre)
            # print(reduzier_universal)
                if c==3:
                    flansche= d
                    try:
                        r4 = requests.get(flansche, headers)
                        soupa = BeautifulSoup(r4.content, 'html.parser')
                        flansch= soupa.select(' a[href*="https://"  ].product--title')
                        url_variantes3 = [x.get('href') for x in flansch]
                        #print('das ist die Kategorie flansche {links}'.format(links=url_variantes3))
                    except ValueError as e:
                        print(e)
                    flansche = {x: str(z).strip() for (x, z) in enumerate(url_variantes3)}
                if c==4:
                    flexrohre= d
                    try:
                        r5 = requests.get(flexrohre, headers)
                        soupa = BeautifulSoup(r5.content, 'html.parser')
                        flexrohr = soupa.select(' a[href*="https://"  ].product--title')
                        url_variantes4 = [x.get('href') for x in flexrohr]
                        #print('das ist die Kategorie flexrohre {links}'.format(links=url_variantes4))
                    except ValueError as e:
                        print(e)
                    flexrohre = {x: str(z).strip() for (x, z) in enumerate(url_variantes4)}
                if c==5:
                    rohverbinder= d
                    try:

                        r6 = requests.get(rohverbinder, headers)
                        soupa = BeautifulSoup(r6.content, 'html.parser')
                        rohrverbinder = soupa.select(' a[href*="https://"].product--title')
                        url_variantes5 = [x.get('href') for x in rohrverbinder]
                        #print('das ist die Kategorie rohrverbinder {links}'.format(links=url_variantes5))
                    except ValueError as e:
                        print(e)
                    rohrverbinder= {x: str(z).strip() for (x, z) in enumerate(url_variantes5)}
                if c==6:
                    montaget= d
                    #print(montaget)
                    try:
                        r7 = requests.get(montaget, headers)
                        soupa = BeautifulSoup(r7.content, 'html.parser')
                        montageteile = soupa.select(' a[href*="https://"  ].product--title')
                        url_variantes6 = [x.get('href') for x in montageteile]
                        #print('das ist die Kategorie montageteile{links}'.format(links=url_variantes6))
                    except ValueError as e:
                        print(e)
                    montaget = {x: str(z).strip() for (x, z) in enumerate(url_variantes6)}
                #print(auspuff)

print(meterware)
print(c0_cm)
print(c00_cm)
print(auspuff_rohre)
print(reduzier_universal)
print(flansche)
print(flexrohre)
print(rohrverbinder)
print(montaget)




#############
def p_decorate(func):
    def func_wrapper(name, name2):
        return "<h2>{0}</h2>".format(func(name)),  '<li>{0}</li>'.format(func(name2))

    return func_wrapper


#my_get_text = p_decorate(get_text)
def wrapper(name):
    return "<h2>{0}</h2>".format(name)

def wrapper2(name):
    return '<li>{0}</li>'.format(name)



for i, j in meterware.items():
    r_t = requests.get(j, headers)
    soup = BeautifulSoup(r_t.content, 'html.parser')
    ####### Titulo ########
    try:
        titel = soup.find_all('h1', class_='product--title')
        titulo = [x.text.replace('\n', '') for x in titel]
        titulo= '\n'.join(titulo)
        titulo= wrapper(titulo)

    except ValueError as e:
        print(e)
        try:
            titel = soup.select('h1.product--title')
            titulo = [x.text.replace('\n', '') for x in titel]
            titulo = '\n'.join(titulo)
        except ValueError as e:
            print(e)

    ####### Text_details############
    try:

        details= soup.select('div > article.as--article-description')
        detalles= [x.text.split('\n') for x in details]

        flatten = [item for sublist in detalles for item in sublist]
        flatten = list(filter(None, flatten))
        str_list = [wrapper2(item) for item in flatten]
        str_list = '\n'.join(str_list)
        #str_list = wrapper2(str_list)

    except ValueError as e:
        print(e)
        try:

            details= soup.select('ul > li.detail--bulletpoint.base-info--entry.entry-attribute')
            detalles= [x.text.split('\n') for x in details]

            flatten = [item for sublist in detalles for item in sublist]
            str_list = list(filter(None, flatten))
            str_list = '\n'.join(str_list)

        except ValueError as e:
            print(e)

   #=====von Listen in Liste zu einer senkrechten String

    file_nombre= 'Produkt'+'_'+ str(i)+'.txt'
    file= open(file_nombre, 'w')
    file.write(str(titulo) + '\n')
    file.write(str(str_list) + '\n')
    file.close()
# print(titulos)
# print(detalles)
# print(str_list)
