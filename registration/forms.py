from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 máximo y válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Check email unique
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta siendo usado, prueba con otro.")

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'balance', 'addr_base', 'addr_withdraw', 'public', 'user']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control-file mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control-file mt-3', 'placeholder': 'Enlace'}),
            #'balance': forms.URLInput(attrs={'class':'form-control-file mt-3', 'placeholder': 'Balance'}),
            'addr_base': forms.TextInput(attrs={'class':'form-control-file mt-3', 'placeholder': 'Dirección Base'}),
            'addr_with': forms.TextInput(attrs={'class':'form-control-file mt-3', 'placeholder': 'Dirección de Retirada'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 máximo y válido.")

    class Meta:
        model = User
        fields = ["email"]

    
    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Check email unique
        if "email" in self.changed_data: 
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta siendo usado, prueba con otro.")

        return email