from django.shortcuts import render
from events.views import public_event_list

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
