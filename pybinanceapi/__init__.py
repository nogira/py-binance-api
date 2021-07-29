# package version
__version__ = "0.1.3"

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
    if baseurl != '': generated.baseurl = baseurl
    if api_key != '': generated.api_key = api_key
    if api_secret != '': generated.api_secret = api_secret
    if email != '': generated.email = email