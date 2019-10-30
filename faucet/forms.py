from .models import Faucet
from django import forms
from captcha.fields import CaptchaField


class FaucetForm(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Faucet
        fields = ()

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

        self.fields['captcha'].widget.attrs.update({'class': 'form-control', 'placeholder': "Enter code here"})
