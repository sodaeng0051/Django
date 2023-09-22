from django import forms
from .models import Letter

class LetterWrite(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ('title', 'write', 'send', 'contents', 'complete')

class LetterSend():
    class Meta:
        model = Letter
        fields = ('title')