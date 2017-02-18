from django import forms as f
from .models import Member, Job, Team

class form_member_create(f.ModelForm):
	class Meta:
		model = Member
		fields = '__all__'

	def clean(self):
		cleaned_data = super(form_member_create, self).clean()
		photo = cleaned_data.get("photo")
		lastname = cleaned_data.get("lastname")
		firstname = cleaned_data.get("firstname")
		for dat in Member.objects.all():
			if dat.firstname == firstname and dat.lastname == lastname:
				raise f.ValidationError("Ce membre existe déja", code="err1")
		return cleaned_data

class form_member_edit(f.ModelForm):
	class Meta:
		model = Member
		fields = '__all__'

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
