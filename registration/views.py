from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from wallet.commands.instruct_wallet import instruct_wallet


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        
        # Modificacion en tiempo real
        form.fields["username"].widget = forms.TextInput(attrs={'class':'form-control mb-2', "placeholder":"Nombre de usuario"})
        form.fields["email"].widget = forms.EmailInput(attrs={'class':'form-control mb-2', "placeholder":"Email"})
        form.fields["password1"].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', "placeholder":"Contraseña"})
        form.fields["password2"].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', "placeholder":"Repite la contraseña"})
        
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    

    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        x = profile.user
        faucet_user = str(x) + "-faucet"
        balance_faucet = instruct_wallet('getbalance', [str(faucet_user)])["result"]
        balance = instruct_wallet('getbalance', [str(x)])["result"]
        profile.balance = balance
        profile.balance_faucet = balance_faucet
        profile.save()
        return profile

@method_decorator(login_required, name="dispatch")
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = "registration/profile_email_form.html"

    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields["email"].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placerholder':'email'})
        return form

