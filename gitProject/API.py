import requests

parameter = {'count': '2'}
# get result from currencyconverterapi
myrequest = requests.get("https://free.currencyconverterapi.com/api/v6/convert?q=USD_ILS&compact=n&apiKey=72a1f59a5bf27c222c80" ,params=parameter)

#https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=82afb087d5943815c10a
#https://free.currencyconverterapi.com/api/v6/convert?q=USD_ILS&compact=n&apiKey=72a1f59a5bf27c222c80
# save result as json
result = myrequest.json()
print(result)
# # print ILS to USD currency
print(result['query']['count'])
print(result['results']['USD_ILS']['val'])