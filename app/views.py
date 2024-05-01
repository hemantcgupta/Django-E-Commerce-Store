from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.authPermission import IsAuthenticatedJWT
from django.shortcuts import Http404
from django.contrib.auth.hashers import check_password
import jwt
import datetime
from .serializers import RegisterSerializer, LoginSerializer, ProductSerializer, ProductDetailSerializer, CategorySerializer
from .models import UserProfile, Product, Category

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        response = Response()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = UserProfile.fetch_user_by_email(username)
            if user is not None:
                if check_password(password, user.password):
                    payload = {
                        'user_id': user.id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                        'iat': datetime.datetime.utcnow()
                    }
                    token = jwt.encode(payload, 'HeMaNt', algorithm='HS256')
                    response.set_cookie(key='jwt', value=token, httponly=True)
                    response.data = {'jwt': token}
                else:
                    response.data = {'error': 'Incorrect password!'}
            else:
                response.data = {'error': 'User not found'}
        else:
            response.data = serializer.errors
        return response     
     

# class ProductView(APIView):
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedJWT]

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = self.serializer_class(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk):
#         product = self.get_object(pk)
#         serializer = self.serializer_class(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = self.get_object(pk)
#         serializer = self.serializer_class(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
class ProductView(APIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedJWT]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticatedJWT]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = self.serializer_class(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryView(APIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedJWT]
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedJWT]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = self.serializer_class(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        