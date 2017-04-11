from gestion.models import Member
def get_verbose(obj,field_title):
	try:
		return obj._meta.get_field(field_title).verbose_name
	except:
		if field_title == '__all__':
			return 'Géneral'
		else:
			return 'Pas de verbose trouvé pour' + field_title + ' avec l\'objet ' + str(obj)


def get_field_by_string(instance, field):
	field_path = field.split('.')
	attr = instance
	for elem in field_path:
		try:
			attr = getattr(attr, elem)
		except AttributeError:
			attr = None
	if callable(attr):
		return '%s' % attr
	return attr
