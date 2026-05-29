from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=0)

    image = models.ImageField(upload_to='products/')

    tagline = models.CharField(max_length=255)

    description = models.TextField()

    material = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name