num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


def operator():
    print("Choose your operator (+ , - , * , /)")
    op = input("Enter Operator: ")
    return op

def calculate():
    op = operator()
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        print("Please enter correct operator!")
        return calculate()


print("Answer: " + str(calculate()))
