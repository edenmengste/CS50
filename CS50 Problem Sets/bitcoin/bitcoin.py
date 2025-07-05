import sys
import requests

def main():
   
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_url = "https://api.coincap.io/v2/assets/bitcoin"
   
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()

        bitcoin_price_usd = float(data['data']['priceUsd'])

    except requests.RequestException:
       
        sys.exit("Could not retrieve Bitcoin price. Check internet connection or API status.")
    except KeyError:
      
        sys.exit("Could not parse Bitcoin price from API response. Unexpected data format.")
    except ValueError:
       
        sys.exit("Retrieved Bitcoin price is not a valid number.")
    total_cost_usd = n_bitcoins * bitcoin_price_usd

    print(f"${total_cost_usd:,.4f}")

if __name__ == "__main__":
    main()
