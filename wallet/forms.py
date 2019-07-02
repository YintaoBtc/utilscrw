from django import forms
from wallet.commands.validators import crw_address

class SendForm(forms.Form):
    send_to = forms.CharField(label='Dirección destino', max_length=100, validators=[crw_address])
    amount = forms.FloatField(label='Cantidad')
