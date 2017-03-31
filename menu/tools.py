from .models import Menu, Right_job

def get_access(job_id,menu_id):
	try:
		r=Right_job.objects.get(job=job_id,menu=menu_id)
		r = r.value
	except:
		if job_id > 0:
			r=1
		else:
			r=0
	return r


def get_valid_menu_with_job(job_id,menu_parent_id = None):
	if Menu.objects.count() > 0:
		if menu_parent_id is None:
			m = Menu.objects.all()
		else:
			m = Menu.objects.filter(parent=menu_parent_id)
		l =list()
		for i in m:
			if get_access(job_id,i.pk):
				l.append(i)
		print(len(l))
		if len(l) > 0:
			return l
	return None
