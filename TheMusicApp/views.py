from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

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
    template = loader.get_template('TheMusicApp/details.html')
    album = Album.objects.get(pk = album_id)
    context = {'album': album}
    return HttpResponse(template.render(context,request))


def favourites(request,album_id):
    return HttpResponse('Favorites bro')