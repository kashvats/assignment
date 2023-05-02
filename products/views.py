from django.shortcuts import render
from rest_framework.views import APIView
from .models import product,User
from .serializer import RegisterSerializer,ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class ProductAPI(APIView):
    "Here we will perfom crud operations on products that Admin has created"
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        queryset = product.objects.filter(owner=request.user)
        if request.query_params.get("search"):
            queryset = queryset.filter(item_name=request.query_params.get("search"))
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        if request.user.roles == "SE":
            data = request.data
            serializer = ProductSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(owner=request.user)
            return Response({"msg":"Product Added successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"msg":"Customer can't add product"},status=status.HTTP_200_OK)

    def put(self,request,id):
        if request.user.roles == "SE":
            queryset = product.objects.get(id=id,owner=request.user)
            serializer = ProductSerializer(queryset,data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(owner=request.user)
            return Response({"msg":"Product Updated successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"msg":"Customer can't update product"},status=status.HTTP_200_OK)

    def delete(self,request,id):
        queryset = product.objects.get(id=id,owner=request.user)
        if queryset:
            if request.query_params.get("delete") == "0":
                queryset.delete()
            else:
                queryset.deleted = True
                queryset.save()
            return Response({"message":"Product Deleted successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"product does not Exist"},status=status.HTTP_200_OK)
        
class productAPIView(APIView):
    
    def get(self,request):
        queryset = product.objects.all()
        if request.query_params.get("search"):
            queryset = queryset.filter(item_name=request.query_params.get("search"))
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)    

class RegisterAPI(APIView):
    
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'message': 'user created',
                    'user': serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'errors': serializers.errors}, statuc=status.HTTP_400_BAD_REQUEST)

        except:
            print(traceback.print_exc())
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
