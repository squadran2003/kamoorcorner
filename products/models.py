from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255,blank = False)
    description = models.CharField(max_length = 255,blank= False)
    Cost = models.DecimalField(max_digits = 20,decimal_places = 2,default = 750)
    created_on = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title
