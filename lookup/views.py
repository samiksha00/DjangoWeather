from django.shortcuts import render

def index(request):
	import json
	import requests

	if request.method=="POST":
		zipcode=request.POST['zipcode']
		api_url=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=25&API_KEY=4D008F4C-87EA-4080-BD6B-4A54E80FA809")
		try:
			api=json.loads(api_url.content)
		except Exception as e:
			api="Error..."
		return render(request, 'index.html',{'api':api,'zipcode':zipcode})

	else:
		api_url=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=4D008F4C-87EA-4080-BD6B-4A54E80FA809")
		try:
			api=json.loads(api_url.content)
		except Exception as e:
			api="Error..."
		return render(request, 'index.html',{'api':api})

def about(request):
	return render(request, 'about.html',{})