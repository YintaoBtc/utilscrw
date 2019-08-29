import json
import requests
import os


#Function for connect with Crown Wallets
def instruct_wallet(method, params):

    #Set data for login
    RPC_USER = os.environ.get('RPC_USER')
    RPC_PHRASE = os.environ.get('RPC_PHRASE')
    RPC_URL = os.environ.get('RPC_URL')

    #Check crownd for info
    payload = json.dumps({"method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    try:
        response = requests.request("POST", RPC_URL, data=payload, headers=headers, auth=(RPC_USER, RPC_PHRASE))
        result = json.loads(response.text)
        return result
    except requests.exceptions.RequestException as e:
        print (e)
    except:
        print ('No response from Wallet, check Bitcoin is running on this machine')

    instruct_wallet('walletpassphrase', [RPC_PHRASE, 5])
    instruct_wallet('settxfee', [0.00000007])