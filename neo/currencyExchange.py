import requests

def fetch_currency_exchange_rate(fromCurr, toCurr):
    url = ""
    if fromCurr != "":
        url = "https://api.exchangeratesapi.io/latest?base={}&symbols={}".format(toCurr, fromCurr)
    else:
        url = "https://api.exchangeratesapi.io/latest?base={}".format(toCurr)
    response = requests.get(url)
    return response.json()
