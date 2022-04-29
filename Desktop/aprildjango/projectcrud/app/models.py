from django.db import models

# Create your models here.
class Schoolbranch(models.Model):
    affid = models.IntegerField()
    branchname = models.CharField(max_length=50)
    email = models.EmailField(max_length = 20)

class ExamModel(models.Model):
    first_name = models.CharField(max_length =40)
    last_name =  models.CharField(max_length =40)
    father_name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    age = models.IntegerField()
    School_name = models.CharField(max_length=40)


class Eighth(models.Model):
    roll_no = models.IntegerField()
    division = models.CharField(max_length=50)

