from art import logo
print(logo)

# TODO 1: Write out the other 3 functions - subtract, multiply and divide.
# TODO 1A: Additions.
def add(num1, num2):
    return num1 + num2

# TODO 1B: Subtraction.
def sub(num1, num2):
    return num1 - num2

# TODO 1C: Multiplication.
def mult(num1, num2):
    return num1 * num2

# TODO 1D: Division.
def div(num1, num2):
    return num1 / num2

# TODO 2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

# TODO 3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# place = operations["*"](4, 8)
# print(operations["*"](4, 8))

# Functionality
# TODO 4: Perform the Calculations.

def calculator():
    reload = True

    # TODO 4A: Program asks the user to type the first number.
    ask_num1 = float(input("Enter your first number: "))

    # TODO 4G: If yes, program loops to use the previous result as the first number and then repeats the calculation process.
    while reload:

        # TODO 4B: Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
        print("Valid Choices are: '+', '-', '*', '/'")
        ask_opr = str(input("Enter the operation: "))

        # TODO 4C: Program asks the user to type the second number.
        ask_num2 = float(input("Enter your next number: "))

        # TODO 4D: Program works out the result based on the chosen mathematical operator.
        result = operations[ask_opr](ask_num1, ask_num2)

        print(f"{ask_num1} {ask_opr} {ask_num2} = {result}")
        print(f"Do you want to continue calculating with {result}?: ")

        # TODO 4E: Program asks if the user wants to continue working with the previous result.
        reload_choice = str(input("Type 'y' to continue, or Type 'n' to start a new calculation: ")).lower()

        if reload_choice == "y":
            ask_num1 = result

        # TODO 4F: If no, program asks the user for the fist number again and wipes all memory of previous calculations.
        else:
            reload = False
            print("\n" * 20)
            print(logo)
            calculator()

calculator()
