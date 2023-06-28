from django.db import models
from django import forms


class Users(models.Model):
    email = forms.EmailField(
        label=('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    username = models.CharField(max_length=28, blank=False)
    password = models.CharField(max_length=28, blank=False)
