from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm
from albums.models import Album

ALBUM_SORT_OPTIONS = {
    'newest': '-release_date',
    'oldest': 'release_date',
    'title': 'title',
}


def albums_list(request):
    sort = request.GET.get('sort')
    albums = Album.objects.all()

    order_field = ALBUM_SORT_OPTIONS.get(sort)
    if order_field:
        albums = albums.order_by(order_field)

    context = {'albums': albums, 'current_sort': sort}
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
