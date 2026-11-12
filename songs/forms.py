from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'track_number', 'length_in_seconds', 'credited_members', 'description']

        labels = {
            'track_number' : 'Track #',
            'length_in_seconds' : 'Length (seconds)',
            'credited_members' : 'Credited members',
        }

        help_texts = {
            'length_in_seconds' : 'Enter the full song length in seconds, e.g. 185 for 3:05.',
         }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the song title'}),

            'album': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Position on the album title'}),

            'length_in_seconds':forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'e.g. 185'})
        }

