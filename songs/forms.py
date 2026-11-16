from django import forms
from .models import Song
from albums.models import Album
from members.models import Member
from .validators import validate_search_length

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'track_number', 'length_in_seconds', 'credited_members', 'description']

        labels = {
            'track_number': 'Track #',
            'length_in_seconds': 'Length (seconds)',
            'credited_members': 'Credited members',
        }

        help_texts = {
            'album': 'Optional: leave empty for songs that are not part of an album.',
            'length_in_seconds': 'Enter the full song length in seconds, e.g. 185 for 3:05.',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the song title'}),
            'album': forms.Select(attrs={'class': 'form-select'}),
            'track_number': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Enter track number'}),
            'length_in_seconds': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 1, 'placeholder': 'e.g. 185'}),
            'credited_members': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter a short description of the song'}),
        }

        error_messages = {
            'title': {
                'required': 'Please enter a title for the song.',
                'max_length': 'The title is too long, please shorten it.',
            },
            'track_number': {
                'required': 'Please enter a track number for the song.',
                'invalid': 'Please enter the track number as a whole number. (e.g. 3)',
            },
            'length_in_seconds': {
                'required': 'Please enter a length in seconds for the song.',
                'invalid': 'Please enter the length in seconds as a whole number. (e.g. 185)',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['album'].required = False
        self.fields['album'].empty_label = 'No album'

        if self.instance.pk:
            self.fields['album'].disabled = True
            self.fields['album'].help_text = "The album can't be changed after creation."

    def clean(self):
        cleaned_data = super().clean()

        album = cleaned_data.get('album')
        track_number = cleaned_data.get('track_number')

        if album is None or track_number is None:
            return cleaned_data

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


class SongFilterForm(forms.Form):
    SORT_CHOICES = [
        ('', 'Default order'),
        ('title', 'Title (A-Z)'),
        ('-title', 'Title (Z-A)'),
        ('track_number', 'Track number (low to high)'),
        ('-track_number', 'Track number (high to low)'),
        ('length_in_seconds', 'Length (shortest first)'),
        ('-length_in_seconds', 'Length (longest first)'),
    ]

    search = forms.CharField(
        required=False,
        max_length=100,
        label='Search',
        validators=[validate_search_length],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by song title....'}),
        error_messages={
            'max_length': 'The search text is too long, please use at most 100 characters.',
        },
    )

    album = forms.ModelChoiceField(
        queryset=Album.objects.all(),
        required=False,
        empty_label='All albums',
        label='Album',
        widget=forms.Select(attrs={'class': 'form-select'}),
        error_messages={
            'invalid_choice': 'Please choose an album from the list.',
        },
    )

    members = forms.ModelChoiceField(
        queryset=Member.objects.all(),
        required=False,
        empty_label='All members',
        label='Members',
        widget=forms.Select(attrs={'class': 'form-select'}),
        error_messages={
            'invalid_choice': 'Please choose a member from the list.',
        },
    )

    sort = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        label='Sort by',
        widget=forms.Select(attrs={'class': 'form-select'}),
        error_messages={
            'invalid_choice': 'Please choose a sorting option from the list.',
        },
    )
