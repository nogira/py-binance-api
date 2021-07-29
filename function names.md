# Wallet Endpoints
System Status (System)
`getSystemStatus`

All Coins' Information (USER_DATA)
`getAllCoinsInfo`

Daily Account Snapshot (USER_DATA)
`getAccSnapshot`

Disable Fast Withdraw Switch (USER_DATA)
`disableFastWithdraw`

Enable Fast Withdraw Switch (USER_DATA)
`enableFastWithdraw`

Withdraw(SAPI)
`withdrawCoin`

Deposit History(supporting network) (USER_DATA)
`getDepositHistory`

Withdraw History (supporting network) (USER_DATA)
`getWithdrawHistory`

Deposit Address (supporting network) (USER_DATA)
`getCoinDepositAddr`

Account Status (USER_DATA)
`getAccStatus`

Account API Trading Status (USER_DATA)
`getApiTradingStatus`

DustLog(USER_DATA)
`getDustHistory`

Dust Transfer (USER_DATA)
`convertToDust`

Asset Dividend Record (USER_DATA)
`getDividendHistory`

Asset Detail (USER_DATA)
`getAssetDetails`

Trade Fee (USER_DATA)
`getTradeFee`

User Universal Transfer
`transferWithin`

Query User Universal Transfer History
`getTransferWithinHistory`

Funding Wallet (USER_DATA)
`getFundingAsset`

Get API Key Permission (USER_DATA)
`getApiPermissions`

# Sub-Account Endpoints
Create a Virtual Sub-account(For Master Account)
`masterCreateSubacc`

Query Sub-account List (For Master Account)
`masterGetSubaccList`

Query Sub-account Spot Asset Transfer History (For Master Account)
`masterGetSpotSubaccToSubaccTransferHist`

Query Sub-account Futures Asset Transfer History (For Master Account)
`masterGetFutSubaccToSubaccTransferHist`

Sub-account Futures Asset Transfer (For Master Account)
`masterTransferFutFrmSubaccToSubacc`

Query Sub-account Assets (For Master Account)
`masterGetSubaccAssets`

Query Sub-account Spot Assets Summary (For Master Account)
`masterGetSubaccSpotAssets`

Get Sub-account Deposit Address (For Master Account)
`masterGetSubaccDepositAddr`

Get Sub-account Deposit History (For Master Account)
`masterGetSubaccDepositHistory`

Get Sub-account's Status on Margin/Futures (For Master Account)
`masterGetSubaccMargFutStatus`

Enable Margin for Sub-account (For Master Account)
`masterEnableMargSubacc`

Get Detail on Sub-account's Margin Account (For Master Account)
`masterGetSubaccMargDetails`

Get Summary of Sub-account's Margin Account (For Master Account)
`masterGetSubaccMargSumm`

Enable Futures for Sub-account (For Master Account)
`masterEnableFutSubacc`

Get Detail on Sub-account's Futures Account (For Master Account)
`masterGetSubaccFutDetails`

Get Summary of Sub-account's Futures Account (For Master Account)
`masterGetSubaccFutSumm`

Get Futures Position-Risk of Sub-account (For Master Account)
`masterGetSubaccFutPosRisk`

Futures Transfer for Sub-account (For Master Account)
`masterTransferFutWithinSubacc`

Margin Transfer for Sub-account (For Master Account)
`masterTransferMargWithinSubacc`

Transfer to Sub-account of Same Master (For Sub-account)
`subaccTransferToSubacc`

Transfer to Master (For Sub-account)
`subaccTransferToMaster`

Sub-account Transfer History (For Sub-account)
`subaccGetTransferHistory`

Universal Transfer (For Master Account)
`masterUniversalTransferSubacc`

Query Universal Transfer History (For Master Account)
`masterSubaccUniversalTransferHistory`

Get Detail on Sub-account's Futures Account V2 (For Master Account)
`masterGetSubaccFutDetailsv2`

Get Summary of Sub-account's Futures Account V2 (For Master Account)
`masterGetSubaccFutSummv2`

Get Futures Position-Risk of Sub-account V2 (For Master Account)
`masterGetSubaccFutPosRiskv2`

Enable Leverage Token for Sub-account  (For Master Account)
`masterEnableLeverageTokenInSubacc`

Deposit assets into the managed sub-account（For Investor Master Account）
`investorMasterDepositAssetToSubacc`

Query managed sub-account asset details（For Investor Master Account）
`investorMasterGetSubaccAssetDetails`

Withdrawl assets from the managed sub-account（For Investor Master Account）
`investorMasterWithdrawAssetFrmSubacc`

# Market Data Endpoints
Test Connectivity
`testConnectivity`

Check Server Time
`serverTime`

Exchange Information
`exchangeInfo`

Order Book
`getOrderBook`

Recent Trades List
`getRecentTrades`

Old Trade Lookup
`getOldTrades`

