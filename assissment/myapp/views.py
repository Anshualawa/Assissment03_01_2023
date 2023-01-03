from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import *
from myapp.serializers import Productserializer


class Product(APIView):

    def get(self,request):
        product=productMainModel.objects.all()
        serializer=Productserializer(product,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass

    def patch(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass
