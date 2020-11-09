"""
Created on Fr Nov 9 2020
@author: Cristian Rodrigo Guarachi Ibanez
Text translation 
"""
#=============  Tags Entferner ========================
from html.parser import HTMLParser


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

#=========================== traduction =====================================
from googletrans import Translator

path= r'C:\Users\Cristian\Desktop\scraping\output\kategorie1\Artikel_3.txt'
with open(path, "r+") as f:
	#neuer_Text = f.read()
	linie = f.readline()
	cnt = 1
	contenidos = []
	while linie:
		print("Linie {}: {}".format(cnt, linie.strip()))
		parser = MyHTMLParser()
		parser.feed(linie)
		print(parser.tags)

		translator = Translator()

		if len(parser.tags) == 0:
			pass
		elif parser.tags[0] == '<h2>':
			linieh2= remove_html_tags(linie)
			h2= translator.translate(linieh2, dest="es")
			contenidos.append(wrapper(h2.text))

		elif parser.tags[0] =='<li>':
			linieli=remove_html_tags(linie)
			li = translator.translate(linieli, dest="es")
			contenidos.append(wrapper2(li.text))
		else:
			pass

		linie = f.readline()
		cnt += 1

f = open(path, "r")
contents = f.readlines()
f.close()
#contenido= '\n'.join(str(x) for x in contenido)


contents.insert(0, contenidos)

for contenido in contents:
	f = open(path, "w")
	contents= '\n'.join(contenido)
	#contents = "\n".join(str(x) for x in contents)
	#f.write(contents)
	f.writelines(contents)
	f.close()
