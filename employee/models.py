from django.db import models

# Create your models here.


class Department(models.Model):
    dept_id = models.IntegerField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=256)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
