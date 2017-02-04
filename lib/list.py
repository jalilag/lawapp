from .html import libHtml
from lawapp.settings import MEDIA_URL
def build_list(obj,fields,res_num=10, head=True):
	"""
		Fonction de construction de liste à partir d'un modele
	""" 
	l4 = list()
	l5 = list()
	l2 = libHtml()
	print(float(2.5))
	print(obj._meta.get_field('lastname').verbose_name)
	c = 0
	o = obj.objects.all()
	if res_num <= 0:
		N = res_num
	else:
		N = len(o)
	if head:
		for j in fields:
			l1 = [obj._meta.get_field(j).verbose_name]
			l4.append(l1)
		l5.append(l4)
	for i in o:
		if N>res_num and c<res_num:
			c += 1
			l4 = list()
			for j in fields:
				if j == "photo":
					l3 = [l2.photo_display(MEDIA_URL+str(i.__getattribute__(j)))]
				else:
					l3 = [i.__getattr__(j)]
				l4.append(l3)
			l5.append(l4)
	return l5

