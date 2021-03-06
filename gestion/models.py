from django.db import models as m
from configuration.models import Config
import os
from lawapp.settings import MEDIA_URL, MEDIA_ROOT
from passlib.hash import pbkdf2_sha256

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
	job_choices = (
		(1,'Assistant'),
		(2,'Avocat'),
	)
 
	def get_image_path(self,filename):
		fileformat = os.path.splitext(filename)[1]
		filename = os.path.splitext(filename)[0]
		if not self.pk:
			if Member.objects.count() > 0:
				filename = str(Member.objects.latest("id").id+1)
				print("filename",filename)
			else:
				filename = "1"
		else:
			filename = str(self.id)
		filename += "temp"
		print(filename)
			# Ajouter suppression du fichier deja existant
		if os.path.isfile(MEDIA_ROOT + '/member/photos/'+ filename + fileformat):
			os.remove(MEDIA_ROOT + '/member/photos/'+ filename + fileformat)
		return "member/photos/" + filename + fileformat

	login = m.CharField(max_length=50, verbose_name="Login")
	password = m.CharField(max_length=128, verbose_name="Mot de passe")
	lastname = m.CharField(max_length=50,verbose_name = "Nom")
	firstname = m.CharField(max_length=50, verbose_name = "Prénom")
	photo = m.ImageField(upload_to=get_image_path,verbose_name="Photo")
	job = m.ForeignKey('Job',verbose_name="Fonction")
	team = m.ManyToManyField(Team,verbose_name="Equipe")


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

	def get_team_id(self):
		N = len(self.team.all())
		if N > 0:
			l = list()
			for i in range(0,N):
				l.append(self.team.all()[i].pk)
			return l
		return None

	def delete(self):
		l = os.listdir(MEDIA_ROOT + "/member/photos")
		for i in l:
			filename = os.path.splitext(i)[0]
			if filename == str(self.pk):
				os.remove(MEDIA_ROOT + "/member/photos/" + i)
		super(Member, self).delete()

	def check_password(self,txt):
		"""
			Check if the password is correct
		"""
		return pbkdf2_sha256.verify(txt,self.password)
	
	def encrypt(txt):
		"""
			Encrypt the password
		"""
		return pbkdf2_sha256.encrypt(txt,rounds=12000,salt_size=32)

	def connect(self,request):
		request.session['member'] = self.id
		request.session.set_expiry(int(Config.objects.get(title="EXPIRY_DURATION").value)) 



class Job(m.Model):
	"""
		Classe listant les différentes fonctions au sein du cabinet
	"""
	title = m.CharField(max_length=50,verbose_name="Fonction")

	def __str__(self):
		return self.title

# class CrossMemberTeam(m.Model):
# 	"""
# 		Classe de liaison personel et groupe
# 	"""
# 	# class Meta:
# 	# 	auto_created = True

# 	member = m.ForeignKey('Member',on_delete=m.CASCADE)
# 	team = m.ForeignKey('Team',on_delete=m.CASCADE)
