"""
	Librairie permettant la gestion et la génération de liste à partir des modeles
"""
from .html import libHtml
from django.urls import reverse
from lawapp.settings import MEDIA_URL

def build_list(obj,fields,address_name,res_num=10,bloc_num=1,orderby='id', head=True):
	"""
		Fonction de construction de liste à partir d'un modele
		res_num selectionne le nombre de résultat, si resnum = 0 on prend tout les resultats
		bloc_num permet le découpage en page, si il est sup au nbre de page possible la derniere page sera retournée
		head ajoute une première ligne titre avec les verboses names
		orderby permet de classer	
	""" 
	slist = list()
	mainlist = list()
	l2 = libHtml()
	c = 0
	o = obj.objects.order_by(orderby)
	N = len(o)
	if res_num > 0 and (int(N/res_num) < bloc_num-1):
		bloc_num = int(N/res_num)+1
	if head:
		for j in fields:
			if j == orderby:
				arg = ['1','-'+j,res_num]
			else:
				arg = ['1',j,res_num]
			if j == 'delete':
				l1 = ['']
			else:
				l1 = [l2.lien(obj._meta.get_field(j).verbose_name,reverse(address_name,args=arg))]
			slist.append(l1)
		mainlist.append(slist)
	for i in o:
		c += 1
		if c>(bloc_num-1)*res_num and c<=bloc_num*res_num or res_num == 0:
			slist = list()
			for j in fields:
				if j == "photo":
					l1 = [l2.photo_display(MEDIA_URL+str(i.__getattribute__(j)))]
				elif j == "delete":
					l1 = [l2.checkbox('delete',i.__getattribute__('id'))]
				else:
					l1 = [i.__getattr__(j)]
				slist.append(l1)
			mainlist.append(slist)
	return mainlist

def build_list_html(obj,fields,listaddress,resperpage=10,bloc_num=1,orderby='id', head=True, title = None):
	"""
		Fonction de mise en forme de liste a partir de modeles
		Affiche une liste avec tri possible
		Nombre de res
		Choix des pages
	"""
	l2 = libHtml()
	class_bsp = 'col-lg-6 col-md-offset-3'
	# Boutons nombre de res
	res = ['5','10','20','50']
	but = '<table><tr>'
	for i in res:
		arg = ['1',orderby,i]
		but +='<td>'
		but += l2.button(i,reverse(listaddress,args=arg))
		but +='</td>'
	if 'delete' in fields:
		but += '<td><input type="submit" value="Delete" /></td>'
	but += '</tr></table>'
	content = l2.container(l2.container(but,'div',class_bsp),'div','row')
	# Génération de la liste sous forme de tableau
	N = obj.objects.count()
	l = l2.tableau(build_list(obj,fields,listaddress,resperpage,bloc_num,orderby,head),'class_list')

	content += l2.container(l2.container(l,'div',class_bsp),'div','row')
	# Génération des liens vers les pages
	content += l2.container(l2.container(res_per_page(listaddress,orderby,N,resperpage,bloc_num),'div','col-lg-6 col-md-offset-3'),'div','row')
	if title is not None:
		t = l2.container(l2.container(l2.titre(title),'div','col-lg-6'),'div','row')
		content = t + content	 
	content = l2.container(content,'section')
	return content

def res_per_page(address_name,orderby,res_num,resperpage,currentpage):
	"""
		Fonction permettant de générer une série de lien vers les pages de résultat
	"""
	l2 = libHtml()
	N = int(res_num/resperpage)+1
	if N > 1:
		content = '['
		for i in range(currentpage-3,currentpage):
			if i > 0:
				arg = [str(i),orderby,str(resperpage)]
				content += l2.lien(str(i),reverse(address_name,args=arg))
				if i < currentpage - 1:
					content += ', '
				if i == currentpage -1 and currentpage != N:
					content += ' ... '
		for i in range(currentpage+1,currentpage+4):
			if i <= N:
				arg = [str(i),orderby,str(resperpage)]
				content += l2.lien(str(i),reverse(address_name,args=arg))
				if i < N:
					content += ', '
		content += ']'
	else:
		content =''
	return content


