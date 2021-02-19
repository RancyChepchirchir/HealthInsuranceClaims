from django.db import models
from datetime import datetime


# Create your models here.
# ! Inheritance

class Hospital_Type(models.Model):
    type_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    # ! converts the object into readable format (string)
    def __str__(self):
        return self.type_name


class Hospital(models.Model):
    objects = None
    hospital_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Hospital_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    address = models.TextField()
    updated_date = models.DateTimeField(default=datetime.now)
    logo = models.ImageField(upload_to='images/hospital/', blank=True, null=True)

    # ! table name = app name + django name
    # ! converts the object into readable format (string)
    def __str__(self):
        return self.name
