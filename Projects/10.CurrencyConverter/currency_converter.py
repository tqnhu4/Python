# currency_converter.py

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Unsupported currency.")
    
    # Convert to USD first, then to target
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount


def main():
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'JPY': 110.0,
        'GBP': 0.75,
        'VND': 24000.0,
    }

    print("💱 Welcome to Currency Converter!")

    while True:
        try:
            print("\nAvailable currencies:", ", ".join(rates.keys()))
            from_currency = input("🔁 Convert from: ").upper()
            to_currency = input("➡️ Convert to: ").upper()
            amount = float(input("💰 Amount to convert: "))

            result = convert_currency(amount, from_currency, to_currency, rates)
            print(f"✅ {amount:.2f} {from_currency} = {result:.2f} {to_currency}")

        except ValueError as ve:
            print(f"⚠️ Error: {ve}")
        except Exception as e:
            print("❌ An unexpected error occurred:", str(e))

        again = input("\n🔄 Convert another? (y/n): ").lower()
        if again != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
