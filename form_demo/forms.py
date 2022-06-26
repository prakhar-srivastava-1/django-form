from logging import PlaceHolder
from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=200,
        min_length=4,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control-mb-3',
                'id': 'name-input'
            }
        )
    )
    
    email = forms.CharField(
        label="Email",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control-mb-3',
                'id': 'email-input'
            }
        )
    )

    review = forms.CharField(
        label="Review",
        min_length=4,
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5',
            }
        )
    )