from django.shortcuts import render
import json 
# Create your views here.
def home(request):
	with open('geo_data.json') as f:
		map_data = json.load(f)

	print(type(map_data))

	ctx = {
	'map_data':map_data
	}
	print(map_data,type(map_data))

	return render(request,"map.jinja", ctx)