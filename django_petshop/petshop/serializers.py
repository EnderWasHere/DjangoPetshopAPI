from rest_framework import serializers

from .models import Customer, Pet


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "document",
            "address",
            "complement",
            "phone1",
            "phone2",
            "created",
            "updated",
        ]


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "customer",
            "size",
            "born_date",
            "agressive",
            "plague",
            "comments",
            "created",
            "updated",
        ]
