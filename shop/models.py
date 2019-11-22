from django.db import models
from django.utils import timezone
from django.core.files.storage import default_storage as storage
from PIL import Image

# Create your models here.
"""Creating the Product model for the database"""
#The information will be added by the user in the form
class Product(models.Model):
    product_name = models.CharField(max_length=250, default="")
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='product_images')
    
    def __str__(self):
        return f'{self.product_name}'    

    #Resize the image as it's saved so it doesn't take too much space. If no image given then the 'user-default.jpg' image will be used for that user.
    def save(self):
        super(Product, self).save()
        if self.image:
            size = 500, 500
            product_image = Image.open(self.image)
            product_image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            product_image.save(fh)
            fh.close()