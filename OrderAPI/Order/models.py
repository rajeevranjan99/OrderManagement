from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500)
    product_images = models.ManyToManyField('ProductImage', related_name="products")


    def __str__(self):
        return self.name 

class ProductImage(models.Model):

    image = models.ImageField(upload_to='product_images/')



    def __str__(self):
        return str(self.image.name)
