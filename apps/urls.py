from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.views import RegisterAPIView, CategoryListCreateAPIView, ProductListCreateAPIView, LoginView

#
# router = DefaultRouter()
# router.register(r'register', RegisterAPIView, basename='register')
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginView.as_view()),
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('products/', ProductListCreateAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view())
]
