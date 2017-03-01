from .model import get_verbose
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
	if formulaire.errors.__str__() != "":
		if obj is not None:
			errs = dict(formulaire.errors)
			s = '<ul>'
			for key,val in errs.items():
				ss= str(val)
				s += '<li>' + get_verbose(obj,key) + ' : ' + ss[ss.find('<li>')+4:-10] + '</li>'
			s += '</ul>'
			l["errors"] = s
		else:
			l["errors"] = formulaire.errors.__str__()			
	return l