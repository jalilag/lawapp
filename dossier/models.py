from django.db import models as m

class Intervenant(m.Model):
	entity_type_choices = (
		(1, 'Personne physique'),
		(2, 'Personne morale')
	)
	entity_type = m.IntegerField(choices=entity_type_choices,default=1)
	firstname = m.CharField(max_length=50,blank=True)
	lastname = m.CharField(max_length=50)

class Dossier(m.Model):
	"""
		Classe de création de dossier
	"""
	client = m.ManyToManyField('Intervenant',related_name='client')
	adversaire = m.ManyToManyField('Intervenant',related_name='adversaire')

