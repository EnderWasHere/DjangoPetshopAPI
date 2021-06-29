# from typing_extensions import Required
from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ #algo ligado com internacionalização do erro (importante para mensagem de erros de validação)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100)
    complement = models.CharField(max_length=100, null=True, blank=True)
    phone1 = PhoneNumberField()
    phone2 = PhoneNumberField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def clean(self):

    # VALIDAÇÃO CAMPO "DOCUMENT" (CPF) 
        if self.document.isdigit() == False: # Vefica possui caracteres alem de numeros
            raise ValidationError(_('O CPF deve conter apenas dígitos'))
        if len(self.document) != 11: #verifica se o CPF tem 11 digitos
            raise ValidationError(_('O CPF precisa conter 11 digitos'))
        if len(set(self.document)) == 1: #verifica se possui apenas 1 digito repetidamente
            raise ValidationError(_('O CPF possui muitos números repetidos'))

class Pet(models.Model):
    # auto explicativo
    SIZE_CHOICES = (
        ("PUPPY", "Filhote"),
        ("SMALL", "Pequeno"),
        ("MEDIUM", "Médio"),
        ("LARGE", "Grande"),
        ("GIANT", "Gigante"),
    )

    name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # campo de escolhas
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, blank=False, null=False)
    born_date = models.DateField()
    agressive = models.BooleanField()
    plague = models.BooleanField()
    comments = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class Agendamento(models.Model):
#     date = models.DateTimeField()
#     work = models.CharField(max_length=50)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)