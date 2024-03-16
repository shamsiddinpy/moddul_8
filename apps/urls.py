from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.views import RegisterAPIView, CategoryListCreateAPIView, ProductListCreateAPIView

#
# router = DefaultRouter()
# router.register(r'register', RegisterAPIView, basename='register')
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category'),
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view())
]
