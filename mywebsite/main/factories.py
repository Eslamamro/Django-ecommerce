# products/factories.py

from .models import Chair, Sofa, DiningSet

class ProductFactory:
    @staticmethod
    def create_product(category, **kwargs):
        if category == "chair":
            return Chair.objects.create(**kwargs)
        elif category == "sofa":
            return Sofa.objects.create(**kwargs)
        elif category == "dining":
            return DiningSet.objects.create(**kwargs)
        else:
            raise ValueError("Unknown product category")
