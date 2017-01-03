from django.middleware import csrf
from django.urls import reverse

def lib_new_form(request,action,form_content,submit=True):
	"""
		Génére un formulaire complet à partir de la génération automatique des champs de django
	"""
	content = '<form action="' + reverse(action) + '" ' + 'method="post">'
	content += '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrf.get_token(request) + '">'
	content += form_content
	if submit:
		content += '<input type="submit" value="Submit" />'
	content += '</form>'
	return content

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
			l[field.label.lower()] = l1
	l["submit"] = {'field': '<input type="submit" value="Submit" />'} 
	return l

def lib_gen_table_from_list(l):
	"""
		Génére un élément table à partir d'une liste
		La liste s'écrit : 
		[
			[[lab,class,lspan,colspan],[lab,class,lspan,colspan],[lab,class,lspan,colspan]],
			[[lab,class,lspan,colspan],[lab,class,lspan,colspan],[lab,class,lspan,colspan]],
		]
	"""
	res = '<table>'
	for i in l:
		res += '<tr>'
		for c in i:
			res += '<td ' 
			if len(c) > 1:
				if c[1] != "0":
					res += 'class="' + c[1] + '"'
			if len(c) > 3:
				res += 'rowspan="' + c[2] + '" colspan="' + c[3] + '" '
			res += '>'
			if c[0] != "0":
				res += c[0]
			res += '</td>' 
		res +='</tr>'
	res += '</table>'
	return res   

