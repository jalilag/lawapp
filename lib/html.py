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

	def div(self, content, classe=None, idtxt = None):
		s = '<div '
		if idtxt is not None:
			s += 'id="' + idtxt +'"'
		if classe is not None:
			s += 'class="' + classe + '"'
		s +='>' + content + '</div>'
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

	def tableau(self,reslist,table_class = None,head=True):
		"""
			Génére un élément table à partir d'une liste
			La liste s'écrit : 
			[
				[[lab,class,lspan,colspan],[lab,class,lspan,colspan],[lab,class,lspan,colspan]],
				[[lab,class,lspan,colspan],[lab,class,lspan,colspan],[lab,class,lspan,colspan]],
			]
		"""
		ct = 1
		res = '<table '
		if table_class is not None:
			res += 'class="' + table_class + '"'
		res += '>'
		for i in reslist:
			if ct == 1 and head:
				res += '<thead>'
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
			if ct == 1 and head:
				res += '</thead>'
				ct += 1
		res += '</table>'
		return res

	def form_cadre(self,request,action,form_content,fileupload = False):
		"""
			Permet d'encadre un formulaire avec les informations nécéssaire pour la transmission des infos
			Possibilité d'ajouté un bouton envoyer
			form_content est un bloc html contenant les champs du formumlaire
		"""
		content = '<form action="' + reverse(action) + '" ' + 'method="post"'
		if fileupload:
			content += ' enctype="multipart/form-data"'
		content += '>'
		content += '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrf.get_token(request) + '">'
		content += form_content
		content += '</form>'
		return content

	def form_set_all(self,request,action,form_content,form,title,fileupload=False):
		"""
			Mise en forme complete d'un formulaire
		"""
		content = self.div(self.form_cadre(request,action,form_content,fileupload), "col-lg-8")
		if form is not None:
			if form.errors.__str__() != "":
				content += self.div(form.errors.__str__(),"col-lg-4")
		content = self.div(content,"row")
		content = self.div(self.div(self.titre(title),"col-lg-12"),"row") + content  
		content = self.div(content, "container")
		return content

	def submit_button(self,titre="Submit"):
		return '<input type="submit" value="' + titre + '" />'

	def photo_display(self,img_path,img_title=None,width="100",height="100"):
		if img_title is None:
			img_title = img_path
		l = '<img src="' + img_path + '" '
		l+= 'alt="' + img_title + '" '
		l+= 'style="width:' + width + 'px;height:' + height + 'px;">'
		return l