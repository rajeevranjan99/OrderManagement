from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    desciption = models.CharField(max_length=500)

    def __str__(self):
        return self.name 

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="image" ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
