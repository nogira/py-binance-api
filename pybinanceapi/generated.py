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

# ------------------------------------------------------------------------------

#                               Wallet Endpoints

# ------------------------------------------------------------------------------

def getSystemStatus():
    """# System Status (System)
#### `GET /sapi/v1/system/status`
Fetch system status.
### 
### Parameters:
NONE    """
    endpoint = '/sapi/v1/system/status'
    params = {

    }


    return getbinancedata(endpoint, params)


def getAllCoinsInfo(recvWindow=""):
    """# All Coins' Information (USER_DATA)
#### `GET /sapi/v1/capital/config/getall (HMAC SHA256)`
Get information of coins (available for deposit and withdraw) for user.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/capital/config/getall'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getAccSnapshot(type, startTime="", endTime="", limit="", recvWindow=""):
    """# Daily Account Snapshot (USER_DATA)
#### `GET /sapi/v1/accountSnapshot (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
type	|STRING	|YES	|"SPOT", "MARGIN", "FUTURES"
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|min 5, max 30, default 5
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/accountSnapshot'
    params = {
        "type": type
    }
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def disableFastWithdraw(recvWindow=""):
    """# Disable Fast Withdraw Switch (USER_DATA)
#### `POST /sapi/v1/account/disableFastWithdrawSwitch (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/account/disableFastWithdrawSwitch'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def enableFastWithdraw(recvWindow=""):
    """# Enable Fast Withdraw Switch (USER_DATA)
#### `POST /sapi/v1/account/enableFastWithdrawSwitch (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/account/enableFastWithdrawSwitch'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def withdrawCoin(coin, address, amount, withdrawOrderId="", network="", addressTag="", transactionFeeFlag="", name="", recvWindow=""):
    """# Withdraw(SAPI)
#### `POST /sapi/v1/capital/withdraw/apply (HMAC SHA256)`
Submit a withdraw request.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|YES	|
withdrawOrderId	|STRING	|NO	|client id for withdraw
network	|STRING	|NO	|
address	|STRING	|YES	|
addressTag	|STRING	|NO	|Secondary address identifier for coins like XRP,XMR etc.
amount	|DECIMAL	|YES	|
transactionFeeFlag	|BOOLEAN	|NO	|When making internal transfer, <code>true</code> for returning the fee to the destination account; <code>false</code> for returning the fee back to the departure account. Default <code>false</code>.
name	|STRING	|NO	|Description of the address. Space in name should be encoded into <code>%20</code>.
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/capital/withdraw/apply'
    params = {
        "coin": coin,
        "address": address,
        "amount": amount
    }
    if withdrawOrderId: params["withdrawOrderId"] = withdrawOrderId
    if network: params["network"] = network
    if addressTag: params["addressTag"] = addressTag
    if transactionFeeFlag: params["transactionFeeFlag"] = transactionFeeFlag
    if name: params["name"] = name
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getDepositHistory(coin="", status="", startTime="", endTime="", offset="", limit="", recvWindow=""):
    """# Deposit History(supporting network) (USER_DATA)
#### `GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)`
Fetch deposit history.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|NO	|
status	|INT	|NO	|0(0:pending,6: credited but cannot withdraw, 1:success)
startTime	|LONG	|NO	|Default: 90 days from current timestamp
endTime	|LONG	|NO	|Default: present timestamp
offset	|INT	|NO	|Default:0
limit	|INT	|NO	|Default:1000, Max:1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/capital/deposit/hisrec'
    params = {

    }
    if coin: params["coin"] = coin
    if status: params["status"] = status
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if offset: params["offset"] = offset
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getWithdrawHistory(coin="", status="", offset="", limit="", startTime="", endTime="", recvWindow=""):
    """# Withdraw History (supporting network) (USER_DATA)
#### `GET /sapi/v1/capital/withdraw/history (HMAC SHA256)`
Fetch withdraw history.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|NO	|
status	|INT	|NO	|0(0:Email Sent,1:Cancelled 2:Awaiting Approval 3:Rejected 4:Processing 5:Failure 6:Completed)
offset	|INT	|NO	|
limit	|INT	|NO	|Default: 1000, Max: 1000
startTime	|LONG	|NO	|Default: 90 days from current timestamp
endTime	|LONG	|NO	|Default: present timestamp
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/capital/withdraw/history'
    params = {

    }
    if coin: params["coin"] = coin
    if status: params["status"] = status
    if offset: params["offset"] = offset
    if limit: params["limit"] = limit
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getCoinDepositAddr(coin, network="", recvWindow=""):
    """# Deposit Address (supporting network) (USER_DATA)
#### `GET /sapi/v1/capital/deposit/address (HMAC SHA256)`
Fetch deposit address with network.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|YES	|
network	|STRING	|NO	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/capital/deposit/address'
    params = {
        "coin": coin
    }
    if network: params["network"] = network
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getAccStatus(recvWindow=""):
    """# Account Status (USER_DATA)
#### `GET /sapi/v1/account/status`
Fetch account status detail.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/account/status'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getApiTradingStatus(recvWindow=""):
    """# Account API Trading Status (USER_DATA)
#### `GET /sapi/v1/account/apiTradingStatus (HMAC SHA256)`
Fetch account api trading status detail.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/account/apiTradingStatus'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getDustHistory(startTime="", endTime="", recvWindow=""):
    """# DustLog(USER_DATA)
#### `GET /sapi/v1/asset/dribblet   (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/asset/dribblet'
    params = {

    }
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getDividendHistory(asset="", startTime="", endTime="", limit="", recvWindow=""):
    """# Asset Dividend Record (USER_DATA)
#### `GET /sapi/v1/asset/assetDividend (HMAC SHA256)`
Query asset dividend record.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|Default 20, max 500
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/asset/assetDividend'
    params = {

    }
    if asset: params["asset"] = asset
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getFundingAsset(asset="", needBtcValuation="", recvWindow=""):
    """# Funding Wallet (USER_DATA)
#### `POST /sapi/v1/asset/get-funding-asset (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|NO	|
needBtcValuation	|STRING	|NO	|true or false
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/asset/get-funding-asset'
    params = {

    }
    if asset: params["asset"] = asset
    if needBtcValuation: params["needBtcValuation"] = needBtcValuation
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getApiPermissions(recvWindow=""):
    """# Get API Key Permission (USER_DATA)
#### `GET /sapi/v1/account/apiRestrictions (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/account/apiRestrictions'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                            Sub-Account Endpoints

# ------------------------------------------------------------------------------

def masterGetSpotSubaccToSubaccTransferHist(fromEmail="", toEmail="", startTime="", endTime="", page="", limit="", recvWindow=""):
    """# Query Sub-account Spot Asset Transfer History (For Master Account)
#### `GET /sapi/v1/sub-account/sub/transfer/history (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
fromEmail	|STRING	|NO	|Sub-account email
toEmail	|STRING	|NO	|Sub-account email
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
page	|INT	|NO	|Default value: 1
limit	|INT	|NO	|Default value: 500
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/sub/transfer/history'
    params = {

    }
    if fromEmail: params["fromEmail"] = fromEmail
    if toEmail: params["toEmail"] = toEmail
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if page: params["page"] = page
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetFutSubaccToSubaccTransferHist(email, futuresType, startTime="", endTime="", page="", limit="", recvWindow=""):
    """# Query Sub-account Futures Asset Transfer History (For Master Account)
#### `GET /sapi/v1/sub-account/futures/internalTransfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub-account email
futuresType	|LONG	|YES	|1:USDT-margined Futures，2: Coin-margined Futures
startTime	|LONG	|NO	|Default return the history with in 100 days
endTime	|LONG	|NO	|Default return the history with in 100 days
page	|INT	|NO	|Default value: 1
limit	|INT	|NO	|Default value: 50, Max value: 500
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/futures/internalTransfer'
    params = {
        "email": email,
        "futuresType": futuresType
    }
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if page: params["page"] = page
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterTransferFutFrmSubaccToSubacc(fromEmail, toEmail, futuresType, asset, amount, recvWindow=""):
    """# Sub-account Futures Asset Transfer (For Master Account)
#### `POST /sapi/v1/sub-account/futures/internalTransfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
fromEmail	|STRING	|YES	|Sender email
toEmail	|STRING	|YES	|Recipient email
futuresType	|LONG	|YES	|1:USDT-margined Futures，2: Coin-margined Futures
asset	|STRING	|YES	|
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/futures/internalTransfer'
    params = {
        "fromEmail": fromEmail,
        "toEmail": toEmail,
        "futuresType": futuresType,
        "asset": asset,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def masterGetSubaccSpotAssets(email="", page="", size="", recvWindow=""):
    """# Query Sub-account Spot Assets Summary (For Master Account)
#### `GET /sapi/v1/sub-account/spotSummary (HMAC SHA256)`
Get BTC valued asset summary of subaccounts.
### Weight:
5
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|NO	|Sub account email
page	|LONG	|NO	|default 1
size	|LONG	|NO	|default 10, max 20
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/spotSummary'
    params = {

    }
    if email: params["email"] = email
    if page: params["page"] = page
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccDepositAddr(email, coin, network="", recvWindow=""):
    """# Get Sub-account Deposit Address (For Master Account)
#### `GET /sapi/v1/capital/deposit/subAddress (HMAC SHA256)`
Fetch sub-account deposit address
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub account email
coin	|STRING	|YES	|
network	|STRING	|NO	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/capital/deposit/subAddress'
    params = {
        "email": email,
        "coin": coin
    }
    if network: params["network"] = network
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccDepositHistory(email, coin="", status="", startTime="", endTime="", limit="", offset="", recvWindow=""):
    """# Get Sub-account Deposit History (For Master Account)
#### `GET /sapi/v1/capital/deposit/subHisrec (HMAC SHA256)`
Fetch sub-account deposit history
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub account email
coin	|STRING	|NO	|
status	|INT	|NO	|0(0:pending,6: credited but cannot withdraw, 1:success)
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|
offset	|INT	|NO	|default:0
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/capital/deposit/subHisrec'
    params = {
        "email": email
    }
    if coin: params["coin"] = coin
    if status: params["status"] = status
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if offset: params["offset"] = offset
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccMargFutStatus(email="", recvWindow=""):
    """# Get Sub-account's Status on Margin/Futures (For Master Account)
#### `GET /sapi/v1/sub-account/status (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|NO	|Sub-account email
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/status'
    params = {

    }
    if email: params["email"] = email
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterEnableMargSubacc(email, recvWindow=""):
    """# Enable Margin for Sub-account (For Master Account)
