from menu.models import Menu
def get_verbose(obj,field_title):
	try:
		return obj._meta.get_field(field_title).verbose_name
	except:
		if field_title == '__all__':
			return 'Géneral'
		else:
			return 'Pas de verbose trouvé pour' + field_title + ' avec l\'objet ' + str(obj)

def generate_menu():
	if Menu.objects.count() > 0:
		s ='<ul id="menu-accordeon">'
		o = Menu.objects.all()
		for i in o:
			if i.parent is None:
				s += '<li>'
				if i.url is not None:
					s += '<a href="' + i.url + '">'
				else:
					s += '<a href="#">' 
				s += i.title + '</a>'
				print(o.filter(parent=i.id).count())
			if o.filter(parent=i.id).count() > 0: 
				s += '<ul>'
				oo = o.filter(parent=i.id)
				for j in oo:
					s += '<li>'
					if j.url is not None:
						s += '<a href="' + j.url + '">'
					else:
						s += '<a href="#">' 
					s += j.title + '</a></li>'
				s += '</ul>'
			s += '</li>'
		s += '</ul>'
	else:
		s = '<p>No menu</p>'
	return s
