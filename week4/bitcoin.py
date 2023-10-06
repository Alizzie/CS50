import requests
import sys

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    
    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("Number cannot get converted into float")
    
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    bitcoin_rate = response["bpi"]["USD"]["rate_float"] 
    amount = bitcoin_rate * num
    print(f"${amount:,.4f}")


except requests.RequestException:
    sys.exit("Request Exception")