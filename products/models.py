from django.db import models

# Create your models here.
class Product(models.Model):

     image = models.CharField( max_length= 500, blank = True, help_text= 'Image link' )
     title = models.CharField( max_length= 200)
     description = models.TextField(blank = True)
     price = models.DecimalField(max_digits= 10, decimal_places= 2, blank = True, )
     ratings = models.DecimalField(max_digits=100, decimal_places=0, blank= True, default = 0)
