from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import BaseUserManager

from .models import TrainerProfile, ContactTrainerRequest


class AddTrainerUserNameForm(forms.ModelForm):
    """ this form is used for trainer creation """
    default_password = BaseUserManager().make_random_password()

    user_name = forms.CharField(initial='trainer',max_length=20, required=True)
    password1 = forms.CharField(initial=default_password, required=True)
    password2 = forms.CharField(initial=default_password, required=True)
    firstname = forms.CharField(max_length=50, required=True )
    lastname = forms.CharField(max_length=50, required=True )
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['user_name', 'password1', 'password2', 'firstname', 'lastname', 'email']

    

    def create(self, validated_data):
        validated_data.pop('password2') # you should pop this before create
        user = User.objects.create_user(
            **validated_data
        )
        return user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError(
                 "passwords are not the same!!.")
        
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'user_name': 'Trainer',
            'password1':'Password',
            'password2':'Retype Password',
            'firstname':'First Name',
            'lastname': 'Last Name',
            'email':'Email',
        }

        for field in self.fields:
            if field != 'password2' and field != 'username' and field != 'password1':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black rounded-0 add_trainer-form-input'
                self.fields[field].label = False

class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        exclude = ('user',)
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'phone': 'Mobile Number',
            'bio': 'Short bio',
        }

        for field in self.fields:
            if field != 'image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 add_trainer-form-input'
            self.fields[field].label = False


class ViewTrainerUserNameForm(forms.ModelForm):
    """ this form is used for trainer edit """
    
    first_name = forms.CharField(max_length=50, required=True )
    last_name = forms.CharField(max_length=50, required=True )
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'first_name':'First Name',
            'last_name': 'Last Name',
            'email':'Email',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 add_trainer-form-input'
            self.fields[field].label = False


class ContactTrainerRequestForm(forms.ModelForm):
    """ contact trainer form """
    name = forms.CharField(max_length=50, required=True)
    phone= forms.CharField(max_length=20,  required=True)
    email = forms.EmailField(max_length=254,  required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "required":True}))

    class Meta:
        model = ContactTrainerRequest
        fields = ['name', 'phone', 'email', 'message']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'name':'Full Name',
            'phone': 'Contact phone number',
            'email':'Email',
            'message':'Enter you message'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 add_trainer-form-input'
            self.fields[field].label = False