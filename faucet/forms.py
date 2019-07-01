from .models import Faucet
from django import forms
from captcha.fields import CaptchaField

class FaucetForm(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Faucet
        fields = ()