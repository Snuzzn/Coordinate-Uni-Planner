from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User 
#         fields = ('username','password1','password2',)
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder':'Username'}), 
#             # 'password1': forms.TextInput(attrs={'placeholder':'Create password'}),
#             # 'password2': forms.TextInput(attrs={'placeholder':'Confirm password'})
#         }