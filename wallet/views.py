from django.http import HttpResponseRedirect
from django.shortcuts import render
from wallet.commands.send import send_wallet
from wallet.commands.history import history_user
from wallet.commands.instruct_wallet import instruct_wallet
from datetime import datetime

from .forms import SendForm

def send_tx(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SendForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            send_to = form.cleaned_data['send_to']
            amount = form.cleaned_data['amount']
            username = request.user
            
            tx = send_wallet(amount, send_to, str(username))
            try:
                tx_id = tx["tx_id"]
                print(tx_id)

                if tx["response"] == "good":
                    return render(request, 'wallet/send_good.html', {"tx":tx_id})
                    #return HttpResponseRedirect('send_good', {"tx":tx_id})
                
                else:
                    return HttpResponseRedirect('send_fail')

            except:
                return HttpResponseRedirect('send_fail')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SendForm()

    return render(request, 'wallet/send_form.html', {'form': form})


def send_good(request):
    return render(request, 'wallet/send_good.html')


def send_fail(request):
    return render(request, 'wallet/send_fail.html')


def history(request):
    txs = history_user(request.user)

    return render(request, 'wallet/history.html', {"txs":txs})