from django.db import models
from companies.models import Companies
from carTypes.models import CarTypes
from carTrims.models import CarTrims
from django.contrib.auth.models import User
# Create your models here.
class CarModels(models.Model):
    
    model_name = models.CharField(max_length=200,
blank=False)
    date=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(decimal_places=4,max_digits=15)
    description = models.TextField(blank=True)
    model_poster=models.ForeignKey(User,on_delete=models.CASCADE)
    model_created=models.DateTimeField(auto_now_add=True)
    model_image = models.ImageField(
upload_to='modelImages',
blank=True,
default="modelImages/model.jpeg"
)
    car_company=models.ForeignKey(Companies,on_delete=models.CASCADE)
    car_type=models.ForeignKey(CarTypes,on_delete=models.CASCADE)
    car_trim=models.ForeignKey(CarTrims,on_delete=models.CASCADE)
    class Meta:
        ordering=['-model_created']

    def __str__(self):
        return "{}".format(self.model_name)

class Uploader(models.Model):
    uploaded_by=models.ForeignKey(User,on_delete=models.CASCADE)
    uploaded_content=models.ForeignKey(CarModels,on_delete=models.CASCADE)      