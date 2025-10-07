from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['MovieTitle','Actor1Name','Actor2Name','DirectorName','MovieGenre','ReleaseYear']
        widgets = {
            'MovieTitle': forms.TextInput(attrs={'class':'form-control'}),
            'Actor1Name': forms.TextInput(attrs={'class':'form-control'}),
            'Actor2Name': forms.TextInput(attrs={'class':'form-control'}),
            'DirectorName': forms.TextInput(attrs={'class':'form-control'}),
            'MovieGenre': forms.Select(attrs={'class':'form-select'}),
            'ReleaseYear': forms.NumberInput(attrs={'class':'form-control','min':1900,'max':2100}),
        }
