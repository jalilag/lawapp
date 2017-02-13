from django.db import models as m
import os
from lawapp.settings import MEDIA_URL, MEDIA_ROOT

class Team(m.Model):
	"""
		Classe listant les différentes équipes du cabinet
	"""
	title = m.CharField(max_length=50, verbose_name="Nom de l'équipe")
	
	def __str__(self):
		return self.title


class Member(m.Model):
	"""
		Classe répertoriant les membres du cabinet
	"""
	def get_image_path(self,filename):
		fileformat = os.path.splitext(filename)[1]
		filename = os.path.splitext(filename)[0]
		if not self.pk:
			filename = str(Member.objects.order_by("-id")[0].id +1)
		else:
			filename = str(self.id)
		return "member/photos/" + filename + fileformat


	lastname = m.CharField(max_length=50,verbose_name = "Nom")
	firstname = m.CharField(max_length=50, verbose_name = "Prénom")
	photo = m.ImageField(upload_to=get_image_path,verbose_name="Photo")
	job = m.ForeignKey('Job',verbose_name="Fonction")
	team = m.ManyToManyField(Team,through='CrossMemberTeam',verbose_name="Equipe")

	def __str__(self):
		return self.firstname + " " + self.lastname + " (" + self.job.title + ")"
	
	def __getattr__(self,nom):
		if nom == 'job':
			l = str(self.job.title)
		if nom == 'team':
			N = len(self.team.all())
			l = "no team"
			if N > 0:
				l = ""
				for i in range(0,N):
					l+= str(self.team.all()[i])
					if i < N-1:
						l+= ', '
		else:
			l = super(Member,self).__getattribute__(nom)		
		return l

	def delete(self):
		l = os.listdir(MEDIA_ROOT + "/member/photos")
		for i in l:
			filename = os.path.splitext(i)[0]
			if filename == str(self.pk):
				os.remove(MEDIA_ROOT + "/member/photos/" + i)
		super(Member, self).delete()


class Job(m.Model):
	"""
		Classe listant les différentes fonctions au sein du cabinet
	"""
	title = m.CharField(max_length=50,verbose_name="Fonction")

	def __str__(self):
		return self.title

class CrossMemberTeam(m.Model):
	"""
		Classe de liaison personel et groupe
	"""
	class Meta:
		auto_created = True

	member = m.ForeignKey('Member')
	team = m.ForeignKey('Team')
