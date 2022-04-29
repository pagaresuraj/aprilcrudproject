from django.db import models

# Create your models here.
class Student(models.Model) :
    stuid = models.IntegerField()
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length =30)



