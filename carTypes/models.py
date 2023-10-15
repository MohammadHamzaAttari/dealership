from django.db import models

# Create your models here.
class CarTypes(models.Model):
    type_name=models.CharField(max_length=200,blank=False)
    type_image=models.ImageField(upload_to='typeImages',blank=True)
    type_price=models.DecimalField(decimal_places=4,max_digits=15)
    
    def __str__(self):
        return self.type_name