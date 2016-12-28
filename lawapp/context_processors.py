from django.conf import settings 
def gen_var(request):
	gens = {}
	gens['BASE_DIR'] = settings.BASE_DIR
	gens['CHARSET'] = 'UTF-8'
	gens['LANG_CODE'] = settings.LANGUAGE_CODE
	return gens
	