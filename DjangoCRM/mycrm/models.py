from django.db import models

# Create your models here.

class Record(models.Model):
    created_at=models.DateTimeField(auto_now=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)


