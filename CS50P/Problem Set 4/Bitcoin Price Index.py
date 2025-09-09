import sys
import requests

# likely line of error, need to exit if user doesn't put in valid float
try:
    # calculates quantity of BTC, specified by user
    # convert to a float so price * quantity can be calculated
    BTC_amount = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
except IndexError:
    print("Command-line argument is missing")
    sys.exit(1)

try:

    # pricing components below
    # interacts with the endpoint API
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    # Convert response to JSON (i.e. a Python dictionary)
    data = response.json()
    # looks to JSON 'data' dictionary and then looks to the price value
    # if there's no price it'll return 0
    # JSON returns a string so 2 step process of converting to float
    price_str = data.get("data", {}).get("priceUsd", "0")
    BTC_price = float(price_str)
except requests.RequestException:
    print('Check API. Bitcoin price cannot be retrieved')

# a function that returns BTC via price * user quantity
def BTC_calc(BTC_amount, BTC_price):
    return BTC_amount * BTC_price

amount = BTC_calc(BTC_amount, BTC_price)
print(f"${amount:,.4f}")

