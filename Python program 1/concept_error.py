def calculate_rate(price, rate):
    try:
        growth_rate = float(price) * (1 + rate)
        return growth_rate
    except ValueError:
        return "Invalid input: Price and rate must be numbers."
    except Exception as e:
        return f"An error occured: {e}"
    finally:
        print("Rate calculation attempted.")
# Example usage
input_price = input("Enter the price: ")
final_rate = calculate_rate(input_price, 0.05)
print(f"Calculated growth rate: {final_rate}")