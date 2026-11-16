from rest_framework import serializers
from .models import Student, Tenhim

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TenhimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenhim
        fields = '__all__' 