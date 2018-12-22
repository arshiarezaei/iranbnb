from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,label='Your name')
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='password2')

    class Meta:
        model=User
        fields=('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('passwords dont match')
        return cd['password2']