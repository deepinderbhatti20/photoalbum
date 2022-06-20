from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    descr = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image =  CloudinaryField('image')

    def __str__(self):
        return self.descr
