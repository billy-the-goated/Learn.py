# imports


# Makes
user_go_again = True

# Code
while user_go_again == True:
    user_number1 = float(input("Choose your first number: "))
    user_number2 = float(input("Choose your second number: "))
    user_method = str(input("Choose the method you want to use: \n1.+ \n2.- \n3.* \n4./ \n"))

    if user_method == "+":
        print(f"Your sum for {user_number1} + {user_number2} is {user_number1 + user_number2}")
    elif user_method == "-":
        print(f"Your take away for {user_number1} - {user_number2} is {user_number1 - user_number2}")
    elif user_method == "*":
        print(f"Your multiplication for {user_number1} * {user_number2} is {user_number1 * user_number2}")
    elif user_method == "/":
        if user_number2 == 0:
            print("this is invalid")
        else:
            print(f"Your divide for {user_number1} / {user_number2} is {user_number1 / user_number2}")
    else:
        print("this is invalid")

    user_go_again = input("Go again? (y/n): ").lower() == "y"
