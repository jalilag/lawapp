from django.db import models as m

class gestion_generic(m.Model):
	"""
		Classe abstraite générique
	"""
	nom = m.CharField(max_length=50)

	def __str__(self):
		return self.nom

class member(m.Model):
	"""
		Classe répertoriant les membres du cabinet
	"""
	nom = m.CharField(max_length=50,verbose_name = "Nom")
	prenom = m.CharField(max_length=50)
	fonction = m.ForeignKey('fonction')

	def __str__(self):
		return self.prenom + " " + self.nom + " (" + self.fonction.nom + ")"

class fonction(gestion_generic):
	"""
		Classe listant les différentes fonctions au sein du cabinet
	"""

class groupe(gestion_generic):
	"""
		Classe listant les différents du groupe du cabinet
	"""

class cross_member_group(m.Model):
	"""
		Classe de liaison personel et groupe
	"""
	member = m.ForeignKey('member')
	groupe = m.ForeignKey('groupe')
