"""
	Librairie permettant le formatage html
"""
from django.middleware import csrf
from django.shortcuts import reverse
import os
class libHtml:
	"""
		Classe permettant de générer facilement du code HTML
	"""

	def titre(self,titre,level=1):
		"""
			Fonction retournant un élément titre
			par défaut elle renvoi un titre de niveau 1 (h1)
		"""
		if level == 2:
			s = '<h2>' + titre + '</h2>'
		elif level == 3:
			s = '<h3>' + titre + '</h3>'
		elif level == 4:
			s = '<h4>' + titre + '</h4>'
		elif level == 5:
			s = '<h5>' + titre + '</h5>'
		elif level == 6:
			s = '<h6>' + titre + '</h6>'
		else:
			s = '<h1>' + titre + '</h1>'
		return s

	def div(self, content, classe=None, idtxt = None):
		s = '<div '
		if idtxt is not None:
			s += 'id="' + idtxt +'"'
		if classe is not None:
			s += 'class="' + classe + '"'
		s +='>' + content + '</div>'
		return s

	def container(self, content, cont_type='div',classe=None, idtxt = None):
		s = '<' + cont_type + ' '
		if idtxt is not None:
			s += 'id="' + idtxt +'"'
		if classe is not None:
			s += 'class="' + classe + '"'
		s +='>' + content + '</' + cont_type + '>'
		return s

	def section(self,title,content,classe = None):
		s = '<section '
		if classe is not None:
			s += 'class="' + classe +'"'
		s += '>'
		s += self.titre(title)
		s+= self.container(content,'div')
		return s

	def fieldset(self,title,content):
		s = "<fieldset>"
		s += "<legend>" + title + "</legend>"
		s += content
		s += "</fieldset>"
		return s

	def liste(self,reslist):
		"""
			Fonction générant une liste ul/li a partir d'une liste de string python
		"""
		s = "<ul>"
		for i in reslist:
			s += "<li>" + i + "</li>"
		s += "</ul>"
		return s

	def lien(self,titre,adresse):
		s = '<a href="' + adresse + '">' + titre + '</a>'
		return s


	def tableau(self,reslist,table_class = None, head=True, idkey=None):
		"""
			Génére un élément table à partir d'une liste
			La liste s'écrit : 
			[
				[[lab,params],[lab,params],[lab,params]],
				[[lab,params],[lab,params],[lab,params]],
			]
		"""
		ct = 1
		res = '<table '
		if idkey is not None:
			res += 'id="' + idkey + '" '
		if table_class is not None:
			res += 'class="' + table_class + '"'
		res += '>'
		for i in reslist:
			if ct == 1 and head==True:
				res += '<thead>'
			res += '<tr>'
			for c in i:
				res += '<td ' 
				if len(c) > 1:
					if c[1] != "0":
						res += c[1] 
				res += '>'
				if c[0] != "0":
					res += str(c[0])
				res += '</td>' 
			res +='</tr>'
			if ct == 1 and head==True:
				res += '</thead>'
			ct += 1
		res += '</table>'
		return res


	def tab_with_fieldset(self,reslist,table_class=None,auto_class=True):
		"""
			Génére un élément table à partir d'une liste
			La liste s'écrit : 
			{
				1:{legend: 
						[
							[[lab,params],[lab,params],[lab,params]],
							[[lab,params],[lab,params],[lab,params]],
						]
				}, ...
			}	
		"""
		res = ""
		for l,value in reslist.items():
			for key,val in value.items():
				res += '<fieldset>'
				res += '<legend>' + key + '</legend>'
				res += '<table'
				if table_class is not None:
					res += ' class="' + table_class + '"'
				res += '>'
				for i in val:
					res += '<tr>'
					ct = 1
					for c in i:
						# print(c[0])
						ct += 1
						res += '<td '
						if len(c) > 1:
							if c[1] != "0":
								res += c[1]
						elif auto_class:
							print(str(c[0]).find('label'),c[0])
							if str(c[0]).find('<label') != -1:
								res += 'class="tdlab"'
							elif str(c[0]).find('<input') != -1 or str(c[0]).find('<select') != -1:
								res += 'class="tdfield"'
						res += '>'
						if c[0] != "0":
							res += str(c[0])
						res += '</td>' 
					res +='</tr>'
			res += '</table></fieldset>'
			# print(res)
		return res


	def form_cadre(self,request,action,form_content,fileupload = False,arg=None,name=None,option=None):
		"""
			Permet d'encadre un formulaire avec les informations nécéssaire pour la transmission des infos
			Possibilité d'ajouté un bouton envoyer
			form_content est un bloc html contenant les champs du formumlaire
		"""
		if action != "#":
			link = reverse(action,args=arg)
		else:
			link = "#"
		content = '<form action="' + link + '" ' + 'method="post"'
		if name is not None:
			content += ' name="' + name +'"'
		if fileupload:
			content += ' enctype="multipart/form-data"'
		if option is not None:
			content += ' ' +option
		content += '>'
		content += '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrf.get_token(request) + '">'
		content += form_content
		content += '</form>'
		return content


	def submit_button(self,titre="Submit"):
		return '<input type="submit" value="' + titre + '" />'

	def photo_display(self,img_path,img_title=None,width="150",height="auto"):
		if img_title is None:
			if os.path.isfile(img_path):
				img_title = img_path
			else:
				img_title = "Image introuvable"
		l = '<img src="' + img_path + '" '
		l+= 'alt="' + img_title + '" '
		l+= 'style="width:' + width + 'px;height:' + height + 'px;">'
		return l

	def button(self,title=None,address="#",classname="default",glyph=None,balise='a',params=None):
		s = '<' + balise + ' '
		s += 'class="' + 'btn btn-' + classname + '"'
		s += 'href="' + address + '" '
		s += 'role="button" '
		if params is not None:
			s += params
		s+= '>'

		if glyph is not None:
			s += '<span class="glyphicon glyphicon-' + glyph + '" aria-hidden="true"</span>'
		if title is not None:
			s += title 
		s += '</' + balise + '>'
		return s


	def checkbox(self,name,val="",id=None):
		return self.input("checkbox",name,val)

	def input(self,type,name=None,val="", idkey=None):
		s = '<input type="' + type + '" '
		if idkey is not None:
			s+= 'id="' + idkey +'" '
		if name is not None:
			s += 'name="' + name + '" ' 
		s += 'value="' + str(val) + '" '
		s += '/>'
		return s
