from django import forms
from .models import World, Country, State, Area
from .data.Data import Data

# data = Data()
# globaldata, countrydata, statedata, areadata = data.oneClickchoice()

# world_choice = []
# country_choice = []
# state_choice = []
# area_choice = []

# for world in globaldata:
# 	world_choice.append((f"{world['displayName']}",f"{world['displayName']}"))
# for country in countrydata:
# 	country_choice.append((f"{country['displayName']}",f"{country['displayName']}"))
# for state in statedata:
# 	state_choice.append((f"{state['displayName']}",f"{state['displayName']}"))
# for area in areadata:
# 	area_choice.append((f"{area['displayName']}",f"{area['displayName']}"))

# class LocationForm(forms.Form):
# 	world = forms.CharField(label='Select World', widget=forms.Select(choices=world_choice))
# 	country = forms.CharField(label='Select Country', widget=forms.Select(choices=country_choice))
# 	state = forms.CharField(label='Select State', widget=forms.Select(choices=state_choice))
# 	area = forms.CharField(label='Select Area', widget=forms.Select(choices=area_choice))


