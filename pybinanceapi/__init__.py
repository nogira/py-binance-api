from .generated import *

from . import generated as generated

def vars(baseurl='', api_key='', api_secret='', email=''):
    """
## baseurl
Possible Values:
- https://api.binance.com
- https://api1.binance.com
- https://api2.binance.com
- https://api3.binance.com
- https://testnet.binance.vision

## email
- Must replace '@' with '%40' 
    """
    generated.baseurl = baseurl
    generated.api_key = api_key
    generated.api_secret = api_secret
    generated.email = email