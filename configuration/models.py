from django.db import models as m

# Create your models here.

class Config(m.Model):
	title = m.CharField(max_length=50)
	description = m.CharField(max_length=50)
	value = m.CharField(max_length=50)
