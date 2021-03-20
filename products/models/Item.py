from django.db import models
from .Department import Department
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='img/', null=True, blank=True)
    #department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    visible = models.BooleanField(default=True)
    department = models.ManyToManyField(Department)