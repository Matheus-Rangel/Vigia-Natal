from django.shortcuts import render
from django.http import HttpResponse
from home_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    my_dict = {'insert_me' : "Hello im from home_app"}
    return render(request, 'home_app/index.html', context = my_dict)
