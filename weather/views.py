from django.shortcuts import render, redirect
from .forms import city
import requests
# Create your views here.
def  weather(request):
    if request.method == 'POST':
        form = city(request.POST)
        if form.is_valid():
            form.save()
            para = {
                'q' : 'kanpur',
                'units' : 'imperial',
                'appid' : '2f5d9378ea5e70a2d2d2171dadaef432'
            }
            para['q']=form.cleaned_data['city']
            url = 'http://api.openweathermap.org/data/2.5/weather'
            r = requests.get(url,params = para)
            print(r.text)
            return redirect('weather')
    else:
        form = city()
    return render(request, 'weather/weather.html', {'form' : city})

