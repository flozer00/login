from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=25, blank=False)
    mail = models.CharField(max_length=35, blank=False)
    password = models.CharField(max_length=25, blank=False)
    rep_password = models.CharField(max_length=25, blank=False)
