from django.shortcuts import get_object_or_404,redirect
from django.http import JsonResponse
from django.apps import apps
from lib.list import list_of_one
from lawapp.settings import HOME_URL
# from lib.url import lib_get_all_urls
# from lib.html import libHtml

# def list_links(request):
# 	l = lib_get_all_urls()
# 	l1 = list()
# 	l2 = libHtml()
# 	for i in l:
# 		l1.append(l2.lien(i,i))
# 	l1.sort()
# 	content = l2.liste(l1)
# 	return render(request,"base.html",locals())

def ajax_list_delete_process(request):
	if request.method == "POST" and 'delete' in request.POST:
		l = dict(request.POST)
		adresslist = list_of_one(l['delete_address'])
		model_name =  list_of_one(l['delete_model'])
		app_name =  list_of_one(l['delete_app'])
		if app_name and model_name:
			m = apps.get_model(app_name,model_name)
			for i in l['delete']:
				o = get_object_or_404(m, pk=int(i))
				o.delete()
			return redirect(adresslist)
	return redirect(HOME_URL)

def ajax_list_delete(request):
	res = request.GET.get('res', None)
	model_name = request.GET.get('model_name',None)
	app_name = request.GET.get('app_name',None)
	if res and model_name:
		res2 = res.split(',')
		val = ''
		m = apps.get_model(app_name,model_name)
		for i in res2:
			o = get_object_or_404(m, pk=int(i))
			val += '\t- ' + str(o) + '\n'
		data = {'val':val}
	else:
		data = {'val':error}		
	return JsonResponse(data)

