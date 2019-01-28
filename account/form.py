from django import forms
from django.contrib.auth.models import User
from .models import TestModels,RentOutAHome
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,label='username')
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
            raise forms.ValidationError('passwords don\'t match')
        return cd['password2']


class RentOutAHomeForm(ModelForm):

    class Meta:
        model = RentOutAHome
        fields = ['surface_area','number_of_rooms','address','start_date','finale_date','identity_docs','photo'
            ,'cost_per_day']


class TestForm(ModelForm):
    name = forms.CharField(max_length=30)
    family = forms.CharField(max_length=30)

    class Meta:
        model = TestModels
        fields = '__all__'

