from django.urls import path
from .views import FeaturedProductsAPIView, LatestProductsAPIView, ProductCreateAPIView

urlpatterns = [
    path('featured/', FeaturedProductsAPIView.as_view()),
    path('latest/', LatestProductsAPIView.as_view()),
    path('create/', ProductCreateAPIView.as_view()),
]
