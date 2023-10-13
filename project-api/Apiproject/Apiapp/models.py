from django.db import models

# Create your models here.

class UserTask(models.Model):
    task_title=models.CharField(max_length=1000)
    task_desc=models.CharField(max_length=10000)
    task_date=models.DateField()


class User(models.Model):
    task_title=models.CharField(max_length=1000)
    task_desc=models.CharField(max_length=10000)
    
