from django.db import models

# Create your models here.
class CarTrims(models.Model):
    trim_name=models.CharField(max_length=200)
    trim_price=models.DecimalField(decimal_places=4,max_digits=15)
    trim_image=models.ImageField(upload_to='trimImages',blank=True)
    def __str__(self):
        return self.trim_name