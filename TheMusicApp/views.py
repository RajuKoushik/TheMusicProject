from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Album

def index(request):

    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id)
        html = html + '<a href="' + str(url)+'">' + str(album.album_title)+ '</a> <br>'
    return HttpResponse(html)

def details(request, album_id):
    return HttpResponse("<h1>You are at the album "+ str(album_id)+ " .</h1>")
