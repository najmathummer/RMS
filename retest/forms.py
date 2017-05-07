from django.contrib.auth.models import User
from django import forms

from django import forms
class RetestForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password']


