from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
class CreateUserForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['first_name','last_name','username','email','password1','password2']
