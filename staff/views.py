from django.shortcuts import render
from staff.models import staff
from staff.serializers import StaffSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

class liststaffApiView(ListAPIView):
    queryset = staff.objects.all()
    serializer_class = StaffSerializer

class createstaffApiView(CreateAPIView):
    queryset = staff.objects.all()
    serializer_class = StaffSerializer

class deletestaffApiView(DestroyAPIView):
    queryset = staff.objects.all()
    serializer_class = StaffSerializer

class updatestaffApiView(UpdateAPIView):
    queryset = staff.objects.all()
    serializer_class = StaffSerializer

