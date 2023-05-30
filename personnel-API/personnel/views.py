from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonnelSerializer,DepartmentPersonnelSerializer
from .models import Department, Personnel
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView


class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonnelListCreateView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class PersonnelRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer


class DepartmentPersonnelView(ListAPIView):
    queryset = Personnel.objects.all()
    serializer_class = DepartmentPersonnelSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        
        department = self.kwargs('department')
        if department is not None:
           return Department.objects.filter(name__iexact=department)
