from django.urls import path
from .views import index, location, getWorld, getCountry, getState, getArea
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('location/', location, name='location'),
    path('world_json/', getWorld, name='world'),
	path('country_json/<str:world>/', getCountry, name='country'),
	path('state_json/<str:country>/', getState, name='state'),
	path('area_json/<str:state>/', getArea, name='area'),






] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)