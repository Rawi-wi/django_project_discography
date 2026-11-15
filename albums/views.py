from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm

# Create your views here.

from albums.models import Album

def albums_list(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'albums/album_list.html', context)

def albums_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = {'album': album}
    return render(request, 'albums/album_detail.html', context)

def albums_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('albums:detail', pk=album.pk)
    else:
        form = AlbumForm()

    context = {'form': form}
    return render(request, 'albums/album_form.html', context)

def albums_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('albums:detail', pk=album.pk)

    else:
        form = AlbumForm(instance=album)

    context = {'form': form}
    return render(request, 'albums/album_form.html', context)

def albums_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        album.delete()
        return redirect('albums:list')

    context = {'album': album}
    return render(request, 'albums/album_confirm_delete.html', context)
