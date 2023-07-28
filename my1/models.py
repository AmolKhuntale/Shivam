from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    experience = models.FloatField()
    salary = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self) :
        return self.first_name+" "+self.last_name
    

    