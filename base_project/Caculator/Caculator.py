
from art import logo

def  add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Todo: Add these 4 function into a dictionary as the values.
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# Todo: Use the dictionay operator to perform the caculator.
def calculator():
    print(logo)
    should_accumulate = True

    while should_accumulate:
        num1 = float(input("What is the first number?: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new caculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 10)
            calculator()
            
calculator()