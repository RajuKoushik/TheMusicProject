from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Album

def index(request):

    all_albums = Album.objects.all()
    template = loader.get_template('TheMusicApp/index.html')

    #context has all the variables that are passed into teh context
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context,request))

def details(request, album_id):
    return HttpResponse("<h1>You are at the album "+ str(album_id)+ " .</h1>")
