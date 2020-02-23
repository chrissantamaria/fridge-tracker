from django import forms
from django.utils.timezone import now


class ItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    time_entered = forms.DateTimeField(
        input_formats=["%m/%d/%y, %I:%M %p"]
    )
    expiration_date = forms.DateField(
        required=False,
        input_formats=["%m/%d/%y"]
    )
