import random

exit = False

while exit == False:
    user_capital = 0
    initial_capital = user_capital
    initial_investment = 0
    trades_a_day = 0
    days = 0
    multiply = 0
    results_trades = []
    results_days = []

    # Initialize user input
    def start():
        global user_capital,initial_capital, initial_investment, trades_a_day, days, multiply
        user_capital = float(input("Enter capital: "))
        initial_capital = user_capital
        initial_investment = float(input("Enter how much of the account do you want to risk (advised 0.0001 of your capital, e.g., 1€ for 10,000€ capital): "))
        trades_a_day = int(input("Enter how many trades you want to do a day: "))
        days = int(input("Enter how many days you want to simulate: "))
        multiply = float(input("Enter how much do you want the investment to multiply after loss: "))
        mainloop()

    # Simulate a win
    def win():
        global initial_investment, user_capital
        user_capital += (initial_investment / 100) * 92
        results_trades.append((initial_investment / 100) * 92)
        initial_investment = 1

    # Simulate a loss
    def loss():
        global initial_investment, user_capital
        user_capital -= initial_investment
        results_trades.append(-initial_investment)
        initial_investment *= multiply

    # Main simulation loop
    def mainloop():
        global user_capital, initial_investment
        for i in range(days):
            for n in range(trades_a_day):
                if user_capital <= 0:  # Capital lost
                    break
                elif random.randint(0, 1) == 0:
                    win()
                else:
                    loss()
            results_days.append(sum(results_trades))

    # Results
    def res():
        for result in results_days:
            day = int(results_days.index(result))
            print(f'Day {day+1}: {'profit' if results_days[day] > 0 else 'loss'} for today {round(results_days[day], 2)}€ ')
        print(f'{'Profit' if sum(results_days) > 0 else 'Lost'} {sum(results_days):.2f}€')

    def full_res():
        for result in results_days:
            day = int(results_days.index(result))
            print(f'Day {day+1}: {'profit' if results_days[day] > 0 else 'loss'} for today {round(results_days[day], 2)}€ ')
            for result_trade in results_trades[trades_a_day*day:trades_a_day*day+trades_a_day]:
                print(f'{'Win' if result_trade > 0 else 'Loss'}: {result_trade}€')

        print(f'{'Profit' if sum(results_days) > 0 else 'Lost'} overal {sum(results_days):.2f}€')


    # Run simulation
    start()

    # Print results
    done = input("Type exit to quit the program, res to see the results and full_res to see the full results\nAnything else will restart the program: ")
    if done == "exit":
        exit = True
    elif done == "res":
        res()
        if input("Press enter to continue or type full_res to see all results in detail... ") == "full_res":
            full_res()
            input("Press enter to continue...")
        else:
            pass
    elif done == "full_res":
        full_res()
        input("Press enter to continue...")
        pass
    else:
        pass

print(exit)