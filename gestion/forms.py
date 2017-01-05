from django import forms as f
from .models import member

class form_member_create(f.ModelForm):
	class Meta:
		model = member
		fields = '__all__'

	def clean_nom(self):
		nom = self.cleaned_data['nom']
		raise f.ValidationError("azeazeazea")
		return nom


