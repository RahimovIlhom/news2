from django.forms import ModelForm

from .models import Profile
from django.contrib.auth.models import User


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'birth_of_day']
