from django.db import models as m
from gestion.models import Job, Team, Member
# Create your models here.

class Menu(m.Model):
	title = m.CharField(max_length=50, verbose_name="Titre")
	url = m.CharField(max_length=50, verbose_name="Adresse", null=True,blank=True)
	parent = m.ForeignKey("self", null=True, blank=True, verbose_name="Parent")
	# linked_right_job = m.ManyToManyField(Job, verbose_name="Droits / fonctions",through="Right_job", through_fields=('menu','job'), blank=True)
	# right_team = m.ManyToManyField(Team, verbose_name="Droits / Equipes")
	# right_member = m.ManyToManyField(Member, verbose_name="Droits / Membres")

	def __str__(self):
		return self.title

	def __getattr__(self,nom):
		l = super(Menu,self).__getattribute__(nom)		
		return l




class Right_job(m.Model):
	value_choices = (
			(0,'Accès autorisé'),
			(1,'Accès interdit'),
	)
	menu = m.ForeignKey(Menu,verbose_name="Menu")
	job = m.ForeignKey(Job,verbose_name="Fonction")
	value = m.IntegerField(choices=value_choices,default=1,verbose_name="Droits")

	def __str__(self):
		return self.value_choices[self.value][1] + " sur " + self.menu.title + " pour " + self.job.title + " "

	def __getattr__(self,nom):
		if nom == 'job':	
			l = str(self.job.title)
		if nom == 'menu':
			l = str(self.menu.title)
		if nom == 'value':
			v = dict(self.value_choices)
			l = v[self.value]
		else:
			l = super(Right_job,self).__getattribute__(nom)		
		return l