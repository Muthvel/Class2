from django import forms
from . models import Customer
from django.forms.widgets import PasswordInput

class SignupForm(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignupModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {'password':PasswordInput}
