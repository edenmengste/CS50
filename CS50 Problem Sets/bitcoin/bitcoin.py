import sys
import requests

def main():
    # 1. Handle command-line argument for the number of Bitcoins (n)
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 2. Query the CoinCap API for the current Bitcoin price
    api_url = "https://api.coincap.io/v2/assets/bitcoin"
    # Note: For this specific CoinCap endpoint (getting Bitcoin asset data),
    # an API key is NOT strictly required for public access.
    # The example URL in the problem description might imply it, but for v2/assets/bitcoin,
    # it works without one. If you use other CoinCap endpoints that require auth,
    # you would add headers like: headers = {"Authorization": "Bearer YOUR_API_KEY"}

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Navigate the JSON to get the price
        # The structure is data['data']['priceUsd']
        bitcoin_price_usd = float(data['data']['priceUsd'])

    except requests.RequestException:
        # Catch any network-related errors, bad HTTP responses, etc.
        sys.exit("Could not retrieve Bitcoin price. Check internet connection or API status.")
    except KeyError:
        # Catch if the expected JSON keys are missing (e.g., API response format changed)
        sys.exit("Could not parse Bitcoin price from API response. Unexpected data format.")
    except ValueError:
        # Catch if the priceUsd value cannot be converted to float
        sys.exit("Retrieved Bitcoin price is not a valid number.")


    # 3. Calculate the total cost and output in USD to four decimal places
    total_cost_usd = n_bitcoins * bitcoin_price_usd

    # Format the output: $ prefix, comma as thousands separator, 4 decimal places
    # The ':,.4f' format specifier does exactly this:
    #   ',' for thousands separator
    #   '.4f' for a float with 4 decimal places
    print(f"${total_cost_usd:,.4f}")

if __name__ == "__main__":
    main()
