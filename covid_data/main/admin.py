from django.contrib import admin
from .models import Country, Area, TotalCase, NewCase, TotalDeath, NewDeath

admin.site.register(Country)
admin.site.register(Area)
admin.site.register(TotalCase)
admin.site.register(NewCase)
admin.site.register(TotalDeath)
admin.site.register(NewDeath)