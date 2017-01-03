from django.db import models as m

# Create your models here.

class Articles(m.Model):
	titre = m.CharField(max_length=100)
	auteur = m.CharField(max_length=50)
	content = m.TextField(null=True)
	date = m.DateTimeField(auto_now=False,auto_now_add=True, verbose_name="Date de parution")

	def __str__(self):
		return self.titre + " (" + self.auteur + ")"

