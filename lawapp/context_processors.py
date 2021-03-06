from django.conf import settings 
from lib.html import libHtml
from gestion.views import manage_quick_connect
from menu.views import generate_menu
from gestion.models import Member

def gen_var(request):
	gens = {}
	gens['BASE_DIR'] = settings.BASE_DIR
	gens['CHARSET'] = 'UTF-8'
	gens['LANG_CODE'] = settings.LANGUAGE_CODE
	menu = generate_menu(request)
	if menu is not None:
		gens['MENU'] = menu
	 
	return gens

def quick_connect(request):
	s = libHtml()
	box_connection = {}
	if request.session.get('member') is not None:
		o = Member.objects.get(id=request.session['member'])
	else:
		o = None
	l = manage_quick_connect(o)
	box_connection['connection'] = l
	return box_connection
