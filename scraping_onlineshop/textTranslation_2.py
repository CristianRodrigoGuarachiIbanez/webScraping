"""
Created on Fr Nov 9 2020
@author: Cristian Rodrigo Guarachi Ibanez
Text translation 2
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import copy
import json
import time
import re
from html.parser import HTMLParser

try:
	from collections.abc import Iterable
except ImportError:
	from collections import Iterable

from googletrans import Translator
from textblob_de import TextBlobDE as TextBlob
#=============  Tags Entferner ========================
class MyHTMLParser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.tags = []

	def handle_starttag(self, tag, attrs):
		self.tags.append(self.get_starttag_text())

	def handle_endtag(self, tag):
		self.tags.append(f"</{tag}>")


# parser = MyHTMLParser();
# parser.feed("""<p > Argh, whitespace and p is not closed </a>""")
# parser.tags  # ['<p >', '</a>']
#========================= remover tags ==============
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def wrapper(name):
    return "<h2>{0}</h2>".format(name)

def wrapper2(name):
    return '<li>{0}</li>'.format(name)

def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x + '\n'
         else:
             yield item

#=========================== traduction =====================================

def text_translator(path):
	with open(path, "r+") as f:
		#neuer_Text = f.read()

		#Einlesen des Text File zeilenweise
		linie = f.readline()

		#einen Counter erstellen, um später das Einlesen von Textzeilen vollstellbar zu halten
		cnt = 1
		# hier wird der Text endgultig hinterlegt
		contenidos = []

		translator = Translator()

		while linie:
			print("Linie {}: {}".format(cnt, linie.strip()))
			#nach den Tags zeilenweise im Text absuchen
			parser = MyHTMLParser()
			parser.feed(linie)
			print(parser.tags)
			# translator initiieren
			# REINITIALIZE THE API
			translator = Translator()
			#linie= copy.deepcopy(linie)

			regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

			if not (parser.tags[0]) or (parser.tags[0]== '#') or (parser.tags[0]=='='):
				pass
			elif (regex.search(linie) == '*'):
				linieh2 = remove_html_tags(linie)
				try:
					h2 = translator.translate(str(linieh2), dest="es")
					time.sleep(2 * 2)
				except Exception as e:
					print(str(e))

					try:
						h2 = TextBlob(str(linieh2))
						h2 = h2.translate(from_lang='de', to='es')
						time.sleep(2 * 2)

					except Exception as e:
						print(e)
						h2 = pydeepl.translate(str(linieh2), 'ES', from_lang='DE')
						time.sleep(2 * 2)


			elif parser.tags[0] == '<h2>':
				linieh2 = remove_html_tags(linie)
				try:
					h2 = translator.translate(str(linieh2), dest="es")
					time.sleep(2 * 2)
				except Exception as e:
					print(str(e))

					try:
						h2 = TextBlob(str(linieh2))
						h2 = h2.translate(from_lang='de', to='es')
						time.sleep(2 * 2)

					except Exception as e:
						print(e)
						h2 = pydeepl.translate(str(linieh2), 'ES', from_lang='DE')
						time.sleep(2 * 2)

				newlinie = h2.text
				contenidos.append(wrapper(newlinie))

			elif parser.tags[0] == '<li>':
				linieli = remove_html_tags(linie)

				try:
					li = translator.translate(str(linieli), dest="es")
					time.sleep(2 * 2)
				except Exception as e:
					print(str(e))

					try:
						li = deepl.translate(str(linieli), target="ES")
						time.sleep(2 * 2)
					except Exception as e:
						print(e)
						li = pydeepl.translate(str(linieli), 'ES', from_lang='DE')
						time.sleep(2 * 2)
				newlinie = li.text
				contenidos.append(wrapper2(newlinie))
			else:
				pass
			linie = f.readline()
			cnt += 1

	f = open(path, "r")
	contents = f.readlines()
	#contents=[x.strip() for x in contents]
	f.close()
	#contenido= '\n'.join(str(x) for x in contenido)


	contents.insert(0, contenidos)
	contents= list(flatten(contents))

	print(contents)
	f = open(path, "w")
	for index in range(len(contents)+1):
		#contents= '\n'.join(content)
		#contents = "\n".join(str(x) for x in contents)
		#f.write(contents)
		if (len(contents)//2 - 1)== int(index):
			#f.write(contents[index] + ' ')
			f.writelines('============================ Textquelle=================================== ' + ',,\n')
		else:
			f.writelines(contents[index])
	f.close()


if __name__ == '__main__':
	path= r'C:\Users\Cristian\Desktop\scraping\output'
	directories = [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files]
	print(directories)

	for directory in directories:

		text_translator(directory)
		time.sleep(1*2)

