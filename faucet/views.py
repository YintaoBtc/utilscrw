from django.shortcuts import render
from .forms import FaucetForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Faucet
#from django.views.generic.edit import UpdateView
from django.views.generic import CreateView

from django.http import HttpResponse

# Create your views here.
def faucet(request):

    if request.POST:
        form = FaucetForm(request.POST)
        username = request.user
        ip_user = request.META["REMOTE_ADDR"]
        print(f"ESTO ES EL USER: {username}\nESTO SU IP: {ip_user}")


        if form.is_valid():
            human = True
    else:
        form = FaucetForm()

    return render(request, 'faucet.html')

 
class FaucetCreateView(CreateView):
    form_class = FaucetForm
    template_name = 'faucet.html'

    def get_success_url(self):

        faucet, created = Faucet.objects.get_or_create(username=str(self.request.user))
        if faucet.completed == True:
            print("Ya lo hiciste hoy, vuelve mañana")

        else: 
            faucet.completed = True
            faucet.username = str(self.request.user)
            faucet.ip_user = str(self.request.META["REMOTE_ADDR"])
            faucet.save()
        
        return reverse_lazy('profile') + '?created'

    def get_form(self, form_class=None):
        form = super(FaucetCreateView, self).get_form()
        
        return form

    #def save_data(self, request):
    
        #username = str(request.user)
        #ip_user = str(request.META["REMOTE_ADDR"])
        #print(f"ESTO ES EL USER: {username}\nESTO SU IP: {ip_user}")
        #faucet, created = Faucet.objects.get_or_create(username=self.request.user)
        #faucet.ip_user = request.META["REMOTE_ADDR"]
        #faucet.save()
        #return faucet


"""
@method_decorator(login_required, name='dispatch')
class FaucetUpdate(CreateView):
    
    form_class = FaucetForm
    success_url = reverse_lazy('profile')
    template_name = 'faucet.html'

    def get(self, request):
        username = request.user
        ip_user = request.META["REMOTE_ADDR"]
        faucet, created = Faucet.objects.get_or_create(username="laotse")
        faucet.ip_user = "192.0.0.1"
        faucet.save()
        return faucet
"""

    