from django.db import models

# Create your models here.

class Apache(models.model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	visit = models.IntegerField()

