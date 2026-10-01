# from datetime import datetime

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# income = int(input("Enter your income: "))

# if age < 21 or age > 60:
#     print("You are not eligible because of age.")

# if income < 25000:
#     print("You are not eligible because of income.")

# if age >= 21 and age <= 60 and income >= 25000:
#     print("Congratulations! You are eligible for loan.")

# print("Date and Time:", datetime.now())

# with open("loan.txt", "a") as file:
#     file.write(name + " " + str(datetime.now()) + "\n")

# print("Record saved successfully.")

from datetime import datetime

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 21 or age > 60:
        decision = "Not Eligible - Invalid age"
        print("Age is not valid for loan eligibility.")

    else:
        income = int(input("Enter your monthly income: "))

        if income < 25000:
            decision = "Not Eligible - Income criteria not satisfied"
            print("You are not eligible because your income is below 25000.")

        else:
            decision = "Eligible for Loan"
            print("Congratulations! You are eligible for loan.")

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("loan.txt", "a") as file:
        file.write(
            f"\nName: {name}, \n"
            f"Age: {age}, \n"
            f"Decision: {decision}, \n"
            f"Date and Time: {current_time}\n"
        )

    print("Record saved successfully.")

except ValueError:
    print("Invalid input! Please enter a valid number.")