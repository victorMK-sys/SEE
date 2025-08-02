print("This is a simple calculator program")

num1 = int(input("Enter your first operant: "))
num2 = int(input("Enter the second operant: "))
operation = input("Choose an operation to perform (+, -, *, /): ")

if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2
  
print(f"{num1} {operation} {num2} = {result}")