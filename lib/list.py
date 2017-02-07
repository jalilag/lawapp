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
				arg = [bloc_num,'-'+j]
			else:
				arg = [bloc_num,j]

			l1 = [l2.lien(obj._meta.get_field(j).verbose_name,reverse(address_name,args=arg))]
			# l1 = [obj._meta.get_field(j).verbose_name]
			slist.append(l1)
		mainlist.append(slist)
	for i in o:
		c += 1
		if c>(bloc_num-1)*res_num and c<=bloc_num*res_num or res_num == 0:
			slist = list()
			for j in fields:
				if j == "photo":
					l1 = [l2.photo_display(MEDIA_URL+str(i.__getattribute__(j)))]
				else:
					l1 = [i.__getattr__(j)]
				slist.append(l1)
			mainlist.append(slist)
	return mainlist

def build_list_html(obj,fields,listaddress,res_num=10,bloc_num=1,orderby='id', head=True):
	l = build_list(obj,fields,listaddress,res_num,bloc_num,orderby,head)
	l2 = libHtml()
	N = obj.objects.count()
	content = l2.container(l2.tableau(l),'div','col-lg-12')
	content += l2.container(res_per_page(listaddress,[orderby],N,res_num,bloc_num),'div','col-lg-12')
	content = l2.container(content,'section','row')
	return content

def res_per_page(address_name,arg_list,res_num,resperpage,currentpage):
	l2 = libHtml()
	N = int(res_num/resperpage)+1
	if N > 1:
		content = '['
		for i in range(currentpage-3,currentpage):
			if i > 0:
				arg = list(arg_list)
				arg.insert(0,str(i))
				content += l2.lien(str(i),reverse(address_name,args=arg))
				if i < currentpage - 1:
					content += ', '
				if i == currentpage -1 and currentpage != N:
					content += ' ... '
		for i in range(currentpage+1,currentpage+4):
			if i <= N:
				arg = list(arg_list)
				arg.insert(0,str(i))
				content += l2.lien(str(i),reverse(address_name,args=arg))
				if i < N:
					content += ', '
		content += ']'
	else:
		content =''
	return content


