from django.db import models

class Books(models.Model):
    boo_name =models.CharField(max_length=255)
    boo_author =models.CharField(max_length=255)
    boo_type =models.CharField(max_length=255)
    boo_year =models.CharField(max_length=255)
    boo_image =models.ImageField(upload_to='books')

