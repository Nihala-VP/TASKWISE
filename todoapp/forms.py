

from django import forms

from django.contrib.auth.models import User

from todoapp.models import Todo


from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    class Meta:

        model = User

        fields= ["username","email","password1","password2"]



class LoginForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField()


class TodoForm(forms.ModelForm):

    class Meta:

        model = Todo

        exclude = ("owner",)
