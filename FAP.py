import streamlit as st
import pandas as pd
from datetime import date
from yahoo_finance import Share as sh
from yahoo_fin import stock_info as si
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
import requests


st.set_page_config(page_title='Stock Prediction using ML', page_icon=' ')

def main():

	st.title("Welcome to Predict Future of Finance.")

	#----------Menu----------#

	menu = ["Recommendations","Crypto Currencies","Currency Converter","Analization","Stock Prediction using ML","Crypto Prediction using ML"]
	choice = st.sidebar.selectbox("Menu",menu)


#----------------------Recommendation----------------------#

	if choice == "Recommendations":
		st.header("Recommendations ")

	#----------Fetching Data of Most Active Users----------#

		si.get_day_most_active()
		st.subheader("Today's Most Active Users")
		active = si.get_day_most_active()
		st.write(active)
		
	#----------Plotting Data of Most Active Users----------#

		def plot_raw_data():
			fig = go.Figure()
			fig.add_trace(go.Bar(x=active['Symbol'], y=active['Volume']))
			fig.layout.update(title_text='Ranking of Most Active Users : ', xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
			st.plotly_chart(fig)			
		plot_raw_data()	

	#----------Fetching Data of Top Gainers----------#

		si.get_day_gainers()
		st.subheader("Today's Top Gainers")
		gainer = si.get_day_gainers()
		st.write (gainer)

	#----------Plotting Data of Top Gainers----------#

		def plot_raw_data():
			fig = go.Figure()
			fig.add_trace(go.Bar(x=gainer['Symbol'],y=gainer['% Change']))
			fig.layout.update(title_text='Ranking of Top Gainers : ', xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
			st.plotly_chart(fig)			
		plot_raw_data()	

	#----------Fetching Data of Top Losers----------#

		si.get_day_losers()
		st.subheader("Today's Top Losers")
		loser = si.get_day_losers()
		st.write(loser)

	#----------Plotting Data of Top Losers----------#

		def plot_raw_data():
			fig = go.Figure()
			fig.add_trace(go.Bar(x=loser['Symbol'],y=loser['% Change']))
			fig.layout.update(title_text='Ranking of Top Losers : ', xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
			st.plotly_chart(fig)			
		plot_raw_data()

#------------------------Currencies------------------------#

	elif choice == "Currencies":
    		
		#----------Fetching Data of Most Active Users----------#

			si.get_currencies()
			st.subheader("Today's Top Currencies ")
			currency = si.get_currencies()
			st.write(currency)

			def plot_raw_data():
				fig = go.Figure()
				fig.add_trace(go.Bar( x=currency['Symbol'],y=currency['% Change']))
				fig.layout.update(xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
				st.plotly_chart(fig)			
			plot_raw_data()

#---------------------Crypto Currencies---------------------#			


	elif choice == "Crypto Currencies":
    		
			si.get_top_crypto()
			st.subheader("Today's Top Crypto: ")
			crypto = si.get_top_crypto()
			st.write(crypto)

			st.subheader("Top Crypto's Price: ")

			def plot_raw_data():
				fig = go.Figure()
				fig.add_trace(go.Bar(x=crypto['Symbol'],y=crypto['Price (Intraday)']))
				fig.layout.update(xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
				st.plotly_chart(fig)			
			plot_raw_data()

			st.subheader("Top Crypto's Change (%): ")

			def plot_raw_data():
				fig = go.Figure()
				fig.add_trace(go.Bar(x=crypto['Symbol'],y=crypto["% Change"]))
				fig.layout.update(xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
				st.plotly_chart(fig)			
			plot_raw_data()

#--------------------Currency Converter--------------------#	


	if choice == "Currency Converter":
			st.header("Currency Converter ")

			api_key = '21XTTGBDL2CBO627'

			cmenu=['Choose type...','Currency','Cryptocurrency']
			choice1 = st.selectbox("Menu",cmenu)
			if choice1=='Choose type...':
    				
					st.write()


			elif choice1=='Currency':

				amount = st.number_input("Enter Amount...")


				c1 = st.selectbox("Convert From : ",
											["ALL - Lek	 - 	Albania Lek	",
											"AFN - 	؋	 - 	Afghanistan Afghani",
											"ARS - 	$	 - 	Argentina Peso",
											"AWG - 	ƒ	 - 	Aruba Guilder",
											"AUD - 	$	 - 	Australia Dollar",
											"AZN - 	₼	 - 	Azerbaijan Manat	",
											"BSD - 	$	 - 	Bahamas Dollar	",
											"BBD - 	$	 - 	Barbados Dollar	",
											"BYN - 	Br	 - 	Belarus Ruble	",
											"BZD - 	BZ$	 - 	Belize Dollar	",
											"BMD - 	$	 - 	Bermuda Dollar	",
											"BOB - 	$b	 - 	Bolivia Bolíviano	",
											"BAM - 	KM	 - 	Bosnia and Herzegovina Convertible Mark	",
											"BWP - 	P	 - 	Botswana Pula	",
											"BGN - 	лв	 - 	Bulgaria Lev	",
											"BRL - 	R$	 - 	Brazil Real	",
											"BND - 	$	 - 	Brunei Darussalam Dollar	",
											"HR	- 	៛	 - 	Cambodia Riel	",
											"CAD - 	$	 - 	Canada Dollar	",
											"KYD - 	$	 - 	Cayman Islands Dollar	",
											"CLP - 	$	 - 	Chile Peso	",
											"CNY - 	¥	 - 	China Yuan Renminbi	",
											"COP - 	$	 - 	Colombia Peso	",
											"CRC - 	₡	 - 	Costa Rica Colon	",
											"HRK - 	kn	 - 	Croatia Kuna	",
											"UP	- 	₱	 - 	Cuba Peso	",
											"CZK - 	Kč	 - 	Czech Republic Koruna	",
											"DKK - 	kr	 - 	Denmark Krone	",
											"DOP - 	RD$	 - 	Dominican Republic Peso	",
											"XCD - 	$	 - 	East Caribbean Dollar	",
											"EGP - 	£	 - 	Egypt Pound	",
											"SVC - 	$	 - 	El Salvador Colon	",
											"EUR - 	€	 - 	Euro Member Countries	",
											"FKP - 	£	 - 	Falkland Islands (Malvinas) Pound	",
											"FJD - 	$	 - 	Fiji Dollar	",
											"GHS - 	¢	 - 	Ghana Cedi	",
											"GIP - 	£	 - 	Gibraltar Pound	",
											"GTQ - 	Q	 - 	Guatemala Quetzal	",
											"GGP - 	£	 - 	Guernsey Pound	",
											"GYD - 	$	 - 	Guyana Dollar	",
											"HNL - 	L	 - 	Honduras Lempira	",
											"HKD - 	$	 - 	Hong Kong Dollar	",
											"HUF - 	Ft	 - 	Hungary Forint	",
											"ISK - 	kr	 - 	Iceland Krona	",
											"INR - 	₹	 - 	India Rupee	",
											"IDR - 	Rp	 - 	Indonesia Rupiah	",
											"IRR - 	﷼	 - 	Iran Rial	",
											"IMP - 	£	 - 	Isle of Man Pound	",
											"ILS - 	₪	 - 	Israel Shekel	",
											"JMD - 	J$	 - 	Jamaica Dollar	",
											"JPY - 	¥	 - 	Japan Yen	",
											"JEP - 	£	 - 	Jersey Pound	",
											"KZT - 	лв	 - 	Kazakhstan Tenge	",
											"KPW - 	₩	 - 	Korea (North) Won	",
											"KRW - 	₩	 - 	Korea (South) Won	",
											"KGS - 	лв	 - 	Kyrgyzstan Som	",
											"LAK - 	₭	 - 	Laos Kip	",
											"LBP - 	£	 - 	Lebanon Pound	",
											"LRD - 	$	 - 	Liberia Dollar	",
											"MKD - 	ден	 - 	Macedonia Denar	",
											"MYR - 	RM	 - 	Malaysia Ringgit	",
											"MUR - 	₨	 - 	Mauritius Rupee	",
											"MXN - 	$	 - 	Mexico Peso	",
											"MNT - 	₮	 - 	Mongolia Tughrik	",
											"MZN - 	MT	 - 	Mozambique Metical	",
											"NAD - 	$	 - 	Namibia Dollar	",
											"NPR - 	₨	 - 	Nepal Rupee	",
											"ANG - 	ƒ	 - 	Netherlands Antilles Guilder	",
											"NZD - 	$	 - 	New Zealand Dollar	",
											"NIO - 	C$	 - 	Nicaragua Cordoba	",
											"NGN - 	₦	 - 	Nigeria Naira	",
											"NOK - 	kr	 - 	Norway Krone	",
											"OMR - 	﷼	 - 	Oman Rial	",
											"PKR - 	₨	 - 	Pakistan Rupee	",
											"PAB - 	B/.	 - 	Panama Balboa	",
											"PYG - 	Gs	 - 	Paraguay Guarani	",
											"PEN - 	S/.	 - 	Peru Sol	",
											"PHP - 	₱	 - 	Philippines Peso	",
											"PLN - 	zł	 - 	Poland Zloty	",
											"QAR - 	﷼	 - 	Qatar Riyal	",
											"RON - 	lei	 - 	Romania Leu	",
											"RUB - 	₽	 - 	Russia Ruble	",
											"SHP - 	£	 - 	Saint Helena Pound	",
											"SAR - 	﷼	 - 	Saudi Arabia Riyal	",
											"SD	- 	Дин.    - 	Serbia Dinar	",
											"SCR - 	₨	 - 	Seychelles Rupee	",
											"SGD - 	$	 - 	Singapore Dollar	",
											"SBD - 	$	 - 	Solomon Islands Dollar	",
											"SOS - 	S	 - 	Somalia Shilling	",
											"ZAR - 	R	 - 	South Africa Rand	",
											"LKR - 	₨	 - 	Sri Lanka Rupee	",
											"SEK - 	kr	 - 	Sweden Krona	",
											"CHF - 	CHF	 - 	Switzerland Franc	",
											"SRD - 	$	 - 	Suriname Dollar	",
											"SYP - 	£	 - 	Syria Pound	",
											"TWD - 	NT$	 - 	Taiwan New Dollar	",
											"THB - 	฿	 - 	Thailand Baht	",
											"TTD - 	TT$	 - 	Trinidad and Tobago Dollar	",
											"TRY - 	Turkey Lira	",
											"TVD - 	$	 - 	Tuvalu Dollar	",
											"UAH - 	₴	 - 	Ukraine Hryvnia	",
											"GBP - 	£	 - 	United Kingdom Pound	",
											"USD - 	$	 - 	United States Dollar	",
											"UYU - 	$U	 - 	Uruguay Peso	",
											"UZS - 	лв	 - 	Uzbekistan Som	",
											"VEF - 	Bs	 - 	Venezuela Bolívar	",
											"VND - 	₫	 - 	Viet Nam Dong	",
											"YER - 	﷼	 - 	Yemen Rial	",
											"ZWD - 	Z$	 - 	Zimbabwe Dollar	"])

				c2 = st.selectbox("Convert To : ",
										["ALL - Lek	 - 	Albania Lek	",
											"AFN - 	؋	 - 	Afghanistan Afghani",
											"ARS - 	$	 - 	Argentina Peso",
											"AWG - 	ƒ	 - 	Aruba Guilder",
											"AUD - 	$	 - 	Australia Dollar",
											"AZN - 	₼	 - 	Azerbaijan Manat	",
											"BSD - 	$	 - 	Bahamas Dollar	",
											"BBD - 	$	 - 	Barbados Dollar	",
											"BYN - 	Br	 - 	Belarus Ruble	",
											"BZD - 	BZ$	 - 	Belize Dollar	",
											"BMD - 	$	 - 	Bermuda Dollar	",
											"BOB - 	$b	 - 	Bolivia Bolíviano	",
											"BAM - 	KM	 - 	Bosnia and Herzegovina Convertible Mark	",
											"BWP - 	P	 - 	Botswana Pula	",
											"BGN - 	лв	 - 	Bulgaria Lev	",
											"BRL - 	R$	 - 	Brazil Real	",
											"BND - 	$	 - 	Brunei Darussalam Dollar	",
											"HR	- 	៛	 - 	Cambodia Riel	",
											"CAD - 	$	 - 	Canada Dollar	",
											"KYD - 	$	 - 	Cayman Islands Dollar	",
											"CLP - 	$	 - 	Chile Peso	",
											"CNY - 	¥	 - 	China Yuan Renminbi	",
											"COP - 	$	 - 	Colombia Peso	",
											"CRC - 	₡	 - 	Costa Rica Colon	",
											"HRK - 	kn	 - 	Croatia Kuna	",
											"UP	- 	₱	 - 	Cuba Peso	",
											"CZK - 	Kč	 - 	Czech Republic Koruna	",
											"DKK - 	kr	 - 	Denmark Krone	",
											"DOP - 	RD$	 - 	Dominican Republic Peso	",
											"XCD - 	$	 - 	East Caribbean Dollar	",
											"EGP - 	£	 - 	Egypt Pound	",
											"SVC - 	$	 - 	El Salvador Colon	",
											"EUR - 	€	 - 	Euro Member Countries	",
											"FKP - 	£	 - 	Falkland Islands (Malvinas) Pound	",
											"FJD - 	$	 - 	Fiji Dollar	",
											"GHS - 	¢	 - 	Ghana Cedi	",
											"GIP - 	£	 - 	Gibraltar Pound	",
											"GTQ - 	Q	 - 	Guatemala Quetzal	",
											"GGP - 	£	 - 	Guernsey Pound	",
											"GYD - 	$	 - 	Guyana Dollar	",
											"HNL - 	L	 - 	Honduras Lempira	",
											"HKD - 	$	 - 	Hong Kong Dollar	",
											"HUF - 	Ft	 - 	Hungary Forint	",
											"ISK - 	kr	 - 	Iceland Krona	",
											"INR - 	₹	 - 	India Rupee	",
											"IDR - 	Rp	 - 	Indonesia Rupiah	",
											"IRR - 	﷼	 - 	Iran Rial	",
											"IMP - 	£	 - 	Isle of Man Pound	",
											"ILS - 	₪	 - 	Israel Shekel	",
											"JMD - 	J$	 - 	Jamaica Dollar	",
											"JPY - 	¥	 - 	Japan Yen	",
											"JEP - 	£	 - 	Jersey Pound	",
											"KZT - 	лв	 - 	Kazakhstan Tenge	",
											"KPW - 	₩	 - 	Korea (North) Won	",
											"KRW - 	₩	 - 	Korea (South) Won	",
											"KGS - 	лв	 - 	Kyrgyzstan Som	",
											"LAK - 	₭	 - 	Laos Kip	",
											"LBP - 	£	 - 	Lebanon Pound	",
											"LRD - 	$	 - 	Liberia Dollar	",
											"MKD - 	ден	 - 	Macedonia Denar	",
											"MYR - 	RM	 - 	Malaysia Ringgit	",
											"MUR - 	₨	 - 	Mauritius Rupee	",
											"MXN - 	$	 - 	Mexico Peso	",
											"MNT - 	₮	 - 	Mongolia Tughrik	",
											"MZN - 	MT	 - 	Mozambique Metical	",
											"NAD - 	$	 - 	Namibia Dollar	",
											"NPR - 	₨	 - 	Nepal Rupee	",
											"ANG - 	ƒ	 - 	Netherlands Antilles Guilder	",
											"NZD - 	$	 - 	New Zealand Dollar	",
											"NIO - 	C$	 - 	Nicaragua Cordoba	",
											"NGN - 	₦	 - 	Nigeria Naira	",
											"NOK - 	kr	 - 	Norway Krone	",
											"OMR - 	﷼	 - 	Oman Rial	",
											"PKR - 	₨	 - 	Pakistan Rupee	",
											"PAB - 	B/.	 - 	Panama Balboa	",
											"PYG - 	Gs	 - 	Paraguay Guarani	",
											"PEN - 	S/.	 - 	Peru Sol	",
											"PHP - 	₱	 - 	Philippines Peso	",
											"PLN - 	zł	 - 	Poland Zloty	",
											"QAR - 	﷼	 - 	Qatar Riyal	",
											"RON - 	lei	 - 	Romania Leu	",
											"RUB - 	₽	 - 	Russia Ruble	",
											"SHP - 	£	 - 	Saint Helena Pound	",
											"SAR - 	﷼	 - 	Saudi Arabia Riyal	",
											"SD	- 	Дин.    - 	Serbia Dinar	",
											"SCR - 	₨	 - 	Seychelles Rupee	",
											"SGD - 	$	 - 	Singapore Dollar	",
											"SBD - 	$	 - 	Solomon Islands Dollar	",
											"SOS - 	S	 - 	Somalia Shilling	",
											"ZAR - 	R	 - 	South Africa Rand	",
											"LKR - 	₨	 - 	Sri Lanka Rupee	",
											"SEK - 	kr	 - 	Sweden Krona	",
											"CHF - 	CHF	 - 	Switzerland Franc	",
											"SRD - 	$	 - 	Suriname Dollar	",
											"SYP - 	£	 - 	Syria Pound	",
											"TWD - 	NT$	 - 	Taiwan New Dollar	",
											"THB - 	฿	 - 	Thailand Baht	",
											"TTD - 	TT$	 - 	Trinidad and Tobago Dollar	",
											"TRY - 	Turkey Lira	",
											"TVD - 	$	 - 	Tuvalu Dollar	",
											"UAH - 	₴	 - 	Ukraine Hryvnia	",
											"GBP - 	£	 - 	United Kingdom Pound	",
											"USD - 	$	 - 	United States Dollar	",
											"UYU - 	$U	 - 	Uruguay Peso	",
											"UZS - 	лв	 - 	Uzbekistan Som	",
											"VEF - 	Bs	 - 	Venezuela Bolívar	",
											"VND - 	₫	 - 	Viet Nam Dong	",
											"YER - 	﷼	 - 	Yemen Rial	",
											"ZWD - 	Z$	 - 	Zimbabwe Dollar	"])
				c3=c1
				c4=c2
				c3=c3[:3]
				c4=c4[:3]
				from_c= c3
				to_c= c4
			
				base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
				main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key

				response = requests.get(main_url)
				result = response.json()

				key = result['Realtime Currency Exchange Rate']
				rate = key['5. Exchange Rate']

				cc = (f'{amount} {from_c} : {float(rate) * amount} {to_c}')

				st.subheader(cc)


			elif choice1=='Cryptocurrency':
    
				amount = st.number_input("Enter Amount...")


				c1 = st.selectbox("Convert From : ",
											["BTC - Bitcoin",
											"ETH - Ethereum",
											"USDT - Tether",
											"BNB - 	Binance Coin",
											"ADA - 	Cardano",
											"XRP - 	XRP	",
											"DOGE - Dogecoin",
											"USDC - USD Coin",
											"DOT - 	Polkadot",
											"UNI - 	Uniswap	",
											"BUSD - Binance USD	",
											"BCH - 	Bitcoin Cash",
											"SOL - 	Solana",
											"LTC - 	Litecoin",
											"LINK - Chainlink",
											"MATIC - Polygon",
											"WBTC - Wrapped Bitcoin",
											"ETC - 	Ethereum Classic",
											"ICP - 	Internet Computer",
											"THETA - THETA",
											"XLM - 	Stellar",
											"DAI - 	Dai",
											"VET - 	VeChain",
											"FIL - 	Filecoin",
											"TRX - 	TRON",
											"AAVE - Aave",
											"XMR - 	Monero",
											"EOS - 	EOS",
											"SHIB - SHIBA INU",
											"CRO - 	Crypto.com Coin",
											"MKR - 	Maker",
											"ALGO - Algorand",
											"CAKE - PancakeSwap",
											"ATOM - Cosmos",
											"COMP - Compound",
											"BSV - 	Bitcoin SV",
											"NEO - 	Neo",
											"LEO - 	UNUS SED LEO",
											"KLAY - Klaytn",
											"LUNA - Terra",
											"FTT - 	FTX Token",
											"XTZ - 	Tezos",
											"BTCB - Bitcoin BEP2",
											"MIOTA - IOTA",
											"AVAX - Avalanche",
											"AMP - 	Amp",
											"GRT - 	The Graph",
											"UST - 	TerraUSD",
											"TFUEL - Theta Fuel",
											"DCR - 	Decred",
											"BTT - 	BitTorrent",
											"KSM - 	Kusama",
											"HT	- 	Huobi Token",
											"EGLD - Elrond",
											"WAVES - Waves",
											"RUNE - THORChain",
											"HBAR - Hedera Hashgraph",
											"CEL - 	Celsius",
											"TUSD - TrueUSD",
											"SNX - 	Synthetix",
											"CHZ - 	Chili	",
											"DASH - Dash",
											"ZEC - 	Zcash",
											"YFI - 	yearn.finance",
											"XDC - 	XinFin Network",
											"TEL - 	Telcoin	",
											"XEM - 	NEM	",
											"SUSHI - SushiSwap",
											"HNT - 	Helium",
											"HOT - 	Holo",
											"MANA - Decentraland",
											"STX - 	Stacks",
											"ENJ - 	Enjin Coin",
											"QNT - 	Quant",
											"NEAR - NEAR Protocol",
											"ZIL - 	Zilliqa",
											"PAX - 	Paxos Standard",
											"BAT - 	Basic Attention Token",
											"KCS - 	KuCoin Token",
											"MDX - 	Mdex",
											"NEXO - Nexo",
											"BTG - 	Bitcoin Gold",
											"CELO - Celo",
											"BNT - 	Banco	",
											"CRV - 	Curve DAO Token	",
											"ZEN - 	Horizen",
											"ONE - 	Harmony",
											"QTUM - Qtum",
											"REV - 	Revain",
											"SC - 	Siacoin",
											"DGB - 	DigiByte",
											"OMG - 	OMG Network",
											"CHSB - SwissBorg",
											"ONT - 	Ontology",
											"FTM - 	Fantom",
											"OKB - 	OKB",
											"UMA - 	UMA",
											"NANO - Nano",
											"ZRX - 	0x",
											"HUSD -	HUSD"])
				c2 = st.selectbox("Convert To : ",
											["ALL - Lek	 - 	Albania Lek	",
											"AFN - 	؋	 - 	Afghanistan Afghani",
											"ARS - 	$	 - 	Argentina Peso",
											"AWG - 	ƒ	 - 	Aruba Guilder",
											"AUD - 	$	 - 	Australia Dollar",
											"AZN - 	₼	 - 	Azerbaijan Manat	",
											"BSD - 	$	 - 	Bahamas Dollar	",
											"BBD - 	$	 - 	Barbados Dollar	",
											"BYN - 	Br	 - 	Belarus Ruble	",
											"BZD - 	BZ$	 - 	Belize Dollar	",
											"BMD - 	$	 - 	Bermuda Dollar	",
											"BOB - 	$b	 - 	Bolivia Bolíviano	",
											"BAM - 	KM	 - 	Bosnia and Herzegovina Convertible Mark	",
											"BWP - 	P	 - 	Botswana Pula	",
											"BGN - 	лв	 - 	Bulgaria Lev	",
											"BRL - 	R$	 - 	Brazil Real	",
											"BND - 	$	 - 	Brunei Darussalam Dollar	",
											"HR	- 	៛	 - 	Cambodia Riel	",
											"CAD - 	$	 - 	Canada Dollar	",
											"KYD - 	$	 - 	Cayman Islands Dollar	",
											"CLP - 	$	 - 	Chile Peso	",
											"CNY - 	¥	 - 	China Yuan Renminbi	",
											"COP - 	$	 - 	Colombia Peso	",
											"CRC - 	₡	 - 	Costa Rica Colon	",
											"HRK - 	kn	 - 	Croatia Kuna	",
											"UP	- 	₱	 - 	Cuba Peso	",
											"CZK - 	Kč	 - 	Czech Republic Koruna	",
											"DKK - 	kr	 - 	Denmark Krone	",
											"DOP - 	RD$	 - 	Dominican Republic Peso	",
											"XCD - 	$	 - 	East Caribbean Dollar	",
											"EGP - 	£	 - 	Egypt Pound	",
											"SVC - 	$	 - 	El Salvador Colon	",
											"EUR - 	€	 - 	Euro Member Countries	",
											"FKP - 	£	 - 	Falkland Islands (Malvinas) Pound	",
											"FJD - 	$	 - 	Fiji Dollar	",
											"GHS - 	¢	 - 	Ghana Cedi	",
											"GIP - 	£	 - 	Gibraltar Pound	",
											"GTQ - 	Q	 - 	Guatemala Quetzal	",
											"GGP - 	£	 - 	Guernsey Pound	",
											"GYD - 	$	 - 	Guyana Dollar	",
											"HNL - 	L	 - 	Honduras Lempira	",
											"HKD - 	$	 - 	Hong Kong Dollar	",
											"HUF - 	Ft	 - 	Hungary Forint	",
											"ISK - 	kr	 - 	Iceland Krona	",
											"INR - 	₹	 - 	India Rupee	",
											"IDR - 	Rp	 - 	Indonesia Rupiah	",
											"IRR - 	﷼	 - 	Iran Rial	",
											"IMP - 	£	 - 	Isle of Man Pound	",
											"ILS - 	₪	 - 	Israel Shekel	",
											"JMD - 	J$	 - 	Jamaica Dollar	",
											"JPY - 	¥	 - 	Japan Yen	",
											"JEP - 	£	 - 	Jersey Pound	",
											"KZT - 	лв	 - 	Kazakhstan Tenge	",
											"KPW - 	₩	 - 	Korea (North) Won	",
											"KRW - 	₩	 - 	Korea (South) Won	",
											"KGS - 	лв	 - 	Kyrgyzstan Som	",
											"LAK - 	₭	 - 	Laos Kip	",
											"LBP - 	£	 - 	Lebanon Pound	",
											"LRD - 	$	 - 	Liberia Dollar	",
											"MKD - 	ден	 - 	Macedonia Denar	",
											"MYR - 	RM	 - 	Malaysia Ringgit	",
											"MUR - 	₨	 - 	Mauritius Rupee	",
											"MXN - 	$	 - 	Mexico Peso	",
											"MNT - 	₮	 - 	Mongolia Tughrik	",
											"MZN - 	MT	 - 	Mozambique Metical	",
											"NAD - 	$	 - 	Namibia Dollar	",
											"NPR - 	₨	 - 	Nepal Rupee	",
											"ANG - 	ƒ	 - 	Netherlands Antilles Guilder	",
											"NZD - 	$	 - 	New Zealand Dollar	",
											"NIO - 	C$	 - 	Nicaragua Cordoba	",
											"NGN - 	₦	 - 	Nigeria Naira	",
											"NOK - 	kr	 - 	Norway Krone	",
											"OMR - 	﷼	 - 	Oman Rial	",
											"PKR - 	₨	 - 	Pakistan Rupee	",
											"PAB - 	B/.	 - 	Panama Balboa	",
											"PYG - 	Gs	 - 	Paraguay Guarani	",
											"PEN - 	S/.	 - 	Peru Sol	",
											"PHP - 	₱	 - 	Philippines Peso	",
											"PLN - 	zł	 - 	Poland Zloty	",
											"QAR - 	﷼	 - 	Qatar Riyal	",
											"RON - 	lei	 - 	Romania Leu	",
											"RUB - 	₽	 - 	Russia Ruble	",
											"SHP - 	£	 - 	Saint Helena Pound	",
											"SAR - 	﷼	 - 	Saudi Arabia Riyal	",
											"SD	- 	Дин.    - 	Serbia Dinar	",
											"SCR - 	₨	 - 	Seychelles Rupee	",
											"SGD - 	$	 - 	Singapore Dollar	",
											"SBD - 	$	 - 	Solomon Islands Dollar	",
											"SOS - 	S	 - 	Somalia Shilling	",
											"ZAR - 	R	 - 	South Africa Rand	",
											"LKR - 	₨	 - 	Sri Lanka Rupee	",
											"SEK - 	kr	 - 	Sweden Krona	",
											"CHF - 	CHF	 - 	Switzerland Franc	",
											"SRD - 	$	 - 	Suriname Dollar	",
											"SYP - 	£	 - 	Syria Pound	",
											"TWD - 	NT$	 - 	Taiwan New Dollar	",
											"THB - 	฿	 - 	Thailand Baht	",
											"TTD - 	TT$	 - 	Trinidad and Tobago Dollar	",
											"TRY - 	Turkey Lira	",
											"TVD - 	$	 - 	Tuvalu Dollar	",
											"UAH - 	₴	 - 	Ukraine Hryvnia	",
											"GBP - 	£	 - 	United Kingdom Pound	",
											"USD - 	$	 - 	United States Dollar	",
											"UYU - 	$U	 - 	Uruguay Peso	",
											"UZS - 	лв	 - 	Uzbekistan Som	",
											"VEF - 	Bs	 - 	Venezuela Bolívar	",
											"VND - 	₫	 - 	Viet Nam Dong	",
											"YER - 	﷼	 - 	Yemen Rial	",
											"ZWD - 	Z$	 - 	Zimbabwe Dollar	"])
				c3=c1
				c4=c2
				c3=c3[:3]
				c4=c4[:3]
				from_c= c3
				to_c= c4
			
				base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
				main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key

				response = requests.get(main_url)
				result = response.json()

				key = result['Realtime Currency Exchange Rate']
				rate = key['5. Exchange Rate']

				cc = (f'{amount} {from_c} : {float(rate) * amount} {to_c}')

				st.subheader(cc)

#------------------------Analization------------------------#		

	elif choice == "Analization":
    		
	    st.header("Stock Analization using ML")

	    START = "2015-01-01"
	    TODAY = date.today().strftime("%Y-%m-%d")

	    selected_stock1 = st.text_input("Type 1st Stocks's name...")
	    selected_stock2 = st.text_input("Type 2nd Stocks's name...")

	    submit = st.button('Analyze')
	    if submit:

		    msft = yf.Ticker(selected_stock1) 
		    name1 = msft.info['longName']

		    msft = yf.Ticker(selected_stock2) 
		    name2 = msft.info['longName']

		    si.get_live_price(selected_stock1)
		    st.write("Live Price of " + name1 + " : $" , si.get_live_price(selected_stock1))
            

		    si.get_live_price(selected_stock2)
		    st.write("Live Price of " + name2 + " : $" , si.get_live_price(selected_stock2))

            
		    def load_data(ticker):
			    data = yf.download(ticker, START, TODAY)
			    data.reset_index(inplace=True)
			    return data

                
		    data = load_data(selected_stock1)
		    data1 = load_data(selected_stock2)


		    st.subheader('Raw data of '+ name1)
		    st.write(data.tail())
		    st.subheader('Raw data of '+ name2)
		    st.write(data1.tail())


			# Plot Volume of the companies

		    def plot_raw_data():
		        fig = go.Figure()
		        fig.add_trace(go.Bar(x=data['Date'], y=data['Volume'], name="Volume of "+name1))				
		        fig.add_trace(go.Bar(x=data1['Date'], y=data1['Volume'],name="Volume of "+name2))
		        fig.layout.update(title_text='Analization of Volume Data : ', xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
		        st.plotly_chart(fig)
                
		    plot_raw_data()


            # Plot Open & Closed Data
            
		    def plot_raw_data():
		        fig = go.Figure()
		        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Open Price of " +name1))
		        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Closed Price of "+name1))
		        fig.add_trace(go.Scatter(x=data1['Date'], y=data1['Open'], name="Open Price of "+name2))
		        fig.add_trace(go.Scatter(x=data1['Date'], y=data1['Close'], name="Closed Price of " +name2))
		        fig.layout.update(title_text='Analization of Open and Close Data : ', xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
		        st.plotly_chart(fig)
                
		    plot_raw_data()

			# Plot High & low of the companies

		    def plot_raw_data():
		        fig = go.Figure()
		        fig.add_trace(go.Line(x=data['Date'], y=data['High'], name="High of "+name1))	
		        fig.add_trace(go.Line(x=data['Date'], y=data['Low'], name="Low of "+name1))				
		        fig.add_trace(go.Line(x=data1['Date'], y=data1['High'],name="High of "+name2))			
		        fig.add_trace(go.Line(x=data1['Date'], y=data1['Low'],name="Low of "+name2))
		        fig.layout.update(title_text='Analization of High and Low Data : ', xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
		        st.plotly_chart(fig)      

		    plot_raw_data()

#-----------------Stock Prediction using ML-----------------#	

	elif choice == "Stock Prediction using ML":
		st.header("Stock Prediction using ML")

		START = "2010-01-01"
		TODAY = date.today().strftime("%Y-%m-%d")

		selected_stock = st.text_input("Type Stocks's name...")


		n_years = st.slider("Years of prediction:", 1, 10)
		period = n_years * 365


		submit = st.button('Predict')
		if submit:
    			
			
			def load_data(ticker):
				data = yf.download(ticker, START, TODAY)
				data.reset_index(inplace=True)
				return data

			data_load_state = st.text('Loading data...')
			data = load_data(selected_stock)
			data_load_state.text('Loading data... done!')

			
			si.get_live_price(selected_stock)
			st.write("Live Price : $", si.get_live_price(selected_stock))

			
			si.get_market_status()
			st.write("Market state : ", "CLOSED")


			st.subheader('Raw data')
			st.write(data.tail())

			# Plot raw data
			
			def plot_raw_data():
				fig = go.Figure()
				fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Open Price"))
				fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Closed Price"))
				fig.layout.update(title_text='Open and Close Price Data : ', xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
				st.plotly_chart(fig)
				
			plot_raw_data()

			# Predict forecast with Prophet.
			df_train = data[['Date','Close']]
			df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

			m = Prophet()
			m.fit(df_train)
			future = m.make_future_dataframe(periods=period)
			forecast = m.predict(future)

			# Show and plot forecast
			st.subheader('Forecasted data')
			st.write(forecast.tail())
				
			st.write(f'Forecasted plot for {n_years} years')
			fig1 = plot_plotly(m, forecast)
			fig1.layout.update( xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
			st.plotly_chart(fig1)

			st.write("Forecasted components")
			fig2 = m.plot_components(forecast)
			st.write(fig2)

#-----------------Crypto Prediction using ML-----------------#	

	elif choice == "Crypto Prediction using ML":
			st.header("Crypto Prediction using ML")

			START = "2010-01-01"
			TODAY = date.today().strftime("%Y-%m-%d")

			selected_crypto = st.text_input("Type Crypto Currency's name...")

			
			n_years = st.slider("Years of prediction:", 1, 10)
			period = n_years * 365


			submit = st.button('Predict')
			if submit:
					
				
				def load_data(ticker):
					data = yf.download(ticker, START, TODAY)
					data.reset_index(inplace=True)
					return data

				data_load_state = st.text('Loading data...')
				data = load_data(selected_crypto)
				data_load_state.text('Loading data... done!')
							
				si.get_live_price(selected_crypto)
				st.write("Live Price : ", si.get_live_price(selected_crypto))
				
				si.get_market_status()
				st.write("Market state : ", "CLOSED")


				st.subheader('Raw data')
				st.write(data.tail())

				# Plot raw data
				
				def plot_raw_data():
					fig = go.Figure()
					fig.add_trace(go.Scatter(x=data['Date'], y=data['High'], name="Highest"))
					fig.add_trace(go.Scatter(x=data['Date'], y=data['Low'], name="Lowest"))
					fig.layout.update(title_text='High and Low Data : ', xaxis_rangeslider_visible=True,width=800, height=600, hovermode='x')
					st.plotly_chart(fig)
					
				plot_raw_data()

				# Predict forecast with Prophet.
				df_train = data[['Date','Close']]
				df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

				m = Prophet()
				m.fit(df_train)
				future = m.make_future_dataframe(periods=period)
				forecast = m.predict(future)

				# Show and plot forecast
				st.subheader('Forecasted data')
				st.write(forecast.tail())
					
				st.write(f'Forecasted plot for {n_years} Years')
				fig3 = plot_plotly(m, forecast)
				fig3.layout.update( xaxis_rangeslider_visible=True, width=800, height=600, hovermode='x')
				st.plotly_chart(fig3)

				st.write("Forecasted components")
				fig4 = m.plot_components(forecast)
				st.write(fig4)

if __name__ == '__main__':
	main()