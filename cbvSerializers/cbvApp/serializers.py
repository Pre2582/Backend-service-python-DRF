from rest_framework import serializers
from cbvApp.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'age', 'department', 'score']
