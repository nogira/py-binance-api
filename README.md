# Python Wrapper for the Binance API

Made by scraping [binance docs](https://binance-docs.github.io/apidocs) to allow for easy updates as the API changes. 

Functions include some documentation, but if in need of more information, read the [binance docs](https://binance-docs.github.io/apidocs) (The parameters listed in the docs are the same name as in the python wrapper).

Also, to find the name of a function based on its title in the binance docs, just search the `function names.md` file in this repository.

<br>

Currently no support for streams.

<br>

Notes:
- The `timestamp` parameter is autogenerated by the wrapper so while it is a mandatory parameter to call some things in binance's API, you do not need to declare it when using this wrapper.
- You dont need an `api_key`/`api_secret` unless you're interacting with a binance account (e.g. getting the price of bitcoin doesn't need them)

### Basic Setup

```shell
pip install py-binance-api
```

```py
import py-binance-api as pb

# declare api key and secret
# (can also declare 'baseurl' (default is https://api.binance.com) or 'email' (change '@' to '%40'))
pb.vars(
    api_key='FaROkRyeIfyMeAS53cmVlzVHCTcpcM7qPf2Mlf9nz3QpOEmYbOGOugndQ11pyX8D', 
    api_secret='ZnDfwtZZ7s2QXhw5pw65rzT6IKX731fIj78M7MGpdmiH5UdMhyujBlRxBqZldDFm'
)


# function example
pb.getKline(symbol='BTCBUSD', interval='1m')

# -> [[1627491540000,'40137.19000000','40142.85000000','40104.79000000','40129.66000000',
#    '5.21430300',1627491599999,'209204.30175243',223,'2.33255200','93581.43908787','0'],
#    [1627491600000,'40129.65000000','40129.66000000','40065.84000000','40067.32000000',
#    '4.40163100',1627491659999,'176503.34747241',243,'1.33479500','53523.47926157','0'], ...etc

```

<br>

<br>

## [Support Me :)](https://nogira.github.io/generate/donate.html)
