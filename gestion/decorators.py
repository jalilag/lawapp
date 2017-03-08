from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .models import Member

def registered_user(function):
	"""Decorator to grant access to user only."""
	def decorator(request,*args, **kwargs):
		try:
			o = request.session['member']
		except:
			o = None
		if o is None:
			request.session['current_url'] = request.path
			return redirect('member_login')
		return function(request,*args, **kwargs)
	return decorator

