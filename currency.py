from forex_python.converter import CurrencyRates

def convert_currency():
    # Create an instance of the CurrencyRates class
    c = CurrencyRates()

    # Get the latest exchange rates
    exchange_rates = c.get_rates('USD')  

    
    print("Available currencies:")
    for currency_code, rate in exchange_rates.items():
        print(f"{currency_code}: {rate}")

    # Input for conversion
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))

    # Perform the conversion
    converted_amount = c.convert(from_currency, to_currency, amount)

    # Display the result
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

if __name__ == "__main__":
    convert_currency()