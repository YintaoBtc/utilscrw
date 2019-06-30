from core.instruct_wallet import instruct_wallet
from datetime import datetime

def history(username):
    #Take all txs
    txs = instruct_wallet("listtransactions", [str(username)])["result"]

    for tx in reversed(txs[5:]):

        try:
            print (tx)
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
        
    
