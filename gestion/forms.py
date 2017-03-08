from django import forms as f
from .models import Member, Job, Team
from passlib.hash import pbkdf2_sha256

class form_member_create(f.ModelForm):
	password = f.CharField(widget=f.PasswordInput())
	class Meta:
		model = Member
		fields = '__all__'

	def clean(self):
		cleaned_data = super(form_member_create, self).clean()
		lastname = cleaned_data.get("lastname")
		firstname = cleaned_data.get("firstname")
		login = cleaned_data.get("login")
		password = cleaned_data.get("password")
		if password:
			if len(password) < 5:
				self.add_error("password","Le mot de passe doit au moins faire 5 caractères")
			if login and firstname and lastname:
				if lastname in password or firstname in password or login in password:
					self.add_error("password","Le mot de passe ne doit pas contenir le prénom, le nom ou le login")
		if Member.objects.count()>0:
			for dat in Member.objects.all():
				if dat.login == login:
					self.add_error("login","Ce login existe déja")
		return cleaned_data

	def clean_password(self):
		data = self.cleaned_data['password']
		enc_password = Member.encrypt(data)
		return enc_password

class form_member_edit(f.ModelForm):
	class Meta:
		model = Member
		exclude = ['password']
	
	def clean(self):
		cleaned_data = super(form_member_edit, self).clean()
		login = cleaned_data.get("login")
		if Member.objects.count()>0:
			for dat in Member.objects.all():
				if dat.login == login and dat.id != self.instance.id:
					self.add_error("login","Ce login existe déja")
		return cleaned_data


class form_login(f.ModelForm):
	class Meta:
		model = Member
		fields = ('login','password')
		widgets = {'password':f.TextInput(attrs={'type':'password'})}
	def clean(self):
		cleaned_data = super(form_login, self).clean()
		login = cleaned_data.get("login")
		password = cleaned_data.get("password")
		try:
			o=Member.objects.get(login=login)
			if o.check_password(password) is not True:
				self.add_error('password',"Le mot de passe est incorrect !")
		except:
			self.add_error("login","Ce login n'éxiste pas !")
		return cleaned_data

class form_job_create(f.ModelForm):
	class Meta:
		model = Job
		fields = '__all__'

	def clean_title(self):
		title = self.cleaned_data['title']
		for job in Job.objects.all():
			if job.title == title:
				raise f.ValidationError("Titre déja existant",code="Err2")
		return title

class form_team_create(f.ModelForm):
	class Meta:
		model = Team
		fields = '__all__'

	def clean_title(self):
		title = self.cleaned_data['title']
		for team in Team.objects.all():
			if team.title == title:
				raise f.ValidationError("Titre déja existant",code="Err2")
		return title
