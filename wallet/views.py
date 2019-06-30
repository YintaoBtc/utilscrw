from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.send import send_wallet
from core.history import history
from core.instruct_wallet import instruct_wallet
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
            print(send_to + str(amount))
            tx = send_wallet(amount, send_to, "laotse")
            print (tx)

        return HttpResponseRedirect('send_good')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SendForm()

    return render(request, 'wallet/send_form.html', {'form': form})


def send_good(request):
    return render(request, 'wallet/send_good.html')


def history(request):
    txs = instruct_wallet("listtransactions", [str("laotse")])["result"]
    for tx in reversed(txs):
        try:
            sendto = tx["otheraccount"]
            amount = tx["amount"]
            timestamping = tx["time"]
            date = datetime.fromtimestamp(timestamping)
            print("{} CRW || {} || {}".format(amount, sendto, date))        
        
        except:
            amount = tx["amount"]
            timestamping = tx["time"]
            address = tx["address"]
            date = datetime.fromtimestamp(timestamping)
            print("{} CRW || {} || {} ".format(amount,address, date))

    history = "Probando esto de las variables"
    return render(request, 'wallet/history.html', {"txs":txs})