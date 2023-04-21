import requests
import json
import smtplib
#INR = ['RVN', 'RLC', 'KDA', 'VBTC', 'STORJ', 'KNC', 'BUSD', 'SHIB', 'BOND', 'CRV', 'CHZ', 'CND', 'CHR',  'XEM', 'EGLD', 'XCN', 'XMR', 'GRT', 'JASMY', 'GNO', 'FLOW', 'YFII', 'HOT', 'SUSHI', 'DIA', 'MAHA', 'MANA', 'MINA', 'MASK', 'ONE', 'OXT', 'UNI', 'MCO', 'MIR', 'MKR', 'XNO', 'EOS', 'BRISE', 'GALA', 'GARI', 'SFP', 'STX', 'SNT', 'SNX', 'SXP', 'DAI', 'JST', 'DGTX', 'DYDX', 'DOGE', 'DASH', 'AAVE', 'BCH', 'BAT', 'KLAY', 'YFI', 'DOT', 'ICX', 'IMX', 'ICP', 'ALICE', 'THETA', 'NMR', 'NEO', 'NKN', 'POLYX', 'SUPER', 'LTC', 'LPT', 'LDO', 'LRC', 'VET', 'HIGH', 'TUSD', 'FIL', 'FET', 'TRB', 'TRX', 'DGB', 'DFA', 'DNT', 'ZEC', 'ZIL', 'USDT', 'USDC', 'REN', 'REQ', 'SC', 'KSM', ]

USDT =['GRT', 'REN', 'REQ', 'TRB', 'TRX', 'JST', 'ZEC', 'ZIL', 'MARSH', 'FANC', 'FIDA', 'TRADE', 'LTC', 'LPT', 'LDO', 'LRC', 'ALICE', 'DFA', 'CAKE', 'CELO', 'CELR', 'COMP', 'COTI', 'TFUEL', 'POLYX', 'MATIC', 'FTM', 'FLM', 'THETA', 'QNT', '1INCH', 'GALA', 'GARI', 'SC', 'USDC', 'OGN', 'SHIB', 'STPT', 'BNB', 'BTC', 'BTT', 'SKL', 'SOL', 'BNX', 'XCAD', 'BUSD', 'BOND', 'BAND', 'PUSH', 'POWR', 'PAXG', 'OP', 'MBOX', 'WAXP', 'UNI', 'HIGH', 'TLOS', 'AAVE', 'KAVA', 'KDA', 'KNC', 'REEF', 'RUNE', 'ROSE', 'MKR', 'YFII', 'ALPACA', 'EOS', 'JASMY', 'GNO', 'INJ', 'WAVES', 'DYDX', 'DOGE', 'OMG', 'DASH', 'CRV', 'CHZ', 'CHR', 'XEM', 'XCN', 'XMR', 'STORJ', 'LINK','QTUM', 'RVN', 'RLC', 'TON', 'TWT', 'ZRX', 'HOT', 'FLOW', 'LIT', 'DCR', 'DGB', 'DIA', 'DAO', 'DAI', 'AUDIO', 'SUPER', 'DOT', 'FIL', 'FET', 'IOST', 'IOTX', 'PEOPLE', 'GLMR', 'NMR', 'NEO', 'NKN', 'NEAR', 'NEXO', 'SAND', 'EGLD', 'BCH', 'BAT', 'SFP', 'STX', 'SNT', 'SNX', 'SXP', 'BTTC', 'BRISE', 'SPELL', 'MANA', 'MINA', 'MASK', 'UMA', 'UST', 'HBAR', 'TUSD', 'ANKR', 'AVAX', 'KLAY', 'ALGO', 'ARPA', 'ATOM', 'VOLT', 'VINU', 'KSM', 'MDX', 'MTL', 'ENS', 'ENJ', 'ETN', 'EFI', 'ETH', 'ETC', 'GMT', 'ICX', 'IMX', 'ICP', 'VET', 'YFI', 'ONE', 'OXT', 'CKB', 'XTZ', 'XLM', 'XDB', 'XDC', 'XRP', 'OOKI', 'AR', 'OSMO', 'XNO', 'APE', 'ARB', 'ARV', 'ADA', 'APT', 'AXS', 'SUSHI']

