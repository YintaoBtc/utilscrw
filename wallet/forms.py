from django import forms

class SendForm(forms.Form):
    send_to = forms.CharField(label='Dirección destino', max_length=100)
    amount = forms.FloatField(label='Cantidad')