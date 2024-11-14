# Ask the user to input two numbers and a mathematical operation
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the mathematical operation (+, -, *, /): ")

# Perform the operation based on the user's input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation!")

# Print the result
print(f"{num1} {operation} {num2} = {result}")