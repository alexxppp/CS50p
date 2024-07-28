import requests
import sys

if len(sys.argv) != 2:
    sys.exit(1)

try:
    quantity = float(sys.argv[1])
except:
    sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    price = r["bpi"]["USD"]["rate"]
except requests.exceptions.JSONDecodeError:
    print("no content")
    sys.exit(1)
except requests.RequestException:
    print("unable to make request")
    sys.exit(1)

amount = float(price.replace(",", "")) * quantity

print(f"${amount:,.4f}")
