from .html import libHtml
from lawapp.settings import MEDIA_URL
def build_list(obj,fields,res_num=10,bloc_num=1,orderby='id', head=True):
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
			l1 = [obj._meta.get_field(j).verbose_name]
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

