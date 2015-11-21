from django.db import models

# Create your models here.

class Apache(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	visit = models.IntegerField()

	def __str__(self):
		return "%s" % self.visit

