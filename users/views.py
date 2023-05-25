from django.shortcuts import render
from users.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import *
from users.utils import generate_token, update_token ,login_update
from django.contrib.auth.hashers import check_password 
from rest_framework.permissions import IsAuthenticated
from users.custom_auth import CustomAuthenticationBackend
from datetime import datetime

# Create your views here.

class userlogin(APIView):
    serializer_class = UserSerializer 
    def post(self,request):
        data=request.data
        try:
            employee = Employees.objects.get(email=data["email"])
        except:
            return Response({"message":"No user found"},status=400)   
        password = employee.password
        if check_password(data["password"],password,preferred="unsalted_md5"):
            api_token = generate_token()
            update_token(self,employee.id,api_token)
            login = login_update(self,employee.id)    
            return Response({"message":"Login Success","token":api_token},status=200)
        else:
            return Response({"message":"Login Failed,Incorrect Password"},status=400)  

class userlogout(APIView):
    authentication_classes = [CustomAuthenticationBackend]

    def post(self,request):
        data=request.data
        login = TblEmployeeLogin.objects.filter(employee_id=data["employee_id"]).latest('login_time')
        try:
            login_id = TblEmployeeLogin.objects.get(id=login.pk)
            login_id.logout_time = datetime.now()
            login_id.save()
        except TblEmployeeLogin.DoesNotExist:
        # Handle the case where no matching login record is found
            pass
        return Response({"message":"Logout Successful"},status=200)         
        
class shoplist(APIView):
    serializer_class = ShopSerializer
    authentication_classes = [CustomAuthenticationBackend]

    def post(self,request):
        data =request.data
        data["created_at"] = datetime.now().isoformat()
        data["updated_at"] = datetime.now().isoformat()
        serializer = ShopSerializer(data=data,context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"Message":"Shop added","data":serializer.data},status=200)
    
    def get(self,request):
        obj = TblShop.objects.all().values()
        return Response(obj,status=200)
    

class shopvisit(APIView):
    authentication_classes = [CustomAuthenticationBackend]
    serializer_class = ShopVisitSerializer

    def post(self,request):
        data=request.data
        data["created_at"] = datetime.now().isoformat()
        data["updated_at"] = datetime.now().isoformat()
        data["visit_date"] = datetime.today()
        serializer = ShopVisitSerializer(data=data,context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"Message":"Updated","data":serializer.data},status=200)
           
