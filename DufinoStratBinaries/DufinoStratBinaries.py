import random

# User-defined variables
user_capital = 0
user_initial_investment = 0
trades_a_day = 0
days = 0
multiply = 0

# Initialize user input
def init():
    global user_capital, user_initial_investment, trades_a_day, days, multiply
    user_capital = float(input("Enter capital: "))
    user_initial_investment = float(input("Enter how much of the account do you want to risk (advised 0.0001 of your capital, e.g., 1€ for 10,000€ capital): "))
    trades_a_day = int(input("Enter how many trades you want to do a day: "))
    days = int(input("Enter how many days you want to simulate: "))
    multiply = float(input("Enter how much do you want the investment to multiply after loss: "))

# Simulated daily capital and investment
capital = 0
initial_investment = 0
account = 0  # Total profit/loss tracker

# Simulate a win
def win():
    global initial_investment, capital
    capital += (initial_investment / 100) * 92
    initial_investment = 1

# Simulate a loss
def loss():
    global initial_investment, capital
    capital -= initial_investment
    initial_investment *= multiply

# Store results
results = []
num_failed = 0

# Main simulation loop
def mainloop():
    global capital, initial_investment, account, num_failed
    capital = user_capital  # Reset capital at the start of each day
    initial_investment = user_initial_investment  # Reset initial investment each day
    
    for _ in range(trades_a_day):
        if capital <= 0:  # Capital exhausted
            num_failed += 1
            account -= user_capital  # Subtract the total capital as a loss
            results.append(-user_capital)  # Record a total loss for the day
            return
        if random.randint(0, 1) == 0:
            win()
        else:
            loss()

    # Save the profit/loss of the day into the account
    daily_result = capital - user_capital
    account += daily_result
    results.append(daily_result)

# Run simulation
init()
capital = user_capital
initial_investment = user_initial_investment

for _ in range(days):
    mainloop()

# Print results
for day, result in enumerate(results, 1):
    print(f"Day {day}: {'Profit' if result > 0 else 'Loss'} {result:.2f} €")

# Print the total account balance
print(f"Total account balance: {account:.2f} €")
print(f"Initial account balance: {user_capital} €")

# Calculate and print success rate
if num_failed == 0:
    print("Success rate: 100%")
else:
    success_rate = 100 * (len(results) - num_failed) / len(results)
    print(f"Success rate: {success_rate:.2f}%")

input("Press Enter to exit...")