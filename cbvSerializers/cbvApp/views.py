from django.shortcuts import render
import django_filters
from cbvApp.models import Students
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class StudentPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    # pagination_class = StudentPagination
    pagination_class = LimitOffsetPagination
    
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'score']
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^name', '^id']  # ^ means starts with, $ means ends with, no symbol means contains
    
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'score']
    ordering = ['name']  # default ordering




"""
class StudentList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer   

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer    

class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)


# Create your views here.
class StudentList(APIView):
    
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
