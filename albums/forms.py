from django import forms
from .models import Album
from .validators import (
    validate_cover_url_is_image,
    validate_release_date_not_in_future,
    validate_title_length,
)


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_date', 'album_type', 'cover_url', 'description']

        labels = {
            'title': 'Album title',
            'release_date': 'Release date',
            'album_type': 'Album type',
            'cover_url': 'Cover image URL',
            'description': 'Description',
        }

        help_texts = {
            'title': 'Enter the official album title.',
            'release_date': 'The release date cannot be in the future.',
            'album_type': 'Choose the type of release.',
            'cover_url': 'Must start with http:// or https://',
            'description': 'A short summary of the album.',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Album Title',
            }),
            'release_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date', 'class': 'form-control'},
            ),
            'album_type': forms.Select(attrs={'class': 'form-select'}),
            'cover_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/cover.jpg',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write something about this album...',
                'rows': 4,
            }),
        }

        error_messages = {
            'title': {
                'required': 'Please enter the album title.',
                'max_length': 'The album title is too long.',
            },
            'release_date': {
                'required': 'Please enter the release date.',
                'invalid': 'Enter a valid date (YYYY-MM-DD).',
            },
            'cover_url': {
                'required': 'Please provide a cover image URL.',
                'invalid': 'Enter a valid URL, e.g. https://example.com/cover.jpg',
                'max_length': 'The cover URL is too long.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].validators.append(validate_title_length)
        self.fields['release_date'].validators.append(validate_release_date_not_in_future)
        self.fields['cover_url'].validators.append(validate_cover_url_is_image)

    def clean_title(self):
        return self.cleaned_data['title'].strip()