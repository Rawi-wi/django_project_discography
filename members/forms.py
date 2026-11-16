from django import forms
from members.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'stage_name',
            'birth_name',
            'birthday',
            'position',
            'image_url',
            'bio',
        ]

        labels = {
            'stage_name': 'Stage Name',
            'birth_name': 'Birth Name',
            'birthday': 'Birthday',
            'position': 'Position',
            'image_url': 'Image URL',
            'bio': 'Biography',
        }

        help_texts = {
            'stage_name': 'The name the member performs under.',
            'birth_name': "The member's full legal name.",
            'birthday': 'Cannot be a date in the future.',
            'position': 'For example: Leader, Main Rapper, Vocalist.',
            'image_url': 'Link to a profile photo of the member.',
            'bio': 'A short description of the member (optional).',
        }

        widgets = {
            'stage_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Bang Chan',
            }),
            'birth_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Christopher Bang',
            }),
            'birthday': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
            ),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Leader, Producer',
            }),
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/member.jpg',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about this member...',
                'rows': 4,
            }),
        }

        error_messages = {
            'stage_name': {
                'required': 'Please enter the stage name.',
                'max_length': 'The stage name is too long.',
                'unique': 'A member with this stage name already exists.',
            },
            'birth_name': {
                'required': 'Please enter the birth name.',
                'max_length': 'The birth name is too long.',
            },
            'birthday': {
                'required': 'Please enter the birthday.',
                'invalid': 'Enter a valid date.',
            },
            'position': {
                'max_length': 'The position is too long.',
            },
            'image_url': {
                'invalid': 'Enter a valid image URL.',
            },
        }
