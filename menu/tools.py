from .models import Menu, Right_job,Right_member,Right_team
from gestion.models import Member
from lib.model import get_field_by_string

def get_user_info(request,refkey):
	try:
		o = request.session['member']
		m = Member.objects.get(pk=o)
		if refkey == "team.id":
			return m.get_team_id()
		else:
			return get_field_by_string(m,refkey)
	except:
		return None

def check_access_with_job(job_id,menu_id):
	r = 1
	if job_id is None:
		r = 0
	else:
		if Right_job.objects.filter(job=job_id,menu=menu_id).count() == 1:
			r *= int(Right_job.objects.get(job=job_id,menu=menu_id).value)
	return r

def check_access_with_team(team_id,menu_id):
	r = 1
	if team_id is None:
		r = 0
	elif isinstance(team_id,list):
		for i in team_id:
			if Right_team.objects.filter(team=i,menu=menu_id).count() == 1:
				r =  0
	else:
		if Right_team.objects.filter(team=team_id,menu=menu_id).count() == 1:
			r =  0
	return r

def check_access_with_member(member_id,menu_id):
	r = 1
	if member_id is None:
		r = 0
	else:
		if Right_member.objects.filter(member=member_id,menu=menu_id).count() == 1:
			r = 0
	return r

def check_access(request,menu_id):
	r_id = check_access_with_member(get_user_info(request,"id"),menu_id)
	r_job = check_access_with_job(get_user_info(request,"job.id"),menu_id)
	r_team = check_access_with_team(get_user_info(request,"team.id"),menu_id)
	if r_job and r_id and r_team:
			return True
	return False

def get_valid_menu(request,menu_parent_id = None):
	if Menu.objects.count() > 0:
		if menu_parent_id is None:
			m = Menu.objects.all()
		else:
			m = Menu.objects.filter(parent=menu_parent_id)
		l =list()
		for i in m:
			if check_access(request,i.pk):
				l.append(i)
		if len(l) > 0:
			return l
	return None

