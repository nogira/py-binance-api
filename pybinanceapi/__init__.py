from .generated import *

from . import generated as generated

def vars(baseurl='', api_key='', api_secret='', email=''):
    generated.baseurl = baseurl
    generated.api_key = api_key
    generated.api_secret = api_secret
    generated.email = email