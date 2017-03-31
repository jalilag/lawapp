from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member
from lawapp.settings import MEDIA_ROOT
import os

@receiver(post_save, sender=Member)
def model_post_save(sender, **kwargs):
	l = kwargs['instance'].__dict__
	fileformat = os.path.splitext(l['photo'])[1]
	filename = str(l["id"]) + fileformat
	print(filename,l['photo'])
	Member.objects.filter(pk=l['id']).update(photo="member/photos/"+filename)
	if os.path.isfile(MEDIA_ROOT + '/' + l['photo']):
		os.rename(MEDIA_ROOT + '/' + l['photo'],MEDIA_ROOT + '/member/photos/' + filename)
		print("renomage ok")
