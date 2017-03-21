from django import forms as f
from django.test import Client
from .models import Menu, Right_job
from django.urls import resolve,Resolver404
from lawapp.settings import BASE_DIR

class form_menu_create(f.ModelForm):
	class Meta:
		model = Menu
		fields = ('title','url','parent')

	def clean(self):
		cleaned_data = super(form_menu_create, self).clean()
		title = cleaned_data.get("title")
		url = cleaned_data.get("url")
		if title:
			if Menu.objects.count() > 0 :
				for dat in Menu.objects.all():
					if dat.title == title:
						self.add_error("title","Ce titre existe deja")
		if url:
			c = Client()
			response = c.get(url)
			print(response.status_code)
			if int(response.status_code) >= 400:
				self.add_error("url","Adresse inconnue")
		return cleaned_data
	
	def clean_url(self):
		data = self.cleaned_data['url']
		if data:
			if data[0] != '/':
				data = '/' + data
		return data

class form_right_job(f.ModelForm):
	class Meta:
		model = Right_job
		fields = ('menu','job','value')

	def clean(self):
		cleaned_data = super(form_right_job, self).clean()
		menu = cleaned_data.get('menu')
		job = cleaned_data.get('job')
		if menu and job and Right_job.objects.count()>0:
			obj = Right_job.objects.all()
			for i in obj:
				if i.menu == menu and i.job == job:
					raise f.ValidationError("Ce couple menu/fonction a déja des droits.")
		return cleaned_data
