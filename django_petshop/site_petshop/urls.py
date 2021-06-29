from django.contrib import admin
from django.urls import path, include
from petshop.views import CustomerViewSet, PetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"clientes", CustomerViewSet)
router.register(r"pets", PetViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
