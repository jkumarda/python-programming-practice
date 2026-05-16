def analyze_stock_price(company_name, stock_price, growth_rate, years=1):
    projected_price = stock_price + (stock_price * growth_rate * years)
    #print(f"Projected stock price for {company_name} after growth: ${projected_price:.2f}")
    return projected_price
# Example usage
print(f"The projected stock price for Dynamic Cables is ${analyze_stock_price('Dynamic Cables', 150.00, 0.10, 2):.2f}")