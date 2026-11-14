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

<<<<<<< HEAD
            'album': forms.Select(attrs={'class': 'form-select'}),

            'track_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Enter track number'}),

            'length_in_seconds':forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'e.g. 185'}),

            'credited_members': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter a short description of the song'}),
        }

        error_messages = {
            'title': {
                'required': 'Please enter a title for the song.',
                'max_length': 'The title is too long, please shorten it',
            },
            'track_number': {
                'required': 'Please enter a track number for the song.',
                'invalid':   'Please enter the track number as whole number. (e.g. 3)'
            },
            'length_in_seconds': {
                'required': 'Please enter a length in seconds for the song.',
                'invalid':  'Please enter a length in seconds as whole number. (e.g. 185)'
            },

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['album'].disabled = True
            self.fields['album'].help_text = (
                "The album can't be changed after creation."
            )

    def clean(self):
        cleaned_data = super().clean()

        album = cleaned_data.get('album')
        track_number = cleaned_data.get('track_number')

        if album and track_number:
            clashes = Song.objects.filter(album=album, track_number=track_number)

            if self.instance.pk:
                clashes = clashes.exclude(pk=self.instance.pk)

            if clashes.exists():
                self.add_error(
                    'track_number',
                    f'The track number {track_number} is already in use. '
                    'Please choose another track number.'
                )

        return cleaned_data


=======
            'album': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Position on the album title'}),

            'length_in_seconds':forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'e.g. 185'})
        }

>>>>>>> b0cfb207362c1492d339ac1f151bad5e5698fc87
