from django.db import models


# Create your models here.
class rent(models.Model):
    rent_id = models.AutoField
    rent_person = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default="")
    sub_category = models.CharField(max_length=100,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=100)
    pub_date = models.DateField()
    image = models.ImageField(upload_to= "lend/images", default="")

    def __str__(self):
        return self.rent_person
