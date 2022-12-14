from django import forms
from .models import FeedbackModel, RezumFormModel


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        # fields = '__all__'
        exclude = ('ready',)



class RezumForm(forms.ModelForm):
    class Meta:
        model = RezumFormModel

        exclude = ('ready',)
