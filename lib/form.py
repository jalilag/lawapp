"""
	Librairie gérant la génération de formulaire
"""

def lib_get_field_from_form(formulaire,obj=None):
	"""
		Génére une liste des labels et des champs en attente de structure html
		Par défaut les champs sont organisés en liste sinon en dictionnaire
		Dans le cas d'un dictionnaire l'organisation est la suivante:
		{fieldName:
			{fieldName_label,label},
			{fieldName_field,field},
		
		}
	"""
	l= dict()
	for field in formulaire:
		lab = '<label for="id_' + field.label.lower() + '">' + field.label + ':</label>'
		l1 = {'label':lab,'field':str(field)}
		l[field.name.lower()] = l1
	if obj is not None:
		for field in l:
			s= str(l[field]['field'])
			print(s)
			if s.find('type="text"') != -1:
				i = s.find('type="text"')
				ii = len('type="text"')
				l[field]['field']=s[:i+ii] + ' value="' + str(obj.__getattr__(field.lower())) + '" ' + s[i+ii:]
			elif s.find('select multiple="multiple"') != -1:
				print(obj.__getattr__(field.lower()))
	if formulaire.errors.__str__() != "":
		l["errors"] = formulaire.errors.__str__()
	return l