BTC = [ 'KSM', 'TWT','LINK', 'SAND', 'CKB', 'OP', 'APE', 'ARB', 'ADA', 'APT', 'AXS', 'MATIC', 'XRP', 'XTZ', 'XLM', 'POWR', 'PAXG', 'SPELL', 'GMT', 'FIDA','1INCH', 'MBOX', 'OMG', 'OGN', 'UMA', 'UST', 'ALPACA', 'MDX', 'MTL', 'QTUM', 'ENS', 'ENJ', 'ETN', 'ETH', 'ETC', 'IOST', 'IOTX', 'GLMR', 'SKL', 'AUDIO', 'SOL', 'QNT', 'ANKR', 'BNB', 'KAVA', 'AVAX', 'ALGO', 'ARPA', 'ATOM', 'BNX', 'PEOPLE', 'NEAR', 'OSMO', 'NEXO', 'INJ', 'AR', 'CELO', 'CAKE', 'CELR', 'COMP', 'COTI', 'WAXP', 'TFUEL', 'LIT', 'HBAR',  'WAVES', 'TLOS', 'RUNE', 'ROSE', 'FTM', 'FLM', 'ZRX','RVN', 'RLC', 'KDA', 'STORJ', 'KNC', 'BOND', 'CRV', 'CHZ', 'CND', 'CHR', 'STPT', 'BAND', 'DCR', 'XEM', 'EGLD', 'XMR', 'GRT', 'JASMY', 'GNO', 'FLOW','HOT', 'SUSHI', 'DIA', 'MANA', 'ONE', 'OXT', 'UNI', 'MCO', 'MKR', 'XNO', 'EOS', 'GALA', 'SFP', 'STX', 'SNX', 'SXP', 'DAI', 'JST', 'DYDX', 'DOGE', 'DASH', 'AAVE', 'BCH', 'BAT', 'KLAY', 'YFI', 'DOT', 'ICX', 'IMX', 'ICP', 'ALICE', 'THETA', 'NMR', 'NEO', 'NKN', 'POLYX', 'SUPER', 'LTC', 'LPT', 'LDO', 'LRC', 'VET', 'HIGH', 'TUSD', 'FIL', 'FET', 'TRB', 'TRX', 'DGB', 'DNT', 'ZEC', 'ZIL', 'REN', 'REQ']

BNB = [ 'ZRX','LINK','SAND', 'ADA', 'AXS', 'MATIC', 'XRP', 'XTZ', 'XLM', 'POLY', 'POWR', 'PAXG', 'SPELL', 'GMT', 'FIDA', 'MBOX', 'OGN', 'ALPACA', 'MDX', 'QTUM', 'ENS', 'ENJ', 'ETC', 'IOST', 'SOL', 'QNT', 'ANKR', 'KAVA', 'BTT', 'AVAX', 'ALGO', 'ARPA', 'ATOM', 'BNX', 'PEOPLE', 'NEAR', 'INJ', 'AR', 'CAKE', 'CELR', 'COMP', 'COTI', 'WAXP', 'TFUEL', 'HBAR', 'WAVES', 'RUNE', 'FTM','RVN', 'RLC', 'CRV', 'CHZ', 'CND', 'CHR', 'STPT', 'BAND', 'CVC', 'DCR', 'XEM', 'EGLD', 'XMR', 'GNO', 'YFII', 'HOT', 'SUSHI', 'MINA', 'MASK', 'ONE', 'UNI', 'MCO', 'MKR', 'EOS', 'GALA', 'STX', 'SNX', 'SXP', 'DAI', 'JST', 'DYDX', 'DASH', 'AAVE', 'BCH', 'BAT', 'KLAY', 'YFI', 'DOT', 'ICX', 'ICP', 'THETA', 'NMR', 'NEO', 'LTC', 'LPT', 'VET', 'TUSD', 'FIL', 'FET', 'TRB', 'TRX', 'DGB', 'ZEC', 'ZIL', 'USDC', 'REN', 'SC']