Compressed/Aggregate Trades List
`getCompressedTrades`

Kline/Candlestick Data
`getKline`

Current Average Price
`getCurrentAvgPrice`

24hr Ticker Price Change Statistics
`get24hrPriceStats`

Symbol Price Ticker
`getPrice`

Symbol Order Book Ticker
`getBestOrderBookPrice`

# Spot Acount/Trade
Test New Order (TRADE)
`testNewOrder`

New Order  (TRADE)
`newOrder`

Cancel Order (TRADE)
`cancelOrder`

Cancel all Open Orders on a Symbol (TRADE)
`cancelAllOpenOrdersOnSymbol`

Query Order (USER_DATA)
`getOrderStatus`

Current Open Orders (USER_DATA)
`getOpenOrders`

All Orders (USER_DATA)
`getAllOrders`

New OCO (TRADE)
`newOCO`

Cancel OCO (TRADE)
`cancelOCO`

Query OCO (USER_DATA)
`getOCOStaus`

Query all OCO (USER_DATA)
`getAllOCO`

Query Open OCO (USER_DATA)
`getOpenOCO`

Account Information (USER_DATA)
`getAccInfo`

Account Trade List (USER_DATA)
`getAccTrades`

# Margin Account/Trade
Cross Margin Account Transfer (MARGIN)
`crossMargAccTransfer`

Margin Account Borrow (MARGIN)
`margAccBorrow`

Margin Account Repay (MARGIN)
`margAccRepay`

Query Margin Asset (MARKET_DATA)
`queryMargAsset`

Query Cross Margin Pair (MARKET_DATA)
`queryCrossMargPair`

Get All Margin Assets (MARKET_DATA)
`getAllMargAssets`

Get All Cross Margin Pairs (MARKET_DATA)
`getAllCrossMargPairs`

Query Margin PriceIndex (MARKET_DATA)
`queryMargPriceIndex`

Margin Account New Order (TRADE)
`margAccNewOrder`

Margin Account Cancel Order (TRADE)
`margAccCancelOrder`

Margin Account Cancel all Open Orders on a Symbol (TRADE)
`margAccCancelAllOpenOrdersOnSymbol`

Get Cross Margin Transfer History (USER_DATA)
`getCrossMargTransferHistory`

Query Loan Record (USER_DATA)
`queryLoanRecord`

Query Repay Record (USER_DATA)
`queryRepayRecord`

Get Interest History (USER_DATA)
`getInterestHistory`

Get Force Liquidation Record (USER_DATA)
`getForceLiquidationRecord`

Query Cross Margin Account Details (USER_DATA)
`queryCrossMargAccDetails`

Query Margin Account's Order (USER_DATA)
`queryMargAccOrder`

Query Margin Account's Open Orders (USER_DATA)
`queryMargAccOpenOrders`

Query Margin Account's All Orders (USER_DATA)
`queryMargAccAllOrders`

Query Margin Account's Trade List (USER_DATA)
`queryMargAccTrades`

Query Max Borrow (USER_DATA)
`queryMaxBorrow`

Query Max Transfer-Out Amount (USER_DATA)
`queryMaxTransferOutAmount`

Isolated Margin Account Transfer (MARGIN)
`isolatedMargAccTransfer`

Get Isolated Margin Transfer History (USER_DATA)
`getIsolatedMargTransferHistory`

Query Isolated Margin Account Info (USER_DATA)
`queryIsolatedMargAccInfo`

Query Isolated Margin Symbol (USER_DATA)
`queryIsolatedMargSymbol`

Get All Isolated Margin Symbol(USER_DATA)
`getAllIsolatedMargSymbol`

Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
`toggleBNBBurnOnSpotTradeAndMargInterest`

Get BNB Burn Status (USER_DATA)
`getBNBBurnStatus`

Query Margin Interest Rate History (USER_DATA)
`queryMargInterestRateHistory`

# Savings Endpoints
Get Flexible Product List (USER_DATA)
`getFlexibleProductList`

Get Left Daily Purchase Quota of Flexible Product (USER_DATA)
`getLeftDailyPurchaseQuotaOfFlexibleProduct`

Purchase Flexible Product (USER_DATA)
`purchaseFlexibleProduct`

Get Left Daily Redemption Quota of Flexible Product (USER_DATA)
`getLeftDailyRedemptionQuotaOfFlexibleProduct`

Redeem Flexible Product (USER_DATA)
`redeemFlexibleProduct`

Get Flexible Product Position (USER_DATA)
`getFlexibleProductPosition`

Get Fixed and Activity Project List(USER_DATA)
`getFixedAndActivityProjectList`

Purchase Fixed/Activity Project  (USER_DATA)
`purchaseFixedAndActivityProject`

Get Fixed/Activity Project Position (USER_DATA)
`getFixedAndActivityProjectPosition`

Lending Account (USER_DATA)
`lendingAcc`

