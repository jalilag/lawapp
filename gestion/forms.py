from django import forms as f
from .models import member

class form_member_create(f.ModelForm):
	class Meta:
		model = member
		fields = '__all__'