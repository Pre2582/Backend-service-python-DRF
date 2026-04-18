from django.shortcuts import render
from django.http import JsonResponse
from firstapp.models import Employee

# Create your views here.

def employeeView(request):
    emp = {
        'id': 1,
        'name': 'John Doe',
        'age': 30,
        'department': 'IT',
        'salary': 50000
    }
    
    data = Employee.objects.all()
    response = {'employees': list(data.values('name', 'age', 'department', 'salary'))}
    return JsonResponse(response)