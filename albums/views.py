from django.shortcuts import render

# Create your views here.

from albums.models import Album

def albums_list(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'albums/album_list.html', context)