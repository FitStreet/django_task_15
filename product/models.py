from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField('Address', on_delete = models.CASCADE, related_name = 'company')

class Worker(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name = 'workers')
    projects = models.ManyToManyField('Project', related_name= 'workers', related_query_name='worker')

class Project(models.Model):
    title = models.CharField(max_length=200)

class Address(models.Model):
    city = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)