Get Purchase Record (USER_DATA)
`getPurchaseRecord`

Get Redemption Record (USER_DATA)
`getRedemptionRecord`

Get Interest History (USER_DATA)
`getInterestHistory`

Change Fixed/Activity Position to Daily Position(USER_DATA)
`changeFixedAndActivityPositionToDailyPosition`

# Mining Endpoints
Acquiring Algorithm (USER_DATA)
`miningAcquiringAlgorithm`

Acquiring CoinName (USER_DATA)
`miningAcquiringCoinName`

Request for Detail Miner List (USER_DATA)
`requestForDetailMinerList`

Request for Miner List (USER_DATA)
`requestForMinerList`

Earnings List(USER_DATA)
`miningEarningsList`

Extra Bonus List (USER_DATA)
`miningExtraBonusList`

Hashrate Resale List (USER_DATA)
`hashrateResaleList`

Hashrate Resale Detail (USER_DATA)
`hashrateResaleDetail`

Hashrate Resale Request (USER_DATA)
`hashrateResaleRequest`

Cancel hashrate resale configuration(USER_DATA)
`cancelHashrateResaleConfiguration`

Statistic List (USER_DATA)
`miningStatisticList`

Account List (USER_DATA)
`miningAccList`

# Futures
New Future Account Transfer (USER_DATA)
`newFutureAccountTransfer`

Get Future Account Transaction History List (USER_DATA)
`getFutureAccountTransactionHistoryList`

Borrow For Cross-Collateral (TRADE)
`borrowForCrossCollateral`

Cross-Collateral Borrow History (USER_DATA)
`crossCollateralBorrowHistory`

Repay For Cross-Collateral (TRADE)
`repayForCrossCollateral`

Cross-Collateral Repayment History (USER_DATA)
`crossCollateralRepaymentHistory`

Cross-Collateral Wallet (USER_DATA)
`crossCollateralWallet`

Cross-Collateral Wallet V2 (USER_DATA)
`crossCollateralWalletV2`

Cross-Collateral Information (USER_DATA)
`crossCollateralInformation`

Cross-Collateral Information V2 (USER_DATA)
`crossCollateralInformation_V2`

Calculate Rate After Adjust Cross-Collateral LTV (USER_DATA)
`calculateRateAfterAdjustCrossCollateralLTV`

Calculate Rate After Adjust Cross-Collateral LTV V2 (USER_DATA)
`calculateRateAfterAdjustCrossCollateralLTV_V2`

Get Max Amount for Adjust Cross-Collateral LTV (USER_DATA)
`getMaxAmountForAdjustCrossCollateralLTV`

Get Max Amount for Adjust Cross-Collateral LTV V2 (USER_DATA)
`getMaxAmountForAdjustCrossCollateralLTV_V2`

Adjust Cross-Collateral LTV (TRADE)
`adjustCrossCollateralLTV`

Adjust Cross-Collateral LTV V2 (TRADE)
`adjustCrossCollateralLTV_V2`

Adjust Cross-Collateral LTV History (USER_DATA)
`adjustCrossCollateralLTVHistory`

Cross-Collateral Liquidation History (USER_DATA)
`crossCollateralLiquidationHistory`

Check Collateral Repay Limit (USER_DATA)
`checkCollateralRepayLimit`

Get Collateral Repay Quote (USER_DATA)
`getCollateralRepayQuote`

Repay with Collateral (USER_DATA)
`repayWithCollateral`

Collateral Repayment Result (USER_DATA)
`collateralRepaymentResult`

Cross-Collateral Interest History (USER_DATA)
`crossCollateralInterestHistory`

# BLVT Endpoints
Get BLVT Info (MARKET_DATA)
`getBLVTInfo`

Subscribe BLVT (USER_DATA)
`subscribeBLVT`

Query Subscription Record (USER_DATA)
`querySubscriptionRecord`

Redeem BLVT (USER_DATA)
`redeemBLVT`

Query Redemption Record (USER_DATA)
`queryRedemptionRecord`

Get BLVT User Limit Info (USER_DATA)
`getBLVTUserLimitInfo`

# BSwap Endpoints
List All Swap Pools (MARKET_DATA)
`listAllSwapPools`

Get liquidity information of a pool (USER_DATA)
`getLiquidityInformationOfAPool`

Add Liquidity (TRADE)
`addLiquidity`

Remove Liquidity (TRADE)
`removeLiquidity`

Get Liquidity Operation Record (USER_DATA)
`getLiquidityOperationRecord`

Request Quote (USER_DATA)
`requestQuote`

Swap (TRADE)
`swap`

Get Swap History (USER_DATA)
`getSwapHistory`

# Fiat Endpoints
Get Fiat Deposit/Withdraw History (USER_DATA)
`getFiatDepositAndWithdrawHistory`

Get Fiat Payments History (USER_DATA)
`getFiatPaymentsHistory`