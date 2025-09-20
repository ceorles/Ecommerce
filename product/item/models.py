from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    stockOption = [
        (True, 'Available'),
        (False, 'Not available'),
    ]

    stock = models.BooleanField(choices=stockOption, default=False, null=True)
    image_url = models.URLField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
