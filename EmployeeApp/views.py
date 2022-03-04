from django.shortcuts import render
from django.views.decorators.csrf   import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from polls.models import Departments,Employee
from polls.serializers import DepartmentSerializer,EmployeeSerializer


# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        department=Departments.objects.all()
        department_serializer=DepartmentSerializer(department,many=True)
        return JsonResponse(department_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        if(department_serializer.is_valid()):
            department_serializer.save()
            return JsonResponse("Added succesfully",status=status.HTTP_200_OK,safe=False)
        return JSONParser("Failed",safe=False)
