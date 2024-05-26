from django import forms
from .models import MovieReview

class NameForm(forms.Form):
    your_name = forms.CharField(label="Nombre:", max_length=100, help_text="100 Char Max", 
                                error_messages={"required": "El nombre es requerido"},
                                widget=forms.Textarea(attrs={"class":"text-gray-400", "rows": 3, "cols": 60}))

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 100, 'required': True}),
            'review': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

