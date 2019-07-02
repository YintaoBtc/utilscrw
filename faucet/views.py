from django.shortcuts import render
from .forms import FaucetForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Faucet
#from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from wallet.commands.instruct_wallet import instruct_wallet

import datetime
from django.http import HttpResponse



def faucet_completed(request):
    return render(request, 'faucet_completed.html')

class FaucetCreateView(CreateView):
    form_class = FaucetForm
    template_name = 'faucet.html'

    def get_success_url(self):

        faucet, created = Faucet.objects.get_or_create(username=str(self.request.user))
        
        faucet_date = datetime.datetime.now()
        faucet_date_completed = faucet.updated - datetime.timedelta(1,0)
        print(faucet_date_completed)
        print(faucet_date)
        if faucet_date == faucet_date_completed:
            completed = False
        
        if faucet.completed == True:
            print("Ya lo hiciste hoy, vuelve mañana")
            return reverse_lazy('faucet_completed')

        else: 
            faucet.completed = True
            faucet.username = str(self.request.user)
            faucet.ip_user = str(self.request.META["REMOTE_ADDR"])
            faucet.save()

            user_faucet = faucet.username  + "-faucet"
            print(user_faucet)
            tx = instruct_wallet("move", ["Faucet-CRW", user_faucet, 0.001])["result"]
            balance = instruct_wallet("getbalance", [user_faucet])["result"]
            if balance >= 1:
                tx_move = instruct_wallet("move", [user_faucet, faucet.username, 1])["result"]
            
            return reverse_lazy('profile') + '?created'
 
    def get_form(self, form_class=None):
        form = super(FaucetCreateView, self).get_form()
         
        return form
    