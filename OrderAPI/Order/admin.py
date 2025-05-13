from django.contrib import admin
from django.utils.html import format_html

from .models import Product , ProductImage

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description','display_images',)

    def display_images(self, obj):
        images = obj.product_images.all()
        if images:
            return format_html("".join(
                [f'<img src="{img.image.url}" width="50" height="50" style="margin:2px;"/>' for img in images]
            ))
        return "No images"

    display_images.short_description = 'Product Images'
    
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage) 
