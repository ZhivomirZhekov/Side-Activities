# Finance Calculator App
# Objective:
# Create a Python application that allows users to perform basic financial calculations.
# The application should use functions to handle various financial operations such as interest rate calculations,
# loan payments, and savings projections.
#
# Requirements:
# Create functions for the following financial calculations:
# Calculate Simple Interest
# Calculate Compound Interest
# Calculate Loan Payment (using the formula for monthly loan payments)
# Calculate Future Value of a Savings Account (with regular contributions)
# Implement a main menu function called main_menu() that displays the following options:
# Calculate Simple Interest
# Calculate Compound Interest
# Calculate Loan Payment
# Calculate Future Value of Savings
# Quit the application
# Allow users to input their choice (e.g., 1 for Simple Interest)
# and the required parameters (e.g., principal, rate, time) for the selected financial calculation.
# Call the appropriate function based on the user's choice and display the result.
# Ensure proper error handling for cases like division by zero or invalid input.
# Use appropriate financial formulas for calculations.
# Include user-friendly prompts and error messages.
# Guidelines:
# Use separate functions for each type of financial calculation to promote code modularity.
# Ensure that interest rates are correctly divided by 100 if provided as percentages (e.g., 5% as 0.05).
# Implement loops and error handling to prevent unexpected crashes.
# Provide explanations and labels for the input parameters to guide users.
# Allow users to return to the main menu after each calculation if they want to perform additional calculations.
# Use meaningful variable names to make the code self-explanatory.
# Example Output:
# Main Menu:
#
# Calculate Simple Interest
# Calculate Compound Interest
# Calculate Loan Payment
# Calculate Future Value of Savings
# Quit
# Enter your choice (1/2/3/4/5): 1
#
# Calculate Simple Interest
#
# Enter principal amount: 1000 Enter interest rate (as a decimal): 0.05 Enter time (in years): 3
#
# Simple Interest: $150.0
#
# Do you want to perform another calculation? (yes/no): yes
#
# Main Menu:
#
# Calculate Simple Interest
# Calculate Compound Interest
# Calculate Loan Payment
# Calculate Future Value of Savings
# Quit
# Enter your choice (1/2/3/4/5): 2
#
# Calculate Compound Interest
#
# Enter principal amount: 1000
# Enter annual interest rate (as a decimal): 0.05
# Enter the number of times interest is compounded per year: 4
# Enter time (in years): 3
#
# Compound Interest: $159.44
#
# Do you want to perform another calculation? (yes/no): no
#
# Goodbye!


def simple_interest(principal , rate , time):
    """""
    Formula: Simple Interest (SI) = Principal (P) x Rate (R) x Time (T) / 100.
    """""
    interest = principal * rate * time / 100
    return interest


def compound_interest(principal , rate_of_interest , compounded_interest , time):
    """""
     If the interest is compounded annually, the amount is given as:
     A = P * (1 + R / n) ** n * T
     A = amount
     P = principal
     R = rate of interest
     n = no of times interest got compounded annually
     T = time (in years)
    """""
    interest = principal * ((1 + rate_of_interest / compounded_interest) ** (compounded_interest * time))
    return interest


def monthly_loan(principal , interest_rate):
    """""
    # So, to get your monthly loan payment,
    # you must divide your interest rate by 12.
    # Whatever figure you get, multiply it by your principal.
    # A simpler way to look at it is monthly payment = principal x (interest rate / 12).
    # The formula might seem complex, but it doesn't have to be.
    """""
    monthly_payment = principal * (interest_rate / 12) + (principal / 12)
    return monthly_payment


def future_value(investment_amount, interest_rate, num_of_years):
    """""
    Calculate Future Value of Savings
    FV=I×(1+(R×T))
    where:
    I=Investment amount
    R=Interest rate
    T=Number of years
    """""
    value = investment_amount * (1 + (interest_rate * num_of_years))
    return value


def main_menu(counter):
    if counter > 0:
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation == 'yes':
            number = int(input("1. Calculate Simple Interest\n"
                               "2. Calculate Compound Interest\n"
                               "3. Calculate Loan Payment\n"
                               "4. Calculate Future Value of Savings\n"
                               "5. Quit the application\n"
                               "Enter your choice (1/2/3/4/5): "))
        else:
            number = 5
    else:
        number = int(input("1. Calculate Simple Interest\n"
                           "2. Calculate Compound Interest\n"
                           "3. Calculate Loan Payment\n"
                           "4. Calculate Future Value of Savings\n"
                           "5. Quit the application\n"
                           "Enter your choice (1/2/3/4/5): "))
    return number


counter = 0
number = main_menu(counter)
while number != 5:

    if number == 1:
        principle = float(input("Enter principle amount: "))
        rate = float(input("Enter interest rate percent %: "))
        time = float(input("Enter time in years: "))
        interest = simple_interest(principle, rate, time)
        print(f'Simple interest: {interest:.2f}')
    elif number == 2:
        principle = float(input("Enter principle amount: "))
        rate = float(input("Enter interest rate percent %: ")) / 100
        compounded_interest = float(input("Enter the number of times interest got compounded annually: "))
        time = float(input("Enter time in years: "))
        interest = compound_interest(principle, rate, compounded_interest, time)
        print(f'Compound Interest: {interest:.2f}')
    elif number == 3:
        principle = float(input("Enter principle amount:"))
        rate = float(input("Enter interest rate percent %:")) / 100
        interest = monthly_loan(principle, rate)
        print(f'Loan Payment: {interest:.2f}')
    elif number == 4:
        investment = float(input("Enter investment amount:"))
        rate = float(input("Enter interest rate percent %:")) / 100
        time = float(input("Enter time in years:"))
        value = future_value(investment, rate, time)
        print(f'Future Value of Savings: {value:.2f}')
    else:
        print("Invalid input, please try again!")
    print()
    counter += 1
    number = main_menu(counter)
print("You have exit the finance application. Good bye!")
