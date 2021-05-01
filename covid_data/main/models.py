from django.db import models
from django.utils import timezone

class Country(models.Model):
	id = models.AutoField(primary_key=True)
	country = models.CharField(max_length=100)
	def __str__(self):
		return self.country

class Area(models.Model):
	id = models.AutoField(primary_key=True)
	area = models.CharField(max_length=100)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	def __str__(self):
		return self.area

class TotalCase(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(default=timezone.now)
	totalConfirm = models.BigIntegerField()
	place = models.ForeignKey(Area, on_delete=models.CASCADE)

class NewCase(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(default=timezone.now)
	newCase = models.BigIntegerField()
	place= models.ForeignKey(Area, on_delete=models.CASCADE)

class TotalDeath(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(default=timezone.now)
	totalDeath = models.BigIntegerField()
	place = models.ForeignKey(Area, on_delete=models.CASCADE)

class NewDeath(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateField(default=timezone.now)
	newDeath = models.BigIntegerField()
	place = models.ForeignKey(Area, on_delete=models.CASCADE)


