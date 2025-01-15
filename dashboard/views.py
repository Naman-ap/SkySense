from django.shortcuts import render,HttpResponse
from dashboard.forms import CityForm
from dotenv import load_dotenv
import os
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")
import requests
# Create your views here.
def home(request):
    form=CityForm()
    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()
            city_name=form.cleaned_data.get('city_name')
            print(city_name)
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

            response=requests.get(url)
            json_response=response.json()
            weather_data={
                'temp': json_response['main']['temp'] ,
                'min':  json_response['main']['temp_min'],
                'max':  json_response['main']['temp_max'],
                'city': json_response['name'],
                'country': json_response['sys']['country'],
                'lat':  json_response['coord']['lat'],
                'lon': json_response['coord']['lon'],
                'weather': json_response['weather'][0]['main'],
                'presssure': json_response['main']['pressure'],
                'humidity': json_response['main']['humidity'],
                'windspeed':json_response['wind']['speed']
            }
    elif request.method=='GET':
        weather_data=None

    context={'form':form,'weather_data':weather_data}
    return render(request,"home.html",context=context)