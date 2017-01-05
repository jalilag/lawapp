from django.middleware import csrf
from django.urls import reverse

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

	def tableau(self,reslist,table_class = None):
		"""
			Génére un élément table à partir d'une liste
			La liste s'écrit : 
			[
				[[lab,class,lspan,colspan],[lab,class,lspan,colspan],[lab,class,lspan,colspan]],
				[[lab,class,lspan,colspan],[lab,class,lspan,colspan],[lab,class,lspan,colspan]],
			]
		"""
		res = '<table '
		if table_class is not None:
			res += 'class="' + table_class + '"'
		res += '>'
		for i in reslist:
			res += '<tr>'
			for c in i:
				res += '<td ' 
				if len(c) > 1:
					if c[1] != "0":
						res += 'class="' + c[1] + '"'
				if len(c) > 3:
					res += 'rowspan="' + c[2] + '" colspan="' + c[3] + '" '
				res += '>'
				if c[0] != "0":
					res += c[0]
				res += '</td>' 
			res +='</tr>'
		res += '</table>'
		return res

	def form_cadre(self,request,action,form_content):
		"""
			Permet d'encadre un formulaire avec les informations nécéssaire pour la transmission des infos
			Possibilité d'ajouté un bouton envoyer
			form_content est un bloc html contenant les champs du formumlaire
		"""
		content = '<form action="' + reverse(action) + '" ' + 'method="post">'
		content += '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrf.get_token(request) + '">'
		content += form_content
		content += '</form>'
		return content

	def submit_button(self,titre="Submit"):
		return '<input type="submit" value="' + titre + '" />'