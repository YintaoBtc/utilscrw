import json
import requests
import os

#Load Variables
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env()


#Function for connect with Crown Wallets
def instruct_wallet(method, params):

    #Set data for login
    RPC_USER = env('RPC_USER')
    RPC_PHRASE = env('RPC_PHRASE')
    RPC_URL = env('RPC_URL')

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