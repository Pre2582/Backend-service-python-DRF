from rest_framework import serializers
from fbvApp.models import Students, passanger

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'age', 'department', 'score']

class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = passanger
        fields = ['id', 'name', 'age', 'gender', 'travel_points']        