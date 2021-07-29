import hmac, hashlib, requests
from urllib.parse import urlencode

# ----------------------------------CONSTANTS----------------------------------
baseurl = 'https://api.binance.com'
api_key = ''
api_secret = ''
email = 'example@gmail.com'.replace('@', '%40')

def getservertime():
    servertime = requests.get(baseurl+"/api/v3/time")
    servertimeobject = servertime.json()
    return servertimeobject['serverTime']

# ----------------------------------FUNCTIONS----------------------------------
def tohashedsig(params):
    return hmac.new(
        api_secret.encode('utf-8'), 
        params.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def getparams(params):
    params['timestamp'] = getservertime()

    hashedsig = tohashedsig(urlencode(params))

    # add hashedsig to params
    params['signature'] = hashedsig
    
    return params

def getheaders():
    return {'X-MBX-APIKEY': api_key}

def getbinancedata(endpoint, params):
    x = requests.get(baseurl+endpoint, params=params,headers=getheaders())
    return x.json()

def getbinancedata_sig(endpoint, params):
    x = requests.get(baseurl+endpoint, params=getparams(params),headers=getheaders())
    return x.json()

def postbinancedata_sig(endpoint, params, ):
    x = requests.post(baseurl+endpoint, data=getparams(params),headers=getheaders())
    return x.json()

def deletebinancedata_sig(endpoint, params, ):
    x = requests.delete(baseurl+endpoint, data=getparams(params),headers=getheaders())
    return x.json()