ETH = ['LINK', 'SAND', 'ADA', 'APT', 'MATIC', 'XRP', 'XTZ', 'XLM', 'POWR', 'OMG', 'MTL', 'QTUM', 'ENJ', 'ETC', 'IOST', 'IOTX', 'BNB', 'ALGO', 'ARPA', 'ATOM', 'NEAR', 'NEXO', 'AR', 'COMP', 'WAVES', 'ZRX','RLC', 'KNC', 'CRV', 'CND', 'XEM', 'EGLD', 'XMR', 'GRT', 'FLOW', 'YFII', 'HOT', 'SUSHI', 'MANA', 'MCO', 'MKR', 'XNO', 'EOS', 'SNT', 'SNX', 'JST', 'DASH', 'AAVE', 'BAT', 'YFI', 'DOT', 'ICX', 'ICP', 'THETA', 'NEO', 'LTC', 'LRC', 'VET', 'TUSD', 'TRB', 'TRX', 'DNT', 'ZEC', 'ZIL', 'REN', 'REQ', 'SC']
currency_lists = {
	'USDT': [USDT],
    'BTC': [BTC],
    'ETH': [ETH],
    'BNB': [BNB]
}

basecurrency = ['USDT','BTC', 'ETH', 'BNB']

for base in basecurrency:
    CURRENCY = currency_lists[base]
    for cure in CURRENCY:
	        for curr in cure:
	            url1 = f'https://public.coindcx.com/market_data/orderbook?pair=l-{base}_INR'
	            url2 = f'https://public.coindcx.com/market_data/orderbook?pair=l-{curr}_{base}'
	            url3 = f'https://public.coindcx.com/market_data/orderbook?pair=l-{curr}_INR'
	            response1 = requests.get(url1)
	            response2 = requests.get(url2)
	            response3 = requests.get(url3)
	            if len(response1.content) > 40 and len(response2.content) > 40 and len(response3.content) > 40 :
	            	data1 = json.loads(response1.text)
	            	data2 = json.loads(response2.text)
	            	data3 = json.loads(response3.text)
	            	if  data1['timestamp'] > 1681997077935 and data2['timestamp'] > 1681997077935 and data3['timestamp'] > 1681997077935:
	            		
	            		
	            		
	            		
	            		
	            	
		            	ask_quantity1 = [float(quantity) for quantity in data1['asks'].values()][0]
		            	bid_quantity1 = [float(quantity) for quantity in data1['bids'].values()][0]
		            	ask_quantity2 = [float(quantity) for quantity in data2['asks'].values()][0]
		            	bid_quantity2 = [float(quantity) for quantity in data2['bids'].values()][0]
		            	ask_quantity3 = [float(quantity) for quantity in data3['asks'].values()][0]
		            	bid_quantity3 = [float(quantity) for quantity in data3['bids'].values()][0]
		            	ask_price1 = [float(price) for price in data1['asks'].keys()]
		            	lowest_ask1 = float(min(ask_price1))
		            	bid_price1 = [float(price) for price in data1['bids'].keys()]
		            	highest_bid1 = float(max(bid_price1))
		            	ask_price2 = [float(price) for price in data2['asks'].keys()]
		            	lowest_ask2 = float(min(ask_price2))
		            	bid_price2 = [float(price) for price in data2['bids'].keys()]
		            	highest_bid2 = float(max(bid_price2))
		            	ask_price3 = [float(price) for price in data3['asks'].keys()]
		            	lowest_ask3 = float(min(ask_price3))
		            	bid_price3 = [float(price) for price in data3['bids'].keys()]
		            	highest_bid3 = float(max(bid_price3))
		            	amount1 = lowest_ask1*ask_quantity1
		            	amount2 = lowest_ask2*ask_quantity2*lowest_ask1
		            	amount3 = highest_bid3*bid_quantity3
		            	amount = min(amount1, amount2, amount3)
		            	inr=1000.000000
		            	btc=0
		            	token=0
		            	btc = inr/lowest_ask1
		            	token = btc/lowest_ask2
		            	inr = token*highest_bid3
		            	a= {curr},{base},"safe amount:", amount,"profit:" ,inr
		            	print("\n",{curr},{base},"safe amount:", amount,"\n", "profit:" ,inr)
		            	if inr > 1025:
		            		subject = "Data from my program"
		            		body = "Here is the data:\n{}".format(a)
		            		message = f"Subject: {subject}\n\n{body}"
		            		smtp_server = "smtp.gmail.com"
		            		port = 587
		            		username = "keerak0009@gmail.com"
		            		password = "oywqosuhvhqxtlvy"
		            		with smtplib.SMTP(smtp_server, port) as smtp:
		            			smtp.starttls()
		            			smtp.login(username, password)
		            			smtp.sendmail('keerak0009@gmail.com', 'arpitkeer11@gmail.com', message)
	            	else:
	            		print('\nold data')	         
	            else:
		            print("\nfailed to fetch the data")
