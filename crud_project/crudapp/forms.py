from django import forms
from .models import Card


class CardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Card
        fields = [
            'title',
            'description'
        ]
