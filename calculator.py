def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': 'add', '-': 'subtract', '*': 'multiply', '/': 'divide'}

def calculator():
    num1 = float(input("What is the first number?: "))
    calculator_active = True
    while calculator_active == True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))

        if operation_symbol == '+':
            answer = add(n1=num1, n2=num2)
        if operation_symbol == '-':
            answer = subtract(n1=num1, n2=num2)
        if operation_symbol == '*':
            answer = multiply(n1=num1, n2=num2)
        if operation_symbol == '/':
            answer = divide(n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calculator_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to clear: ")
        if calculator_continue == 'y':
            num1 = answer
        elif calculator_continue == 'n':
            calculator_active = False
            calculator()

calculator()


