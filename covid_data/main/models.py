from django.db import models
from django.utils import timezone

class Data(models.Model):
	id = models.AutoField(primary_key=True)
	name_id = models.CharField(max_length=100)
	totalcase = models.BigIntegerField(null=True)
	newcase = models.BigIntegerField(null=True)
	totaldeath = models.BigIntegerField(null=True)
	newdeath = models.BigIntegerField(null=True)
	date = models.DateField()

	def __str__(self):
		return f"{self.name_id}---{self.date}"

class Location(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	name_id = models.CharField(max_length=100)
	parent_id = models.CharField(max_length=100, null=True)
	location_type = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name}---{self.location_type}"


