from gestion.models import Member
def get_verbose(obj,field_title):
	try:
		return obj._meta.get_field(field_title).verbose_name
	except:
		if field_title == '__all__':
			return 'Géneral'
		else:
			return 'Pas de verbose trouvé pour' + field_title + ' avec l\'objet ' + str(obj)

def get_job_type(request):
	try:
		o = request.session['member']
	except:
		print("non")
		return 0
	m = Member.objects.get(pk=o)
	return m.job.pk