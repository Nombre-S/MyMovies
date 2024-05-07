from typing import Required
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Nombre:", max_length=100, help_text="100 Char Max", 
                                error_messages={"required": "El nombre es requerido"},
                                widget=forms.Textarea(attrs={"class":"text-gray-400", "rows": 3, "cols": 60}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

