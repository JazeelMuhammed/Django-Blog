from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_Profile

class AbstractUserForm(UserCreationForm):
    email = forms.EmailField()
    #  Meta class will contain extra info about the model class

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# MODELFORM allows us to create a FORM that will work with a
# "specific database model. Here that model in db is "User".
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # SINCE WE ONLY DISPLAY USERNAME AND EMAIL IN USER_PROFILE
        fields = ['username', 'email']

# SINCE "USER_PROFILE MODEL" IS SEPERATE FROM "USER MODEL"
# WE SHOULD CREATE A SEPERATE MODEL FOR UPDATING USER_PROFILE
# MODELFORM allows us to create a FORM that will work with a
# "specific database model. Here that model in db is "USER_PROFILE".
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = ['profile_pic']