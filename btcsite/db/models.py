from django.db import models

# Create your models here.
class buyer(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	Data = models.CharField(max_length=30)
