from wallet.commands.instruct_wallet import instruct_wallet
from datetime import datetime

def history_user(username):
    #Take all txs
    txs = instruct_wallet("listtransactions", [str(username)])["result"]
    txs_list = []

    for tx in txs:
        timestamping = tx["time"]
        date = datetime.fromtimestamp(timestamping)
        
        try:
            address = tx["address"] 
        except:
            address = tx["otheraccount"]

        if address == "FeeWallet":
            pass
        
        else:

            tx_ready = dict(address=address, amount = tx["amount"], date= date, category= tx["category"] )
            txs_list.append(tx_ready)

    return txs_list