def main():

    print("Welcome to the Stop Loss Take Profit Calculator")
    entry_price = input("What's your entry price? $")
    float_entry_price = float(entry_price)
    string_entry_price = str(entry_price)
    risk_percentage =input("How much of your capital would you like to risk? 5, 6 or 10%? ")
    profit_percentage =input("How much would you like to grow your capital on this trade? 5, 10, 20, 60, 80 or 100%? ")
    print(f"You're investing $"+ string_entry_price) 
    float_profit_percentage = float(profit_percentage)
    float_risk_percentage = float(risk_percentage)
    percentage = ( float_entry_price * float_risk_percentage ) / 100
    float_percentage = float(percentage)
    string_percentage = str(percentage)
    print(f"You're risking $"+ string_percentage)
    final_value = (float_entry_price - percentage)
    string_final_value = str(final_value)
    print(f"Stop loss at $"+ string_final_value)

    profit_percentage = ( float_entry_price * float_risk_percentage ) / 100

    take_profit = (float_entry_price + ( (float_entry_price * float_profit_percentage) / 100 ))
    string_take_profit = str(take_profit)
    print(f"Take profit at $"+ string_take_profit)

if __name__=="__main__":
        main()