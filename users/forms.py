from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  .models import UserProfile


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name','phone_number']