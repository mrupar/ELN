"""
URL configuration for FAMNIT_ELN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from .home import home
from samples.autocomplete import SpeciesAutocomplete, ProjectAutocomplete, SampleProviderAutocomplete, \
    CountryAutocomplete

urlpatterns = [
    path("", home, name='home'),
    path('admin/', admin.site.urls),
    path("samples/", include("samples.urls")),
    path("users/", include("users.urls")),
    path("forum/", include("forum.urls")),
    # Autocomplete
    re_path(r'^species-autocomplete/$', SpeciesAutocomplete.as_view(), name='species-autocomplete'),
    re_path(r'^project-autocomplete/$', ProjectAutocomplete.as_view(), name='project-autocomplete'),
    re_path(r'^sample-provider-autocomplete/$', SampleProviderAutocomplete.as_view(), name='sample-provider-autocomplete'),
    re_path(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete'),
]
