from django import forms
from wallet.commands.validators import crw_address
from django.utils.translation import ugettext_lazy as _

class SendForm(forms.Form):
    send_to = forms.CharField(label=_('Dirección destino'), max_length=100, validators=[crw_address])
    amount = forms.FloatField(label=_('Cantidad'))
