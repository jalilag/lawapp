from django.core.urlresolvers import get_resolver

def lib_get_all_urls():
	"""
		Fonction retournant sous forme de liste toutes les urls défini dans l'appli
	"""
	reslist = list()
	l = get_resolver(None).reverse_dict.values()
	for i in l:
		reslist.append(i[0][0][0])
	return reslist
