from django.urls import path
from .views import index, locationSelection

urlpatterns = [
    path('', index, name='index'),
    path('location/', locationSelection, name='location'),
]