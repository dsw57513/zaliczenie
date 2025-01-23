from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django.contrib.auth.models import User

class UserAuthForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "username",
            Field('password'),
            Submit('submit', 'Zatwierdź')
        )