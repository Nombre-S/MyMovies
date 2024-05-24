from typing import Required
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Nombre:", max_length=100, help_text="100 Char Max", 
                                error_messages={"required": "El nombre es requerido"},
                                widget=forms.Textarea(attrs={"class":"text-gray-400", "rows": 3, "cols": 60}))

class MovieReviewForm(forms.Form):
    movie_id = forms.IntegerField(widget=forms.HiddenInput())
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
