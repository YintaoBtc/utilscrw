from .instruct_wallet import instruct_wallet

def send_wallet(amount, send_to, username):
    #Take ammount and send to from user
    fee = 0.001

    #Connect at rpc for info, unlock, set tx fee and balance
    balance = instruct_wallet("getbalance", [str(username)])["result"]
        
    #Check if balance its enough
    if balance >= float(amount)+fee:
        
        #If balance is enough and address of Crown net
        if send_to.startswith("CRW"):

            #Fee for use Crown net
            instruct_wallet("move", [str(username), "FeeWallet", fee])
            getinfo = instruct_wallet("sendfrom", [str(username), str(send_to), float(amount)])["result"]
            message = str(amount) + " CRW withdraw to " + send_to + " from " + username + "\nHash Tx: https://chainz.cryptoid.info/crw/tx.dws?"+str(getinfo)
            response = "good"

            data = {"response": response,
                    "tx_id": getinfo
                    }
                    
        else:
            data = "address"


    #If balance not enough
    else:

        #Send message at user with balance
        data = "balance"
    


    return data