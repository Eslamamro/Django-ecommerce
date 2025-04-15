# products/models.py

from django.db import models

# Abstract base model for common product fields
class AbstractProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# Chair model
class Chair(AbstractProduct):
    material = models.CharField(max_length=100, default="Wood")

    def __str__(self):
        return f"Chair: {self.name}"

# Sofa model
class Sofa(AbstractProduct):
    seats = models.IntegerField(default=3)
    upholstery = models.CharField(max_length=100, default="Leather")

    def __str__(self):
        return f"Sofa: {self.name}"

# Dining Set model
class DiningSet(AbstractProduct):
    table_shape = models.CharField(max_length=50, choices=[("Round", "Round"), ("Rectangular", "Rectangular")])
