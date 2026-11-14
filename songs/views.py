<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404

from songs.forms import SongForm
from songs.models import Song

# Create your views here.

def songs_list(request):
    songs = Song.objects.select_related('album').order_by('album','track_number')
    context = {'songs': songs}
    return render(request, 'songs/song_list.html', context )

def songs_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    context = {'song': song}
    return render(request, 'songs/song_detail.html', context)

def songs_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('songs:detail', pk=song.pk)
    else:
        form = SongForm()

    context = {'form': form}
    return render(request, 'songs/song_form.html', context)

def songs_edit(request, pk):
    song = get_object_or_404(Song, pk=pk)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('songs:detail', pk=song.pk)

    else:
        form = SongForm(instance=song)

    context = {'form': form}
    return render(request, 'songs/song_form.html', context )

def songs_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)

    if request.method == 'POST':
        song.delete()
        return redirect('songs:list')

    context = {'song': song}
    return render(request, 'songs/song_confirm_delete.html', context )
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> b0cfb207362c1492d339ac1f151bad5e5698fc87
