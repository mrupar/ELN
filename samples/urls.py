from django.urls import path
from . import views

urlpatterns = [
    path("", views.samples, name="samples"),
    path("add_sample/", views.add_sample, name="add_sample"),
    path("species/", views.species, name="species"),
    path("add_species/", views.add_species, name="add_species"),
]