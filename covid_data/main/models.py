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
	data = models.ForeignKey(Data, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name}---{self.location_type}"	

# class Country(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=100)
# 	location_type = models.CharField(max_length=100)
# 	data = models.ForeignKey(Data, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return f"{self.name}"

# class State(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=100)
# 	location_type = models.CharField(max_length=100)
# 	data = models.ForeignKey(Data, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return f"{self.name}"

# class Area(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=100)
# 	location_type = models.CharField(max_length=100)
# 	data = models.ForeignKey(Data, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return f"{self.name}"
	
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


