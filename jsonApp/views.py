from rest_framework import generics
from .models import Student, Tenhim
from .serializers import StudentSerializer, TenhimSerializer

class StudentGetCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TenhimGetCreate(generics.ListCreateAPIView):
    queryset = Tenhim.objects.all()
    serializer_class = TenhimSerializer