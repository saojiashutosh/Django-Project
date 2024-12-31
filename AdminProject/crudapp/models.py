from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.CharField('Emp No.',max_length=10)
    ename = models.CharField('Emp Name',max_length=100)
    esal = models.FloatField('Emp Salary')
    ecity = models.CharField('Emp City',max_length=50)

