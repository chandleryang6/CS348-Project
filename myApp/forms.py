from django import forms
from .models import Artist, AddConcert

#ArtistForm: A Django ModelForm that creates a form for the Artist model with 'name' and 'description' fields.
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'description']

#ConcertForm: A Django ModelForm for the 'AddConcert' model, including fields for 'date', 'time', 'artist', and 'venue'.
class ConcertForm(forms.ModelForm):
    class Meta:
        model = AddConcert
        fields = ['date', 'time', 'artist', 'venue']