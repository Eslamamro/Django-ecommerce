from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .factories import ProductFactory
from .models import Chair, Sofa, DiningSet
from .serializers import ChairSerializer, SofaSerializer, DiningSetSerializer

class FeaturedProductsAPIView(APIView):
    def get(self, request):
        chairs = Chair.objects.filter(is_featured=True)
        sofas = Sofa.objects.filter(is_featured=True)
        dining = DiningSet.objects.filter(is_featured=True)

        data = (
            ChairSerializer(chairs, many=True).data +
            SofaSerializer(sofas, many=True).data +
            DiningSetSerializer(dining, many=True).data
        )
        return Response(data)

class LatestProductsAPIView(APIView):
    def get(self, request):
        chairs = Chair.objects.order_by('-created_at')[:4]
        sofas = Sofa.objects.order_by('-created_at')[:4]
        dining = DiningSet.objects.order_by('-created_at')[:4]

        data = (
            ChairSerializer(chairs, many=True).data +
            SofaSerializer(sofas, many=True).data +
            DiningSetSerializer(dining, many=True).data
        )
        return Response(data)

class ProductCreateAPIView(APIView):
    def post(self, request):
        category = request.data.get("category")
        try:
            product = ProductFactory.create_product(category, **request.data)
            return Response({"id": product.id}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)
