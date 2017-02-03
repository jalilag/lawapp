

def lib_get_field_from_form(formulaire,list_type='list'):
	"""
		Génére une liste des labels et des champs en attente de structure html
		Par défaut les champs sont organisés en liste sinon en dictionnaire
		Dans le cas d'un dictionnaire l'organisation est la suivante:
		{fieldName:
			{fieldName_label,label},
			{fieldName_field,field},
		
		}
	"""
	if list_type == "list":
		l= list()
		for field in formulaire:
			lab = '<label for="id_' + field.label + '">' + field.label + ':</label>'
			l.append((lab,str(field)))
	else:
		l= dict()
		for field in formulaire:
			lab = '<label for="id_' + field.label.lower() + '">' + field.label + ':</label>'
			l1 = {'label':lab,'field':str(field)}
			l[field.name.lower()] = l1
		if formulaire.errors.__str__() != "":
			l["errors"] = formulaire.errors.__str__()
	return l



