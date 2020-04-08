from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'focus', 'like', 'video_id']

class SearchForm(forms.Form):
    search_term = forms.CharField()