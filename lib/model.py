def get_verbose(obj,field_title):
	try:
		return obj._meta.get_field(field_title).verbose_name
	except:
		return 'Pas de verbose trouvé pour' + field_title + ' avec l\'objet ' + str(obj)