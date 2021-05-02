from django import forms
from .models import World, Country, State, Area

world_choice = []
country_choice = []
state_choice = []
area_choice = []

for world in World.objects.all():
	world_choice.append((f"{world.name}",f"{world.name}"))
for country in Country.objects.all():
	country_choice.append((f"{country.name}",f"{country.name}"))
for state in State.objects.all():
	state_choice.append((f"{state.name}",f"{state.name}"))
for area in Area.objects.all():
	area_choice.append((f"{area.name}",f"{area.name}"))

class LocationForm(forms.Form):
	world = forms.CharField(label='Select World', widget=forms.Select(choices=world_choice))
	country = forms.CharField(label='Select Country', widget=forms.Select(choices=country_choice))
	state = forms.CharField(label='Select State', widget=forms.Select(choices=state_choice))
	area = forms.CharField(label='Select Area', widget=forms.Select(choices=area_choice))


