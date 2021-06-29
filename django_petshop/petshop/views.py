from petshop.models import Customer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Pet
from .serializers import CustomerSerializer, PetSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
