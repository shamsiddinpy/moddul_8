from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.serializers import UserSerializer, LoginSerializer
from root import settings
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Send email notification to user
            send_mail(
                'Site Registration',
                "Saytimizda ro'yxatdan o'tganingiz uchun tashakkur",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=True,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=HTTP_401_UNAUTHORIZED)
