from django.db import models
from django.utils import timezone

class World(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	totalcase = models.BigIntegerField(null=True)
	newcase = models.BigIntegerField(null=True)
	totaldeath = models.BigIntegerField(null=True)
	newdeath = models.BigIntegerField(null=True)
	date = models.DateField()

class Country(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	totalcase = models.BigIntegerField(null=True)
	newcase = models.BigIntegerField(null=True)
	totaldeath = models.BigIntegerField(null=True)
	newdeath = models.BigIntegerField(null=True)
	date = models.DateField()

class State(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	totalcase = models.BigIntegerField(null=True)
	newcase = models.BigIntegerField(null=True)
	totaldeath = models.BigIntegerField(null=True)
	newdeath = models.BigIntegerField(null=True)
	date = models.DateField()

class Area(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	totalcase = models.BigIntegerField(null=True)
	newcase = models.BigIntegerField(null=True)
	totaldeath = models.BigIntegerField(null=True)
	newdeath = models.BigIntegerField(null=True)
	date = models.DateField()

	
# class TotalCase(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	date = models.DateField(default=timezone.now)
# 	totalConfirm = models.BigIntegerField()
# 	place = models.ForeignKey(Area, on_delete=models.CASCADE)

# class NewCase(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	date = models.DateField(default=timezone.now)
# 	newCase = models.BigIntegerField()
# 	place= models.ForeignKey(Area, on_delete=models.CASCADE)

# class TotalDeath(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	date = models.DateField(default=timezone.now)
# 	totalDeath = models.BigIntegerField()
# 	place = models.ForeignKey(Area, on_delete=models.CASCADE)

# class NewDeath(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	date = models.DateField(default=timezone.now)
# 	newDeath = models.BigIntegerField()
# 	place = models.ForeignKey(Area, on_delete=models.CASCADE)


