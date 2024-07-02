from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SchoolSerializer,studentSerailizer
from .models import school,student
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class SchoolView(APIView):
    def get(self, request):
        queryset = school.objects.all()  # Example queryset, replace with your actual queryset logic
        serializer = SchoolSerializer(queryset, many=True)  # Use many=True if queryset has multiple items
        return Response(serializer.data)

    def post(self,request):
        serializer=SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)
    def put(self,request):
        serializer=SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

class StudentView(APIView):
    def get(self, request):
        queryset = student.objects.all()  # Example queryset, replace with your actual queryset logic
        serializer = studentSerailizer(queryset, many=True)  # Use many=True if queryset has multiple items
        return Response(serializer.data)

    def post(self,request):
        serializer=studentSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)
    def put(self,request):
        serializer=SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)