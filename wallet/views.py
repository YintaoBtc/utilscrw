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
            print(username)
            tx = send_wallet(amount, send_to, str(username))
            print (tx)

        return HttpResponseRedirect('send_good')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SendForm()

    return render(request, 'wallet/send_form.html', {'form': form})


def send_good(request):
    return render(request, 'wallet/send_good.html')


def history(request):
    #Check ip
    #print(request.META["REMOTE_ADDR"])
    txs = history_user(request.user)

    return render(request, 'wallet/history.html', {"txs":txs})