#### `POST /sapi/v1/sub-account/margin/enable (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub-account email
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/margin/enable'
    params = {
        "email": email
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def masterGetSubaccMargDetails(email, recvWindow=""):
    """# Get Detail on Sub-account's Margin Account (For Master Account)
#### `GET /sapi/v1/sub-account/margin/account (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub-account email
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/margin/account'
    params = {
        "email": email
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccMargSumm(recvWindow=""):
    """# Get Summary of Sub-account's Margin Account (For Master Account)
#### `GET /sapi/v1/sub-account/margin/accountSummary (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/margin/accountSummary'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterEnableFutSubacc(email, recvWindow=""):
    """# Enable Futures for Sub-account (For Master Account)
#### `POST /sapi/v1/sub-account/futures/enable (HMAC SHA256)`
<strong>Response:</strong>
1
### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub-account email
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/futures/enable'
    params = {
        "email": email
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def masterGetSubaccFutDetails(email, recvWindow=""):
    """# Get Detail on Sub-account's Futures Account (For Master Account)
#### `GET /sapi/v1/sub-account/futures/account (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub-account email
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/futures/account'
    params = {
        "email": email
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccFutSumm(recvWindow=""):
    """# Get Summary of Sub-account's Futures Account (For Master Account)
#### `GET /sapi/v1/sub-account/futures/accountSummary (HMAC SHA256)`

### Weight:
20
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/futures/accountSummary'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccFutPosRisk(email, recvWindow=""):
    """# Get Futures Position-Risk of Sub-account (For Master Account)
#### `GET /sapi/v1/sub-account/futures/positionRisk (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|String	|YES	|Sub-account email
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/futures/positionRisk'
    params = {
        "email": email
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterTransferFutWithinSubacc(email, asset, amount, type):
    """# Futures Transfer for Sub-account (For Master Account)
#### `POST /sapi/v1/sub-account/futures/transfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|String	|YES	|Sub-account email
asset	|STRING	|YES	|The asset being transferred, e.g., USDT
amount	|DECIMAL	|YES	|The amount to be transferred
type	|INT	|YES	|1: transfer from subaccount's spot account to its USDT-margined futures account 2: transfer from subaccount's USDT-margined futures account to its spot account 3: transfer from subaccount's spot account to its COIN-margined futures account 4:transfer from subaccount's COIN-margined futures account to its spot account
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/futures/transfer'
    params = {
        "email": email,
        "asset": asset,
        "amount": amount,
        "type": type
    }


    return postbinancedata_sig(endpoint, params)


def masterTransferMargWithinSubacc(email, asset, amount, type):
    """# Margin Transfer for Sub-account (For Master Account)
#### `POST /sapi/v1/sub-account/margin/transfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|String	|YES	|Sub-account email
asset	|STRING	|YES	|The asset being transferred, e.g., BTC
amount	|DECIMAL	|YES	|The amount to be transferred
type	|INT	|YES	|1: transfer from subaccount's  spot account to margin account 2: transfer from subaccount's margin account to its spot account
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/margin/transfer'
    params = {
        "email": email,
        "asset": asset,
        "amount": amount,
        "type": type
    }


    return postbinancedata_sig(endpoint, params)


def subaccTransferToSubacc(toEmail, asset, amount, recvWindow=""):
    """# Transfer to Sub-account of Same Master (For Sub-account)
#### `POST /sapi/v1/sub-account/transfer/subToSub (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
toEmail	|String	|YES	|Sub-account email
asset	|STRING	|YES	|
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/transfer/subToSub'
    params = {
        "toEmail": toEmail,
        "asset": asset,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def subaccTransferToMaster(asset, amount, recvWindow=""):
    """# Transfer to Master (For Sub-account)
#### `POST /sapi/v1/sub-account/transfer/subToMaster (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/transfer/subToMaster'
    params = {
        "asset": asset,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def subaccGetTransferHistory(asset="", type="", startTime="", endTime="", limit="", recvWindow=""):
    """# Sub-account Transfer History (For Sub-account)
#### `GET /sapi/v1/sub-account/transfer/subUserHistory (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|NO	|If not sent, result of all assets will be returned
type	|INT	|NO	|1: transfer in, 2: transfer out
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|Default 500
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/transfer/subUserHistory'
    params = {

    }
    if asset: params["asset"] = asset
    if type: params["type"] = type
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterUniversalTransferSubacc(fromAccountType, toAccountType, asset, amount, fromEmail="", toEmail="", recvWindow=""):
    """# Universal Transfer (For Master Account)
#### `POST /sapi/v1/sub-account/universalTransfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
fromEmail	|STRING	|NO	|
toEmail	|STRING	|NO	|
fromAccountType	|STRING	|YES	|"SPOT","USDT_FUTURE","COIN_FUTURE"
toAccountType	|STRING	|YES	|"SPOT","USDT_FUTURE","COIN_FUTURE"
asset	|STRING	|YES	|
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/universalTransfer'
    params = {
        "fromAccountType": fromAccountType,
        "toAccountType": toAccountType,
        "asset": asset,
        "amount": amount
    }
    if fromEmail: params["fromEmail"] = fromEmail
    if toEmail: params["toEmail"] = toEmail
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def masterSubaccUniversalTransferHistory(fromEmail="", toEmail="", startTime="", endTime="", page="", limit="", recvWindow=""):
    """# Query Universal Transfer History (For Master Account)
#### `GET /sapi/v1/sub-account/universalTransfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
fromEmail	|STRING	|NO	|
toEmail	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
page	|INT	|NO	|Default 1
limit	|INT	|NO	|Default 500, Max 500
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/universalTransfer'
    params = {

    }
    if fromEmail: params["fromEmail"] = fromEmail
    if toEmail: params["toEmail"] = toEmail
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if page: params["page"] = page
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccFutDetailsv2(email, futuresType, recvWindow=""):
    """# Get Detail on Sub-account's Futures Account V2 (For Master Account)
#### `GET /sapi/v2/sub-account/futures/account (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub-account email
futuresType	|INT	|YES	|1:USDT Margined Futures, 2:COIN Margined Futures
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v2/sub-account/futures/account'
    params = {
        "email": email,
        "futuresType": futuresType
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccFutSummv2(futuresType, page="", limit="", recvWindow=""):
    """# Get Summary of Sub-account's Futures Account V2 (For Master Account)
#### `GET /sapi/v2/sub-account/futures/accountSummary (HMAC SHA256)`

### Weight:
20
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
futuresType	|INT	|YES	|1:USDT Margined Futures, 2:COIN Margined Futures
page	|INT	|NO	|default:1
limit	|INT	|NO	|default:10, max:20
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v2/sub-account/futures/accountSummary'
    params = {
        "futuresType": futuresType
    }
    if page: params["page"] = page
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterGetSubaccFutPosRiskv2(email, futuresType, recvWindow=""):
    """# Get Futures Position-Risk of Sub-account V2 (For Master Account)
#### `GET /sapi/v2/sub-account/futures/positionRisk (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|Sub-account email
futuresType	|INT	|YES	|1:USDT Margined Futures, 2:COIN Margined Futures
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v2/sub-account/futures/positionRisk'
    params = {
        "email": email,
        "futuresType": futuresType
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def masterEnableLeverageTokenInSubacc(email, enableBlvt, recvWindow=""):
    """# Enable Leverage Token for Sub-account  (For Master Account)
#### `POST /sapi/v1/sub-account/blvt/enable (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|String	|YES	|Sub-account email
enableBlvt	|BOOLEAN	|YES	|Only true for now
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/sub-account/blvt/enable'
    params = {
        "email": email,
        "enableBlvt": enableBlvt
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def investorMasterDepositAssetToSubacc(toEmail, asset, amount, recvWindow=""):
    """# Deposit assets into the managed sub-account（For Investor Master Account）
#### `POST /sapi/v1/managed-subaccount/deposit (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
toEmail	|STRING	|YES	|
asset	|STRING	|YES	|
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/managed-subaccount/deposit'
    params = {
        "toEmail": toEmail,
        "asset": asset,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def investorMasterGetSubaccAssetDetails(email, recvWindow=""):
    """# Query managed sub-account asset details（For Investor Master Account）
#### `GET /sapi/v1/managed-subaccount/asset   (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
email	|STRING	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/managed-subaccount/asset'
    params = {
        "email": email
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def investorMasterWithdrawAssetFrmSubacc(fromEmail, asset, amount, transferDate="", recvWindow=""):
    """# Withdrawl assets from the managed sub-account（For Investor Master Account）
#### `POST /sapi/v1/managed-subaccount/withdraw (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
fromEmail	|STRING	|YES	|
asset	|STRING	|YES	|
amount	|DECIMAL	|YES	|
transferDate	|LONG	|NO	|Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the withdrawal occurs right now
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/managed-subaccount/withdraw'
    params = {
        "fromEmail": fromEmail,
        "asset": asset,
        "amount": amount
    }
    if transferDate: params["transferDate"] = transferDate
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                            Market Data Endpoints

# ------------------------------------------------------------------------------

def testConnectivity():
    """# Test Connectivity
#### `GET /api/v3/ping`
Test connectivity to the Rest API.NONE<strong>Data Source:</strong> Memory
### Weight:
1
### Parameters:
NONE    """
    endpoint = '/api/v3/ping'
    params = {

    }


    return getbinancedata(endpoint, params)


def serverTime():
    """# Check Server Time
#### `GET /api/v3/time`
Test connectivity to the Rest API and get the current server time.NONE<strong>Data Source:</strong>
Memory
### Weight:
1
### Parameters:
NONE    """
    endpoint = '/api/v3/time'
    params = {

    }


    return getbinancedata(endpoint, params)


def exchangeInfo():
    """# Exchange Information
#### `GET /api/v3/exchangeInfo`
Current exchange trading rules and symbol informationThere are 3 possible options:If any symbol provided in either `symbol` or `symbols` do not exist, the endpoint will throw an error.<strong>Data Source:</strong>
Memory
### Weight:
10
### Parameters:
NONE    """
    endpoint = '/api/v3/exchangeInfo'
    params = {

    }


    return getbinancedata(endpoint, params)


def getOrderBook(symbol, limit=""):
    """# Order Book
#### `GET /api/v3/depth`
Adjusted based on the limit:
### Weight:
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
limit	|INT	|NO	|Default 100; max 5000. Valid limits:[5, 10, 20, 50, 100, 500, 1000, 5000]

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/depth'
    params = {
        "symbol": symbol
    }
    if limit: params["limit"] = limit

    return getbinancedata(endpoint, params)


def getRecentTrades(symbol, limit=""):
    """# Recent Trades List
#### `GET /api/v3/trades`
Get recent trades.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
limit	|INT	|NO	|Default 500; max 1000.

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/trades'
    params = {
        "symbol": symbol
    }
    if limit: params["limit"] = limit

    return getbinancedata(endpoint, params)


def getOldTrades(symbol, limit="", fromId=""):
    """# Old Trade Lookup
#### `GET /api/v3/historicalTrades`
Get older market trades.
### Weight:
5
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
limit	|INT	|NO	|Default 500; max 1000.
fromId	|LONG	|NO	|Trade id to fetch from. Default gets most recent trades.

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/historicalTrades'
    params = {
        "symbol": symbol
    }
    if limit: params["limit"] = limit
    if fromId: params["fromId"] = fromId

    return getbinancedata(endpoint, params)


def getCompressedTrades(symbol, fromId="", startTime="", endTime="", limit=""):
    """# Compressed/Aggregate Trades List
#### `GET /api/v3/aggTrades`
Get compressed, aggregate trades. Trades that fill at the time, from the same
order, with the same price will have the quantity aggregated.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
fromId	|LONG	|NO	|id to get aggregate trades from INCLUSIVE.
startTime	|LONG	|NO	|Timestamp in ms to get aggregate trades from INCLUSIVE.
endTime	|LONG	|NO	|Timestamp in ms to get aggregate trades until INCLUSIVE.
limit	|INT	|NO	|Default 500; max 1000.

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/aggTrades'
    params = {
        "symbol": symbol
    }
    if fromId: params["fromId"] = fromId
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit

    return getbinancedata(endpoint, params)


def getKline(symbol, interval, startTime="", endTime="", limit=""):
    """# Kline/Candlestick Data
#### `GET /api/v3/klines`
Kline/candlestick bars for a symbol.<br/>
Klines are uniquely identified by their open time.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
interval	|ENUM	|YES	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|Default 500; max 1000.

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/klines'
    params = {
        "symbol": symbol,
        "interval": interval
    }
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit

    return getbinancedata(endpoint, params)


def getCurrentAvgPrice(symbol):
    """# Current Average Price
#### `GET /api/v3/avgPrice`
Current average price for a symbol.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
    """
    endpoint = '/api/v3/avgPrice'
    params = {
        "symbol": symbol
    }


    return getbinancedata(endpoint, params)


def get24hrPriceStats(symbol=""):
    """# 24hr Ticker Price Change Statistics
#### `GET /api/v3/ticker/24hr`
24 hour rolling window price change statistics. <strong>Careful</strong> when accessing this with no symbol.
### Weight:
1 for a single symbol;<br/>
40 when the symbol parameter is omitted;
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|NO	|
    """
    endpoint = '/api/v3/ticker/24hr'
    params = {

    }
    if symbol: params["symbol"] = symbol

    return getbinancedata(endpoint, params)


def getPrice(symbol=""):
    """# Symbol Price Ticker
#### `GET /api/v3/ticker/price`
Latest price for a symbol or symbols.1 for a single symbol;<br/>
<strong>2</strong> when the symbol parameter is omitted
### Weight:
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|NO	|
    """
    endpoint = '/api/v3/ticker/price'
    params = {

    }
    if symbol: params["symbol"] = symbol

    return getbinancedata(endpoint, params)


def getBestOrderBookPrice(symbol=""):
    """# Symbol Order Book Ticker
#### `GET /api/v3/ticker/bookTicker`
Best price/qty on the order book for a symbol or symbols.1 for a single symbol;<br/>
<strong>2</strong> when the symbol parameter is omitted
### Weight:
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|NO	|
    """
    endpoint = '/api/v3/ticker/bookTicker'
    params = {

    }
    if symbol: params["symbol"] = symbol

    return getbinancedata(endpoint, params)


# ------------------------------------------------------------------------------

#                              Spot Account/Trade

# ------------------------------------------------------------------------------

def testNewOrder():
    """# Test New Order (TRADE)
#### `POST /api/v3/order/test (HMAC SHA256)`
Test new order creation and signature/recvWindow long.
Creates and validates a new order but does not send it into the matching engine.Same as `POST /api/v3/order`<strong>Data Source:</strong>
Memory
### Weight:
1
### Parameters:
NONE    """
    endpoint = '/api/v3/order/test'
    params = {

    }


    return postbinancedata_sig(endpoint, params)


def newOrder(symbol, side, type, timeInForce="", quantity="", quoteOrderQty="", price="", newClientOrderId="", stopPrice="", icebergQty="", newOrderRespType="", recvWindow=""):
    """# New Order  (TRADE)
#### `POST /api/v3/order  (HMAC SHA256)`
Send in a new order.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
side	|ENUM	|YES	|
type	|ENUM	|YES	|
timeInForce	|ENUM	|NO	|
quantity	|DECIMAL	|NO	|
quoteOrderQty	|DECIMAL	|NO	|
price	|DECIMAL	|NO	|
newClientOrderId	|STRING	|NO	|A unique id among open orders. Automatically generated if not sent.
stopPrice	|DECIMAL	|NO	|Used with <code>STOP_LOSS</code>, <code>STOP_LOSS_LIMIT</code>, <code>TAKE_PROFIT</code>, and <code>TAKE_PROFIT_LIMIT</code> orders.
icebergQty	|DECIMAL	|NO	|Used with <code>LIMIT</code>, <code>STOP_LOSS_LIMIT</code>, and <code>TAKE_PROFIT_LIMIT</code> to create an iceberg order.
newOrderRespType	|ENUM	|NO	|Set the response JSON. <code>ACK</code>, <code>RESULT</code>, or <code>FULL</code>; <code>MARKET</code> and <code>LIMIT</code> order types default to <code>FULL</code>, all other orders default to <code>ACK</code>.
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

Additional mandatory parameters based on Other info:Trigger order price rules against market price for both MARKET and LIMIT versions:<strong>Data Source:</strong>    """
    endpoint = '/api/v3/order'
    params = {
        "symbol": symbol,
        "side": side,
        "type": type
    }
    if timeInForce: params["timeInForce"] = timeInForce
    if quantity: params["quantity"] = quantity
    if quoteOrderQty: params["quoteOrderQty"] = quoteOrderQty
    if price: params["price"] = price
    if newClientOrderId: params["newClientOrderId"] = newClientOrderId
    if stopPrice: params["stopPrice"] = stopPrice
    if icebergQty: params["icebergQty"] = icebergQty
    if newOrderRespType: params["newOrderRespType"] = newOrderRespType
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def cancelOrder(symbol, orderId="", origClientOrderId="", newClientOrderId="", recvWindow=""):
    """# Cancel Order (TRADE)
#### `DELETE /api/v3/order  (HMAC SHA256)`
Cancel an active order.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
orderId	|LONG	|NO	|
origClientOrderId	|STRING	|NO	|
newClientOrderId	|STRING	|NO	|Used to uniquely identify this cancel. Automatically generated by default.
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

Either <strong>Data Source:</strong>    """
    endpoint = 'DELETE /api/v3/order'
    params = {
        "symbol": symbol
    }
    if orderId: params["orderId"] = orderId
    if origClientOrderId: params["origClientOrderId"] = origClientOrderId
    if newClientOrderId: params["newClientOrderId"] = newClientOrderId
    if recvWindow: params["recvWindow"] = recvWindow

    return deletebinancedata_sig(endpoint, params)


def getOrderStatus(symbol, orderId="", origClientOrderId="", recvWindow=""):
    """# Query Order (USER_DATA)
#### `GET /api/v3/order (HMAC SHA256)`
Check an order's status.
### Weight:
2
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
orderId	|LONG	|NO	|
origClientOrderId	|STRING	|NO	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

Notes:<strong>Data Source:</strong>    """
    endpoint = '/api/v3/order'
    params = {
        "symbol": symbol
    }
    if orderId: params["orderId"] = orderId
    if origClientOrderId: params["origClientOrderId"] = origClientOrderId
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getOpenOrders(symbol="", recvWindow=""):
    """# Current Open Orders (USER_DATA)
#### `GET /api/v3/openOrders  (HMAC SHA256)`
Get all open orders on a symbol. <strong>Careful</strong> when accessing this with no symbol.
### Weight:
3 for a single symbol; 40 when the symbol parameter is omitted
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|NO	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/openOrders'
    params = {

    }
    if symbol: params["symbol"] = symbol
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getAllOrders(symbol, orderId="", startTime="", endTime="", limit="", recvWindow=""):
    """# All Orders (USER_DATA)
#### `GET /api/v3/allOrders (HMAC SHA256)`
Get all account orders; active, canceled, or filled.
### Weight:
10 with symbol
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
orderId	|LONG	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|Default 500; max 1000.
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

<strong>Notes:</strong><strong>Data Source:</strong>    """
    endpoint = '/api/v3/allOrders'
    params = {
        "symbol": symbol
    }
    if orderId: params["orderId"] = orderId
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def newOCO(symbol, side, quantity, price, stopPrice, listClientOrderId="", limitClientOrderId="", limitIcebergQty="", stopClientOrderId="", stopLimitPrice="", stopIcebergQty="", stopLimitTimeInForce="", newOrderRespType="", recvWindow=""):
    """# New OCO (TRADE)
#### `POST /api/v3/order/oco (HMAC SHA256)`
Send in a new OCO
### Weight: 1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
listClientOrderId	|STRING	|NO	|A unique Id for the entire orderList
side	|ENUM	|YES	|
quantity	|DECIMAL	|YES	|
limitClientOrderId	|STRING	|NO	|A unique Id for the limit order
price	|DECIMAL	|YES	|
limitIcebergQty	|DECIMAL	|NO	|
stopClientOrderId	|STRING	|NO	|A unique Id for the stop loss/stop loss limit leg
stopPrice	|DECIMAL	|YES	|
stopLimitPrice	|DECIMAL	|NO	|If provided, <code>stopLimitTimeInForce</code> is required.
stopIcebergQty	|DECIMAL	|NO	|
stopLimitTimeInForce	|ENUM	|NO	|Valid values are <code>GTC</code>/<code>FOK</code>/<code>IOC</code>
newOrderRespType	|ENUM	|NO	|Set the response JSON.
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

Other Info:<strong>Data Source:</strong>    """
    endpoint = '/api/v3/order/oco'
    params = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price,
        "stopPrice": stopPrice
    }
    if listClientOrderId: params["listClientOrderId"] = listClientOrderId
    if limitClientOrderId: params["limitClientOrderId"] = limitClientOrderId
    if limitIcebergQty: params["limitIcebergQty"] = limitIcebergQty
    if stopClientOrderId: params["stopClientOrderId"] = stopClientOrderId
    if stopLimitPrice: params["stopLimitPrice"] = stopLimitPrice
    if stopIcebergQty: params["stopIcebergQty"] = stopIcebergQty
    if stopLimitTimeInForce: params["stopLimitTimeInForce"] = stopLimitTimeInForce
    if newOrderRespType: params["newOrderRespType"] = newOrderRespType
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def cancelOCO(symbol, orderListId="", listClientOrderId="", newClientOrderId="", recvWindow=""):
    """# Cancel OCO (TRADE)
#### `DELETE /api/v3/orderList (HMAC SHA256)`

### Weight: 1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
orderListId	|LONG	|NO	|Either <code>orderListId</code> or <code>listClientOrderId</code> must be provided
listClientOrderId	|STRING	|NO	|Either <code>orderListId</code> or <code>listClientOrderId</code> must be provided
newClientOrderId	|STRING	|NO	|Used to uniquely identify this cancel. Automatically generated by default
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

Additional notes:<strong>Data Source:</strong>    """
    endpoint = 'DELETE /api/v3/orderList'
    params = {
        "symbol": symbol
    }
    if orderListId: params["orderListId"] = orderListId
    if listClientOrderId: params["listClientOrderId"] = listClientOrderId
    if newClientOrderId: params["newClientOrderId"] = newClientOrderId
    if recvWindow: params["recvWindow"] = recvWindow

    return deletebinancedata_sig(endpoint, params)


def getOCOStaus(orderListId="", origClientOrderId="", recvWindow=""):
    """# Query OCO (USER_DATA)
#### `GET /api/v3/orderList (HMAC SHA256)`
Retrieves a specific OCO based on provided optional parameters
### Weight: 2
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
orderListId	|LONG	|NO	|Either <code>orderListId</code> or <code>listClientOrderId</code> must be provided
origClientOrderId	|STRING	|NO	|Either <code>orderListId</code> or <code>listClientOrderId</code> must be provided
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/orderList'
    params = {

    }
    if orderListId: params["orderListId"] = orderListId
    if origClientOrderId: params["origClientOrderId"] = origClientOrderId
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getAllOCO(fromId="", startTime="", endTime="", limit="", recvWindow=""):
    """# Query all OCO (USER_DATA)
#### `GET /api/v3/allOrderList (HMAC SHA256)`
Retrieves all OCO based on provided optional parameters
### Weight: 10
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
fromId	|LONG	|NO	|If supplied, neither <code>startTime</code> or <code>endTime</code> can be provided
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|Default Value: 500; Max Value: 1000
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/allOrderList'
    params = {

    }
    if fromId: params["fromId"] = fromId
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getOpenOCO(recvWindow=""):
    """# Query Open OCO (USER_DATA)
#### `GET /api/v3/openOrderList (HMAC SHA256)`

### Weight: 3
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/openOrderList'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getAccInfo(recvWindow=""):
    """# Account Information (USER_DATA)
#### `GET /api/v3/account (HMAC SHA256)`
Get current account information.
### Weight:
10
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

<strong>Data Source:</strong>    """
    endpoint = '/api/v3/account'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getAccTrades(symbol, startTime="", endTime="", fromId="", limit="", recvWindow=""):
    """# Account Trade List (USER_DATA)
#### `GET /api/v3/myTrades  (HMAC SHA256)`
Get trades for a specific account and symbol.
### Weight:
10
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
fromId	|LONG	|NO	|TradeId to fetch from. Default gets most recent trades.
limit	|INT	|NO	|Default 500; max 1000.
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|

<strong>Notes:</strong><strong>Data Source:</strong>    """
    endpoint = '/api/v3/myTrades'
    params = {
        "symbol": symbol
    }
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if fromId: params["fromId"] = fromId
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                             Margin Account/Trade

# ------------------------------------------------------------------------------

def crossMargAccTransfer(asset, amount, type, recvWindow=""):
    """# Cross Margin Account Transfer (MARGIN)
#### `POST /sapi/v1/margin/transfer (HMAC SHA256)`
Execute transfer between spot account and cross margin account.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|The asset being transferred, e.g., BTC
amount	|DECIMAL	|YES	|The amount to be transferred
type	|INT	|YES	|1: transfer from main account to cross margin account 2: transfer from cross margin account to main account
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/transfer'
    params = {
        "asset": asset,
        "amount": amount,
        "type": type
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def margAccBorrow(asset, amount, isIsolated="", symbol="", recvWindow=""):
    """# Margin Account Borrow (MARGIN)
#### `POST /sapi/v1/margin/loan (HMAC SHA256)`
Apply for a loan.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
symbol	|STRING	|NO	|isolated symbol
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/loan'
    params = {
        "asset": asset,
        "amount": amount
    }
    if isIsolated: params["isIsolated"] = isIsolated
    if symbol: params["symbol"] = symbol
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def margAccRepay(asset, amount, isIsolated="", symbol="", recvWindow=""):
    """# Margin Account Repay (MARGIN)
#### `POST /sapi/v1/margin/repay (HMAC SHA256)`
Repay loan for margin account.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
symbol	|STRING	|NO	|isolated symbol
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/repay'
    params = {
        "asset": asset,
        "amount": amount
    }
    if isIsolated: params["isIsolated"] = isIsolated
    if symbol: params["symbol"] = symbol
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def queryMargAsset(asset):
    """# Query Margin Asset (MARKET_DATA)
#### `GET /sapi/v1/margin/asset `

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
    """
    endpoint = '/sapi/v1/margin/asset'
    params = {
        "asset": asset
    }


    return getbinancedata(endpoint, params)


def queryCrossMargPair(symbol):
    """# Query Cross Margin Pair (MARKET_DATA)
#### `GET /sapi/v1/margin/pair `

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
    """
    endpoint = '/sapi/v1/margin/pair'
    params = {
        "symbol": symbol
    }


    return getbinancedata(endpoint, params)


def getAllMargAssets():
    """# Get All Margin Assets (MARKET_DATA)
#### `GET /sapi/v1/margin/allAssets`
None
### Weight:
1
### Parameters:
NONE    """
    endpoint = '/sapi/v1/margin/allAssets'
    params = {

    }


    return getbinancedata(endpoint, params)


def getAllCrossMargPairs():
    """# Get All Cross Margin Pairs (MARKET_DATA)
#### `GET /sapi/v1/margin/allPairs `
None
### Weight:
1
### Parameters:
NONE    """
    endpoint = '/sapi/v1/margin/allPairs'
    params = {

    }


    return getbinancedata(endpoint, params)


def queryMargPriceIndex(symbol):
    """# Query Margin PriceIndex (MARKET_DATA)
#### `GET /sapi/v1/margin/priceIndex `

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
    """
    endpoint = '/sapi/v1/margin/priceIndex'
    params = {
        "symbol": symbol
    }


    return getbinancedata(endpoint, params)


def margAccNewOrder(symbol, side, type, isIsolated="", quantity="", quoteOrderQty="", price="", stopPrice="", newClientOrderId="", icebergQty="", newOrderRespType="", sideEffectType="", timeInForce="", recvWindow=""):
    """# Margin Account New Order (TRADE)
#### `POST /sapi/v1/margin/order (HMAC SHA256)`
Post a new order for margin account.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
side	|ENUM	|YES	|BUY<br/>SELL
type	|ENUM	|YES	|
quantity	|DECIMAL	|NO	|
quoteOrderQty	|DECIMAL	|NO	|
price	|DECIMAL	|NO	|
stopPrice	|DECIMAL	|NO	|Used with <code>STOP_LOSS</code>, <code>STOP_LOSS_LIMIT</code>, <code>TAKE_PROFIT</code>, and <code>TAKE_PROFIT_LIMIT</code> orders.
newClientOrderId	|STRING	|NO	|A unique id among open orders. Automatically generated if not sent.
icebergQty	|DECIMAL	|NO	|Used with <code>LIMIT</code>, <code>STOP_LOSS_LIMIT</code>, and <code>TAKE_PROFIT_LIMIT</code> to create an iceberg order.
newOrderRespType	|ENUM	|NO	|Set the response JSON. ACK, RESULT, or FULL; MARKET and LIMIT order types default to FULL, all other orders default to ACK.
sideEffectType	|ENUM	|NO	|NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; default NO_SIDE_EFFECT.
timeInForce	|ENUM	|NO	|GTC,IOC,FOK
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/order'
    params = {
        "symbol": symbol,
        "side": side,
        "type": type
    }
    if isIsolated: params["isIsolated"] = isIsolated
    if quantity: params["quantity"] = quantity
    if quoteOrderQty: params["quoteOrderQty"] = quoteOrderQty
    if price: params["price"] = price
    if stopPrice: params["stopPrice"] = stopPrice
    if newClientOrderId: params["newClientOrderId"] = newClientOrderId
    if icebergQty: params["icebergQty"] = icebergQty
    if newOrderRespType: params["newOrderRespType"] = newOrderRespType
    if sideEffectType: params["sideEffectType"] = sideEffectType
    if timeInForce: params["timeInForce"] = timeInForce
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def margAccCancelOrder(symbol, isIsolated="", orderId="", origClientOrderId="", newClientOrderId="", recvWindow=""):
    """# Margin Account Cancel Order (TRADE)
#### `DELETE /sapi/v1/margin/order (HMAC SHA256)`
Cancel an active order for margin account.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
orderId	|LONG	|NO	|
origClientOrderId	|STRING	|NO	|
newClientOrderId	|STRING	|NO	|Used to uniquely identify this cancel. Automatically generated by default.
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = 'DELETE /sapi/v1/margin/order'
    params = {
        "symbol": symbol
    }
    if isIsolated: params["isIsolated"] = isIsolated
    if orderId: params["orderId"] = orderId
    if origClientOrderId: params["origClientOrderId"] = origClientOrderId
    if newClientOrderId: params["newClientOrderId"] = newClientOrderId
    if recvWindow: params["recvWindow"] = recvWindow

    return deletebinancedata_sig(endpoint, params)


def margAccCancelAllOpenOrdersOnSymbol(symbol, isIsolated="", recvWindow=""):
    """# Margin Account Cancel all Open Orders on a Symbol (TRADE)
#### `DELETE /sapi/v1/margin/openOrders (HMAC SHA256)`
Cancels all active orders on a symbol for margin account.<br/>
This includes OCO orders.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = 'DELETE /sapi/v1/margin/openOrders'
    params = {
        "symbol": symbol
    }
    if isIsolated: params["isIsolated"] = isIsolated
    if recvWindow: params["recvWindow"] = recvWindow

    return deletebinancedata_sig(endpoint, params)


def getCrossMargTransferHistory(asset="", type="", startTime="", endTime="", current="", size="", archived="", recvWindow=""):
    """# Get Cross Margin Transfer History (USER_DATA)
#### `GET /sapi/v1/margin/transfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|No	|
type	|STRING	|NO	|Transfer Type: ROLL_IN, ROLL_OUT
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10 Max:100
archived	|STRING	|NO	|Default: <code>false</code>. Set to <code>true</code> for archived data from 6 months ago
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/transfer'
    params = {

    }
    if asset: params["asset"] = asset
    if type: params["type"] = type
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if archived: params["archived"] = archived
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryLoanRecord(asset, isolatedSymbol="", txId="", startTime="", endTime="", current="", size="", archived="", recvWindow=""):
    """# Query Loan Record (USER_DATA)
#### `GET /sapi/v1/margin/loan (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
isolatedSymbol	|STRING	|NO	|isolated symbol
txId	|LONG	|NO	|the tranId in POST /sapi/v1/margin/loan
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10 Max:100
archived	|STRING	|NO	|Default: <code>false</code>. Set to <code>true</code> for archived data from 6 months ago
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/loan'
    params = {
        "asset": asset
    }
    if isolatedSymbol: params["isolatedSymbol"] = isolatedSymbol
    if txId: params["txId"] = txId
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if archived: params["archived"] = archived
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryRepayRecord(asset, isolatedSymbol="", txId="", startTime="", endTime="", current="", size="", archived="", recvWindow=""):
    """# Query Repay Record (USER_DATA)
#### `GET /sapi/v1/margin/repay (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
isolatedSymbol	|STRING	|NO	|isolated symbol
txId	|LONG	|NO	|return of /sapi/v1/margin/repay
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10 Max:100
archived	|STRING	|NO	|Default: <code>false</code>. Set to <code>true</code> for archived data from 6 months ago
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/repay'
    params = {
        "asset": asset
    }
    if isolatedSymbol: params["isolatedSymbol"] = isolatedSymbol
    if txId: params["txId"] = txId
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if archived: params["archived"] = archived
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getInterestHistory(asset="", isolatedSymbol="", startTime="", endTime="", current="", size="", archived="", recvWindow=""):
    """# Get Interest History (USER_DATA)
#### `GET /sapi/v1/margin/interestHistory (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|NO	|
isolatedSymbol	|STRING	|NO	|isolated symbol
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10 Max:100
archived	|STRING	|NO	|Default: <code>false</code>. Set to <code>true</code> for archived data from 6 months ago
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/interestHistory'
    params = {

    }
    if asset: params["asset"] = asset
    if isolatedSymbol: params["isolatedSymbol"] = isolatedSymbol
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if archived: params["archived"] = archived
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getForceLiquidationRecord(startTime="", endTime="", isolatedSymbol="", current="", size="", recvWindow=""):
    """# Get Force Liquidation Record (USER_DATA)
#### `GET /sapi/v1/margin/forceLiquidationRec (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
isolatedSymbol	|STRING	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10 Max:100
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/forceLiquidationRec'
    params = {

    }
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if isolatedSymbol: params["isolatedSymbol"] = isolatedSymbol
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryCrossMargAccDetails(recvWindow=""):
    """# Query Cross Margin Account Details (USER_DATA)
#### `GET /sapi/v1/margin/account (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/account'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryMargAccOrder(symbol, isIsolated="", orderId="", origClientOrderId="", recvWindow=""):
    """# Query Margin Account's Order (USER_DATA)
#### `GET /sapi/v1/margin/order (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
orderId	|STRING	|NO	|
origClientOrderId	|STRING	|NO	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/order'
    params = {
        "symbol": symbol
    }
    if isIsolated: params["isIsolated"] = isIsolated
    if orderId: params["orderId"] = orderId
    if origClientOrderId: params["origClientOrderId"] = origClientOrderId
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryMargAccOpenOrders(symbol="", isIsolated="", recvWindow=""):
    """# Query Margin Account's Open Orders (USER_DATA)
#### `GET /sapi/v1/margin/openOrders (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|NO	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/openOrders'
    params = {

    }
    if symbol: params["symbol"] = symbol
    if isIsolated: params["isIsolated"] = isIsolated
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryMargAccAllOrders(symbol, isIsolated="", orderId="", startTime="", endTime="", limit="", recvWindow=""):
    """# Query Margin Account's All Orders (USER_DATA)
#### `GET /sapi/v1/margin/allOrders (HMAC SHA256)`
<strong>Request Limit</strong><br/>
60times/min per IP
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
isIsolated	|STRING	|NO	|for isolated margin or not, "TRUE", "FALSE"，default "FALSE"
orderId	|LONG	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|Default 500; max 500.
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/allOrders'
    params = {
        "symbol": symbol
    }
    if isIsolated: params["isIsolated"] = isIsolated
    if orderId: params["orderId"] = orderId
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryMaxBorrow(asset, isolatedSymbol="", recvWindow=""):
    """# Query Max Borrow (USER_DATA)
#### `GET /sapi/v1/margin/maxBorrowable (HMAC SHA256)`

### Weight:
5
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
isolatedSymbol	|STRING	|NO	|isolated symbol
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/maxBorrowable'
    params = {
        "asset": asset
    }
    if isolatedSymbol: params["isolatedSymbol"] = isolatedSymbol
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryMaxTransferOutAmount(asset, isolatedSymbol="", recvWindow=""):
    """# Query Max Transfer-Out Amount (USER_DATA)
#### `GET /sapi/v1/margin/maxTransferable (HMAC SHA256)`

### Weight:
5
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
isolatedSymbol	|STRING	|NO	|isolated symbol
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/maxTransferable'
    params = {
        "asset": asset
    }
    if isolatedSymbol: params["isolatedSymbol"] = isolatedSymbol
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def isolatedMargAccTransfer(asset, symbol, transFrom, transTo, amount, recvWindow=""):
    """# Isolated Margin Account Transfer (MARGIN)
#### `POST /sapi/v1/margin/isolated/transfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|asset,such as BTC
symbol	|STRING	|YES	|
transFrom	|STRING	|YES	|"SPOT", "ISOLATED_MARGIN"
transTo	|STRING	|YES	|"SPOT", "ISOLATED_MARGIN"
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/isolated/transfer'
    params = {
        "asset": asset,
        "symbol": symbol,
        "transFrom": transFrom,
        "transTo": transTo,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getIsolatedMargTransferHistory(symbol, asset="", transFrom="", transTo="", startTime="", endTime="", current="", size="", recvWindow=""):
    """# Get Isolated Margin Transfer History (USER_DATA)
#### `GET /sapi/v1/margin/isolated/transfer (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|NO	|
symbol	|STRING	|YES	|
transFrom	|STRING	|NO	|"SPOT", "ISOLATED_MARGIN"
transTo	|STRING	|NO	|"SPOT", "ISOLATED_MARGIN"
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Current page, default 1
size	|LONG	|NO	|Default 10, max 100
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/isolated/transfer'
    params = {
        "symbol": symbol
    }
    if asset: params["asset"] = asset
    if transFrom: params["transFrom"] = transFrom
    if transTo: params["transTo"] = transTo
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryIsolatedMargAccInfo(symbols="", recvWindow=""):
    """# Query Isolated Margin Account Info (USER_DATA)
#### `GET /sapi/v1/margin/isolated/account (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbols	|STRING	|NO	|Max 5 symbols can be sent; separated by ",". e.g. "BTCUSDT,BNBUSDT,ADAUSDT"
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/isolated/account'
    params = {

    }
    if symbols: params["symbols"] = symbols
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryIsolatedMargSymbol(symbol, recvWindow=""):
    """# Query Isolated Margin Symbol (USER_DATA)
#### `GET /sapi/v1/margin/isolated/pair (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
symbol	|STRING	|YES	|
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/isolated/pair'
    params = {
        "symbol": symbol
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getAllIsolatedMargSymbol(recvWindow=""):
    """# Get All Isolated Margin Symbol(USER_DATA)
#### `GET /sapi/v1/margin/isolated/allPairs (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/isolated/allPairs'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def toggleBNBBurnOnSpotTradeAndMargInterest(spotBNBBurn="", interestBNBBurn="", recvWindow=""):
    """# Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
#### `POST /sapi/v1/bnbBurn (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
spotBNBBurn	|STRING	|NO	|"true" or "false"; Determines whether to use BNB to pay for trading fees on SPOT
interestBNBBurn	|STRING	|NO	|"true" or "false"; Determines whether to use BNB to pay for margin loan's interest 
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/bnbBurn'
    params = {

    }
    if spotBNBBurn: params["spotBNBBurn"] = spotBNBBurn
    if interestBNBBurn: params["interestBNBBurn"] = interestBNBBurn
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getBNBBurnStatus(recvWindow=""):
    """# Get BNB Burn Status (USER_DATA)
#### `GET /sapi/v1/bnbBurn (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/bnbBurn'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def queryMargInterestRateHistory(asset, vipLevel="", startTime="", endTime="", limit="", recvWindow=""):
    """# Query Margin Interest Rate History (USER_DATA)
#### `GET /sapi/v1/margin/interestRateHistory (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
vipLevel	|INT	|NO	|Default: user's vip level
startTime	|LONG	|NO	|Default: 7 days ago
endTime	|LONG	|NO	|Default: present. Maximum range: 3 months.
limit	|INT	|NO	|Default: 20. Maximum: 100
recvWindow	|LONG	|NO	|No more than 60000
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/margin/interestRateHistory'
    params = {
        "asset": asset
    }
    if vipLevel: params["vipLevel"] = vipLevel
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                              Savings Endpoints

# ------------------------------------------------------------------------------

def getFlexibleProductList(status="", featured="", current="", size="", recvWindow=""):
    """# Get Flexible Product List (USER_DATA)
#### `GET /sapi/v1/lending/daily/product/list (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
status	|ENUM	|NO	|"ALL", "SUBSCRIBABLE", "UNSUBSCRIBABLE"; Default: "ALL"
featured	|STRING	|NO	|"ALL", "TRUE"; Default: "ALL"
current	|LONG	|NO	|Current query page. Default: 1, Min: 1
size	|LONG	|NO	|Default: 50, Max: 100
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/daily/product/list'
    params = {

    }
    if status: params["status"] = status
    if featured: params["featured"] = featured
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getLeftDailyPurchaseQuotaOfFlexibleProduct(productId, recvWindow=""):
    """# Get Left Daily Purchase Quota of Flexible Product (USER_DATA)
#### `GET /sapi/v1/lending/daily/userLeftQuota (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
productId	|STRING	|YES	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/daily/userLeftQuota'
    params = {
        "productId": productId
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def purchaseFlexibleProduct(productId, amount, recvWindow=""):
    """# Purchase Flexible Product (USER_DATA)
#### `POST /sapi/v1/lending/daily/purchase (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
productId	|STRING	|YES	|
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/daily/purchase'
    params = {
        "productId": productId,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getLeftDailyRedemptionQuotaOfFlexibleProduct(productId, type, recvWindow=""):
    """# Get Left Daily Redemption Quota of Flexible Product (USER_DATA)
#### `GET /sapi/v1/lending/daily/userRedemptionQuota (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
productId	|STRING	|YES	|
type	|ENUM	|YES	|"FAST", "NORMAL"
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/daily/userRedemptionQuota'
    params = {
        "productId": productId,
        "type": type
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def redeemFlexibleProduct(productId, amount, type, recvWindow=""):
    """# Redeem Flexible Product (USER_DATA)
#### `POST /sapi/v1/lending/daily/redeem (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
productId	|STRING	|YES	|
amount	|DECIMAL	|YES	|
type	|ENUM	|YES	|"FAST", "NORMAL"
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/daily/redeem'
    params = {
        "productId": productId,
        "amount": amount,
        "type": type
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getFlexibleProductPosition(asset, recvWindow=""):
    """# Get Flexible Product Position (USER_DATA)
#### `GET /sapi/v1/lending/daily/token/position (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/daily/token/position'
    params = {
        "asset": asset
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getFixedAndActivityProjectList(type, asset="", status="", isSortAsc="", sortBy="", current="", size="", recvWindow=""):
    """# Get Fixed and Activity Project List(USER_DATA)
#### `GET /sapi/v1/lending/project/list (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|NO	|
type	|ENUM	|YES	|"ACTIVITY", "CUSTOMIZED_FIXED"
status	|ENUM	|NO	|"ALL", "SUBSCRIBABLE", "UNSUBSCRIBABLE"; default "ALL"
isSortAsc	|BOOLEAN	|NO	|default "true"
sortBy	|ENUM	|NO	|"START_TIME", "LOT_SIZE", "INTEREST_RATE", "DURATION"; default "START_TIME"
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10, Max:100
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/project/list'
    params = {
        "type": type
    }
    if asset: params["asset"] = asset
    if status: params["status"] = status
    if isSortAsc: params["isSortAsc"] = isSortAsc
    if sortBy: params["sortBy"] = sortBy
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def purchaseFixedAndActivityProject(projectId, lot, recvWindow=""):
    """# Purchase Fixed/Activity Project  (USER_DATA)
#### `POST /sapi/v1/lending/customizedFixed/purchase (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
projectId	|STRING	|YES	|
lot	|LONG	|YES	|
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/customizedFixed/purchase'
    params = {
        "projectId": projectId,
        "lot": lot
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getFixedAndActivityProjectPosition(asset, projectId="", status="", recvWindow=""):
    """# Get Fixed/Activity Project Position (USER_DATA)
#### `GET /sapi/v1/lending/project/position/list (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
projectId	|STRING	|NO	|
status	|ENUM	|NO	|"HOLDING", "REDEEMED"
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/project/position/list'
    params = {
        "asset": asset
    }
    if projectId: params["projectId"] = projectId
    if status: params["status"] = status
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def lendingAcc(recvWindow=""):
    """# Lending Account (USER_DATA)
#### `GET /sapi/v1/lending/union/account (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/union/account'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getPurchaseRecord(lendingType, asset="", startTime="", endTime="", current="", size="", recvWindow=""):
    """# Get Purchase Record (USER_DATA)
#### `GET /sapi/v1/lending/union/purchaseRecord (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
lendingType	|ENUM	|YES	|"DAILY" for flexible, "ACTIVITY" for activity, "CUSTOMIZED_FIXED" for fixed
asset	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10, Max:100
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/union/purchaseRecord'
    params = {
        "lendingType": lendingType
    }
    if asset: params["asset"] = asset
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getRedemptionRecord(lendingType, asset="", startTime="", endTime="", current="", size="", recvWindow=""):
    """# Get Redemption Record (USER_DATA)
#### `GET /sapi/v1/lending/union/redemptionRecord (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
lendingType	|ENUM	|YES	|"DAILY" for flexible, "ACTIVITY" for activity, "CUSTOMIZED_FIXED" for fixed
asset	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10, Max:100
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/union/redemptionRecord'
    params = {
        "lendingType": lendingType
    }
    if asset: params["asset"] = asset
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getInterestHistory(lendingType, asset="", startTime="", endTime="", current="", size="", recvWindow=""):
    """# Get Interest History (USER_DATA)
#### `GET /sapi/v1/lending/union/interestHistory (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
lendingType	|ENUM	|YES	|"DAILY" for flexible, "ACTIVITY" for activity, "CUSTOMIZED_FIXED" for fixed
asset	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10, Max:100
recvWindow	|LONG	|NO	|The value cannot be greater than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/union/interestHistory'
    params = {
        "lendingType": lendingType
    }
    if asset: params["asset"] = asset
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def changeFixedAndActivityPositionToDailyPosition(projectId, lot, positionId="", recvWindow=""):
    """# Change Fixed/Activity Position to Daily Position(USER_DATA)
#### `POST /sapi/v1/lending/positionChanged (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
projectId	|STRING	|YES	|
lot	|LONG	|YES	|
positionId	|LONG	|NO	|for fixed position
recvWindow	|LONG	|NO	|no more than <code>60000</code>
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/lending/positionChanged'
    params = {
        "projectId": projectId,
        "lot": lot
    }
    if positionId: params["positionId"] = positionId
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                               Mining Endpoints

# ------------------------------------------------------------------------------

def miningAcquiringAlgorithm():
    """# Acquiring Algorithm (USER_DATA)
#### `GET /sapi/v1/mining/pub/algoList (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:<br/>
1
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/pub/algoList'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def miningAcquiringCoinName():
    """# Acquiring CoinName (USER_DATA)
#### `GET /sapi/v1/mining/pub/coinList (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:<br/>
1
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/pub/coinList'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def requestForDetailMinerList():
    """# Request for Detail Miner List (USER_DATA)
#### `GET /sapi/v1/mining/worker/detail  (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/worker/detail'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def requestForMinerList():
    """# Request for Miner List (USER_DATA)
#### `GET /sapi/v1/mining/worker/list  (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/worker/list'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def miningEarningsList():
    """# Earnings List(USER_DATA)
#### `GET /sapi/v1/mining/payment/list  (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/payment/list'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def miningExtraBonusList():
    """# Extra Bonus List (USER_DATA)
#### `GET /sapi/v1/mining/payment/other  (HMAC SHA256)`
<strong>Parameter:</strong>
### Weights:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/payment/other'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def hashrateResaleList():
    """# Hashrate Resale List (USER_DATA)
#### `GET /sapi/v1/mining/hash-transfer/config/details/list  (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/hash-transfer/config/details/list'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def hashrateResaleDetail():
    """# Hashrate Resale Detail (USER_DATA)
#### `GET /sapi/v1/mining/hash-transfer/profit/details (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/hash-transfer/profit/details'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def hashrateResaleRequest():
    """# Hashrate Resale Request (USER_DATA)
#### `POST /sapi/v1/mining/hash-transfer/config (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/hash-transfer/config'
    params = {

    }


    return postbinancedata_sig(endpoint, params)


def cancelHashrateResaleConfiguration():
    """# Cancel hashrate resale configuration(USER_DATA)
#### `POST /sapi/v1/mining/hash-transfer/config/cancel (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/hash-transfer/config/cancel'
    params = {

    }


    return postbinancedata_sig(endpoint, params)


def miningStatisticList():
    """# Statistic List (USER_DATA)
#### `GET /sapi/v1/mining/statistics/user/status (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/statistics/user/status'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def miningAccList():
    """# Account List (USER_DATA)
#### `GET /sapi/v1/mining/statistics/user/list (HMAC SHA256)`
<strong>Parameter:</strong>
### Weight:
5
### Parameters:
NONE    """
    endpoint = '/sapi/v1/mining/statistics/user/list'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                                   Futures

# ------------------------------------------------------------------------------

def newFutureAccountTransfer(asset, amount, type, recvWindow=""):
    """# New Future Account Transfer (USER_DATA)
#### `POST /sapi/v1/futures/transfer  (HMAC SHA256)`
Execute transfer between spot account and futures account.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|The asset being transferred, e.g., USDT
amount	|DECIMAL	|YES	|The amount to be transferred
type	|INT	|YES	|<strong>1:</strong> transfer from spot account to USDT-Ⓜ futures account.<br> <strong>2:</strong> transfer from USDT-Ⓜ futures account to spot account. <br><strong>3:</strong> transfer from spot account to COIN-Ⓜ futures account. <br><strong>4:</strong> transfer from COIN-Ⓜ futures account to spot account.</br></br></br>
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/futures/transfer'
    params = {
        "asset": asset,
        "amount": amount,
        "type": type
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getFutureAccountTransactionHistoryList(asset, startTime, endTime="", current="", size="", recvWindow=""):
    """# Get Future Account Transaction History List (USER_DATA)
#### `GET /sapi/v1/futures/transfer (HMAC SHA256)`

### Weight:
5
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
asset	|STRING	|YES	|
startTime	|LONG	|YES	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
size	|LONG	|NO	|Default:10 Max:100
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/futures/transfer'
    params = {
        "asset": asset,
        "startTime": startTime
    }
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if size: params["size"] = size
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def borrowForCrossCollateral(coin, collateralCoin, amount="", collateralAmount="", recvWindow=""):
    """# Borrow For Cross-Collateral (TRADE)
#### `POST /sapi/v1/futures/loan/borrow (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|YES	|
amount	|DECIMAL	|YES when collateralAmount is empty	|
collateralCoin	|STRING	|YES	|
collateralAmount	|DECIMAL	|YES when amount is empty	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Rate Limit:</strong>    """
    endpoint = '/sapi/v1/futures/loan/borrow'
    params = {
        "coin": coin,
        "collateralCoin": collateralCoin
    }
    if amount: params["amount"] = amount
    if collateralAmount: params["collateralAmount"] = collateralAmount
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def crossCollateralBorrowHistory(coin="", startTime="", endTime="", limit="", recvWindow=""):
    """# Cross-Collateral Borrow History (USER_DATA)
#### `GET /sapi/v1/futures/loan/borrow/history (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|LONG	|NO	|default 500, max 1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/borrow/history'
    params = {

    }
    if coin: params["coin"] = coin
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def repayForCrossCollateral(coin, collateralCoin, amount, recvWindow=""):
    """# Repay For Cross-Collateral (TRADE)
#### `POST /sapi/v1/futures/loan/repay (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|YES	|
collateralCoin	|STRING	|YES	|
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Rate Limit:</strong>1/1s per account    """
    endpoint = '/sapi/v1/futures/loan/repay'
    params = {
        "coin": coin,
        "collateralCoin": collateralCoin,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def crossCollateralRepaymentHistory(coin="", startTime="", endTime="", limit="", recvWindow=""):
    """# Cross-Collateral Repayment History (USER_DATA)
#### `GET /sapi/v1/futures/loan/repay/history HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|LONG	|NO	|default 500, max 1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/repay/history HMAC SHA256)'
    params = {

    }
    if coin: params["coin"] = coin
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def crossCollateralWallet(recvWindow=""):
    """# Cross-Collateral Wallet (USER_DATA)
#### `GET /sapi/v1/futures/loan/wallet (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/wallet'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def crossCollateralWalletV2(recvWindow=""):
    """# Cross-Collateral Wallet V2 (USER_DATA)
#### `GET /sapi/v2/futures/loan/wallet (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v2/futures/loan/wallet'
    params = {

    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def crossCollateralInformation(collateralCoin="", recvWindow=""):
    """# Cross-Collateral Information (USER_DATA)
#### `GET /sapi/v1/futures/loan/configs (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
collateralCoin	|STRING	|NO	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/configs'
    params = {

    }
    if collateralCoin: params["collateralCoin"] = collateralCoin
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def crossCollateralInformation_V2(loanCoin="", collateralCoin="", recvWindow=""):
    """# Cross-Collateral Information V2 (USER_DATA)
#### `GET /sapi/v2/futures/loan/configs (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
loanCoin	|STRING	|NO	|
collateralCoin	|STRING	|NO	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v2/futures/loan/configs'
    params = {

    }
    if loanCoin: params["loanCoin"] = loanCoin
    if collateralCoin: params["collateralCoin"] = collateralCoin
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def calculateRateAfterAdjustCrossCollateralLTV(collateralCoin, amount, direction, recvWindow=""):
    """# Calculate Rate After Adjust Cross-Collateral LTV (USER_DATA)
#### `GET /sapi/v1/futures/loan/calcAdjustLevel (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
collateralCoin	|STRING	|YES	|
amount	|DECIMAL	|YES	|
direction	|ENUM	|YES	|"ADDITIONAL", "REDUCED"
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/calcAdjustLevel'
    params = {
        "collateralCoin": collateralCoin,
        "amount": amount,
        "direction": direction
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def calculateRateAfterAdjustCrossCollateralLTV_V2(loanCoin, collateralCoin, amount, direction, recvWindow=""):
    """# Calculate Rate After Adjust Cross-Collateral LTV V2 (USER_DATA)
#### `GET /sapi/v2/futures/loan/calcAdjustLevel (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
loanCoin	|STRING	|YES	|
collateralCoin	|STRING	|YES	|
amount	|DECIMAL	|YES	|
direction	|ENUM	|YES	|"ADDITIONAL", "REDUCED"
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v2/futures/loan/calcAdjustLevel'
    params = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        "amount": amount,
        "direction": direction
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getMaxAmountForAdjustCrossCollateralLTV(collateralCoin, recvWindow=""):
    """# Get Max Amount for Adjust Cross-Collateral LTV (USER_DATA)
#### `GET /sapi/v1/futures/loan/calcMaxAdjustAmount (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
collateralCoin	|STRING	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/calcMaxAdjustAmount'
    params = {
        "collateralCoin": collateralCoin
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getMaxAmountForAdjustCrossCollateralLTV_V2(loanCoin, collateralCoin, recvWindow=""):
    """# Get Max Amount for Adjust Cross-Collateral LTV V2 (USER_DATA)
#### `GET /sapi/v2/futures/loan/calcMaxAdjustAmount (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
loanCoin	|STRING	|YES	|
collateralCoin	|STRING	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v2/futures/loan/calcMaxAdjustAmount'
    params = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def adjustCrossCollateralLTV(collateralCoin, amount, direction, recvWindow=""):
    """# Adjust Cross-Collateral LTV (TRADE)
#### `POST /sapi/v1/futures/loan/adjustCollateral (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
collateralCoin	|STRING	|YES	|
amount	|DECIMAL	|YES	|
direction	|ENUM	|YES	|"ADDITIONAL", "REDUCED"
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>RateLimit:</strong>    """
    endpoint = '/sapi/v1/futures/loan/adjustCollateral'
    params = {
        "collateralCoin": collateralCoin,
        "amount": amount,
        "direction": direction
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def adjustCrossCollateralLTV_V2(loanCoin, collateralCoin, amount, direction, recvWindow=""):
    """# Adjust Cross-Collateral LTV V2 (TRADE)
#### `POST /sapi/v2/futures/loan/adjustCollateral (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
loanCoin	|STRING	|YES	|
collateralCoin	|STRING	|YES	|
amount	|DECIMAL	|YES	|
direction	|ENUM	|YES	|"ADDITIONAL", "REDUCED"
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>RateLimit:</strong>    """
    endpoint = '/sapi/v2/futures/loan/adjustCollateral'
    params = {
        "loanCoin": loanCoin,
        "collateralCoin": collateralCoin,
        "amount": amount,
        "direction": direction
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def adjustCrossCollateralLTVHistory(loanCoin="", collateralCoin="", startTime="", endTime="", limit="", recvWindow=""):
    """# Adjust Cross-Collateral LTV History (USER_DATA)
#### `GET /sapi/v1/futures/loan/adjustCollateral/history (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
loanCoin	|STRING	|NO	|
collateralCoin	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|LONG	|NO	|default 500, max 1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/adjustCollateral/history'
    params = {

    }
    if loanCoin: params["loanCoin"] = loanCoin
    if collateralCoin: params["collateralCoin"] = collateralCoin
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def crossCollateralLiquidationHistory(loanCoin="", collateralCoin="", startTime="", endTime="", limit="", recvWindow=""):
    """# Cross-Collateral Liquidation History (USER_DATA)
#### `GET /sapi/v1/futures/loan/liquidationHistory (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
loanCoin	|STRING	|NO	|
collateralCoin	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|LONG	|NO	|default 500, max 1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/liquidationHistory'
    params = {

    }
    if loanCoin: params["loanCoin"] = loanCoin
    if collateralCoin: params["collateralCoin"] = collateralCoin
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def checkCollateralRepayLimit(coin, collateralCoin, recvWindow=""):
    """# Check Collateral Repay Limit (USER_DATA)
#### `GET /sapi/v1/futures/loan/collateralRepayLimit (HMAC SHA256)`
Check the maximum and minimum limit when repay with collateral.
### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|YES	|
collateralCoin	|STRING	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/collateralRepayLimit'
    params = {
        "coin": coin,
        "collateralCoin": collateralCoin
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getCollateralRepayQuote(coin, collateralCoin, amount, recvWindow=""):
    """# Get Collateral Repay Quote (USER_DATA)
#### `GET /sapi/v1/futures/loan/collateralRepay (HMAC SHA256)`
Get quote before repay with collateral is mandatory, the quote will be valid within 25 seconds.
### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
coin	|STRING	|YES	|
collateralCoin	|STRING	|YES	|
amount	|DECIMAL	|YES	|repay amount
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/collateralRepay'
    params = {
        "coin": coin,
        "collateralCoin": collateralCoin,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def repayWithCollateral(quoteId, recvWindow=""):
    """# Repay with Collateral (USER_DATA)
#### `POST /sapi/v1/futures/loan/collateralRepay (HMAC SHA256)`
Repay with collateral. Get quote before repay with collateral is mandatory, the quote will be valid within 25 seconds.
### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
quoteId	|STRING	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/collateralRepay'
    params = {
        "quoteId": quoteId
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def collateralRepaymentResult(quoteId, recvWindow=""):
    """# Collateral Repayment Result (USER_DATA)
#### `GET /sapi/v1/futures/loan/collateralRepayResult (HMAC SHA256)`
Check collateral repayment result.
### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
quoteId	|STRING	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/collateralRepayResult'
    params = {
        "quoteId": quoteId
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def crossCollateralInterestHistory(collateralCoin="", startTime="", endTime="", current="", limit="", recvWindow=""):
    """# Cross-Collateral Interest History (USER_DATA)
#### `GET /sapi/v1/futures/loan/interestHistory (HMAC SHA256)`

### 
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
collateralCoin	|STRING	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
current	|LONG	|NO	|Currently querying page. Start from 1. Default:1
limit	|LONG	|NO	|Default:500 Max:1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|

<strong>Weight:</strong>    """
    endpoint = '/sapi/v1/futures/loan/interestHistory'
    params = {

    }
    if collateralCoin: params["collateralCoin"] = collateralCoin
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if current: params["current"] = current
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                                BLVT Endpoints

# ------------------------------------------------------------------------------

def getBLVTInfo(tokenName=""):
    """# Get BLVT Info (MARKET_DATA)
#### `GET /sapi/v1/blvt/tokenInfo`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
tokenName	|STRING	|NO	|BTCDOWN, BTCUP
    """
    endpoint = '/sapi/v1/blvt/tokenInfo'
    params = {

    }
    if tokenName: params["tokenName"] = tokenName

    return getbinancedata(endpoint, params)


def subscribeBLVT(tokenName, cost, recvWindow=""):
    """# Subscribe BLVT (USER_DATA)
#### `POST /sapi/v1/blvt/subscribe  (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
tokenName	|STRING	|YES	|BTCDOWN, BTCUP
cost	|DECIMAL	|YES	|spot balance
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/blvt/subscribe'
    params = {
        "tokenName": tokenName,
        "cost": cost
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def querySubscriptionRecord(tokenName="", id="", startTime="", endTime="", limit="", recvWindow=""):
    """# Query Subscription Record (USER_DATA)
#### `GET /sapi/v1/blvt/subscribe/record  (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
tokenName	|STRING	|NO	|BTCDOWN, BTCUP
id	|LONG	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|default 1000, max 1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/blvt/subscribe/record'
    params = {

    }
    if tokenName: params["tokenName"] = tokenName
    if id: params["id"] = id
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def redeemBLVT(tokenName, amount, recvWindow=""):
    """# Redeem BLVT (USER_DATA)
#### `POST /sapi/v1/blvt/redeem (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
tokenName	|STRING	|YES	|BTCDOWN, BTCUP
amount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/blvt/redeem'
    params = {
        "tokenName": tokenName,
        "amount": amount
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def queryRedemptionRecord(tokenName="", id="", startTime="", endTime="", limit="", recvWindow=""):
    """# Query Redemption Record (USER_DATA)
#### `GET /sapi/v1/blvt/redeem/record  (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
tokenName	|STRING	|NO	|BTCDOWN, BTCUP
id	|LONG	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|INT	|NO	|default 1000, max 1000
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/blvt/redeem/record'
    params = {

    }
    if tokenName: params["tokenName"] = tokenName
    if id: params["id"] = id
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getBLVTUserLimitInfo(tokenName="", recvWindow=""):
    """# Get BLVT User Limit Info (USER_DATA)
#### `GET /sapi/v1/blvt/userLimit  (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
tokenName	|STRING	|NO	|BTCDOWN, BTCUP
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/blvt/userLimit'
    params = {

    }
    if tokenName: params["tokenName"] = tokenName
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                               BSwap Endpoints

# ------------------------------------------------------------------------------

def listAllSwapPools():
    """# List All Swap Pools (MARKET_DATA)
#### `GET /sapi/v1/bswap/pools`
Get metadata about all swap pools.None
### Weight:
1
### Parameters:
NONE    """
    endpoint = '/sapi/v1/bswap/pools'
    params = {

    }


    return getbinancedata(endpoint, params)


def getLiquidityInformationOfAPool():
    """# Get liquidity information of a pool (USER_DATA)
#### `GET /sapi/v1/bswap/liquidity (HMAC SHA256)`
Get liquidity information and user share of a pool.<strong>1</strong> for one pool<strong>10</strong> when the poolId parameter is omitted<strong>Parameter:</strong>
### Weight:
### Parameters:
NONE    """
    endpoint = '/sapi/v1/bswap/liquidity'
    params = {

    }


    return getbinancedata_sig(endpoint, params)


def addLiquidity():
    """# Add Liquidity (TRADE)
#### `POST /sapi/v1/bswap/liquidityAdd (HMAC SHA256)`
Add liquidity to a pool.<strong>Parameter:</strong>
### Weight:
2
### Parameters:
NONE    """
    endpoint = '/sapi/v1/bswap/liquidityAdd'
    params = {

    }


    return postbinancedata_sig(endpoint, params)


def removeLiquidity(poolId, type, shareAmount, asset="", recvWindow=""):
    """# Remove Liquidity (TRADE)
#### `POST /sapi/v1/bswap/liquidityRemove (HMAC SHA256)`
Remove liquidity from a pool, `type` include `SINGLE` and `COMBINATION`, asset is mandatory for single asset removal
### Weight:
2
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
poolId	|LONG	|YES	|
type	|STRING	|YES	|<code>SINGLE</code> for single asset removal, <code>COMBINATION</code> for combination of all coins removal
asset	|LIST	|NO	|Mandatory for single asset removal
shareAmount	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/bswap/liquidityRemove'
    params = {
        "poolId": poolId,
        "type": type,
        "shareAmount": shareAmount
    }
    if asset: params["asset"] = asset
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getLiquidityOperationRecord(operationId="", poolId="", operation="", startTime="", endTime="", limit="", recvWindow=""):
    """# Get Liquidity Operation Record (USER_DATA)
#### `GET /sapi/v1/bswap/liquidityOps (HMAC SHA256)`
Get liquidity operation (add/remove) records.
### Weight:
2
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
operationId	|LONG	|NO	|
poolId	|LONG	|NO	|
operation	|ENUM	|NO	|<code>ADD</code> or <code>REMOVE</code>
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
limit	|LONG	|NO	|default 3, max 100
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/bswap/liquidityOps'
    params = {

    }
    if operationId: params["operationId"] = operationId
    if poolId: params["poolId"] = poolId
    if operation: params["operation"] = operation
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def requestQuote(quoteAsset, baseAsset, quoteQty, recvWindow=""):
    """# Request Quote (USER_DATA)
#### `GET /sapi/v1/bswap/quote (HMAC SHA256)`
Request a quote for swap quote asset (selling asset) for base asset (buying asset), essentially price/exchange rates.`quoteQty` is quantity of quote asset (to sell).Please be noted the quote is for reference only, the actual price will change as the liquidity changes, it's recommended to swap immediate after request a quote for slippage prevention.
### Weight:
2
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
quoteAsset	|STRING	|YES	|
baseAsset	|STRING	|YES	|
quoteQty	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/bswap/quote'
    params = {
        "quoteAsset": quoteAsset,
        "baseAsset": baseAsset,
        "quoteQty": quoteQty
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def swap(quoteAsset, baseAsset, quoteQty, recvWindow=""):
    """# Swap (TRADE)
#### `POST /sapi/v1/bswap/swap (HMAC SHA256)`
Swap `quoteAsset` for `baseAsset`.
### Weight:
2
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
quoteAsset	|STRING	|YES	|
baseAsset	|STRING	|YES	|
quoteQty	|DECIMAL	|YES	|
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/bswap/swap'
    params = {
        "quoteAsset": quoteAsset,
        "baseAsset": baseAsset,
        "quoteQty": quoteQty
    }
    if recvWindow: params["recvWindow"] = recvWindow

    return postbinancedata_sig(endpoint, params)


def getSwapHistory(swapId="", startTime="", endTime="", status="", quoteAsset="", baseAsset="", limit="", recvWindow=""):
    """# Get Swap History (USER_DATA)
#### `GET /sapi/v1/bswap/swap (HMAC SHA256)`
Get swap history.
### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
swapId	|LONG	|NO	|
startTime	|LONG	|NO	|
endTime	|LONG	|NO	|
status	|INT	|NO	|0: pending for swap, 1: success, 2: failed
quoteAsset	|STRING	|NO	|
baseAsset	|STRING	|NO	|
limit	|LONG	|NO	|default 3, max 100
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/bswap/swap'
    params = {

    }
    if swapId: params["swapId"] = swapId
    if startTime: params["startTime"] = startTime
    if endTime: params["endTime"] = endTime
    if status: params["status"] = status
    if quoteAsset: params["quoteAsset"] = quoteAsset
    if baseAsset: params["baseAsset"] = baseAsset
    if limit: params["limit"] = limit
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


# ------------------------------------------------------------------------------

#                                Fiat Endpoints

# ------------------------------------------------------------------------------

def getFiatDepositAndWithdrawHistory(transactionType, beginTime="", endTime="", page="", rows="", recvWindow=""):
    """# Get Fiat Deposit/Withdraw History (USER_DATA)
#### `GET /sapi/v1/fiat/orders (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
transactionType	|STRING	|YES	|0-deposit,1-withdraw
beginTime	|LONG	|NO	|
endTime	|LONG	|NO	|
page	|INT	|NO	|default 1
rows	|INT	|NO	|default 100, max 500
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/fiat/orders'
    params = {
        "transactionType": transactionType
    }
    if beginTime: params["beginTime"] = beginTime
    if endTime: params["endTime"] = endTime
    if page: params["page"] = page
    if rows: params["rows"] = rows
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


def getFiatPaymentsHistory(transactionType, beginTime="", endTime="", page="", rows="", recvWindow=""):
    """# Get Fiat Payments History (USER_DATA)
#### `GET /sapi/v1/fiat/payments (HMAC SHA256)`

### Weight:
1
### Parameters:

Name	|Type	|Mandatory	|Description
--------|--------|--------|--------
transactionType	|STRING	|YES	|0-buy,1-sell
beginTime	|LONG	|NO	|
endTime	|LONG	|NO	|
page	|INT	|NO	|default 1
rows	|INT	|NO	|default 100, max 500
recvWindow	|LONG	|NO	|
timestamp	|LONG	|YES	|
    """
    endpoint = '/sapi/v1/fiat/payments'
    params = {
        "transactionType": transactionType
    }
    if beginTime: params["beginTime"] = beginTime
    if endTime: params["endTime"] = endTime
    if page: params["page"] = page
    if rows: params["rows"] = rows
    if recvWindow: params["recvWindow"] = recvWindow

    return getbinancedata_sig(endpoint, params)


