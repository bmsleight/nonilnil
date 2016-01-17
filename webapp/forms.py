from django import forms

from .models import Prediction

class PredictionForm(forms.ModelForm):

    class Meta:
        model = Prediction
        fields = ('team',)


class EmailOutForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    send_to_all = forms.BooleanField(required=False)
