print("Thise is Calculator Program")

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operator
print("Select an operator:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
operator = input("Enter the operator 1-5: ")

if operator == '1':
    result = num1 + num2
    operator_name = "Addition"
elif operator == '2':
    result = num1 - num2
    operator_name = "Subtraction"
elif operator == '3':
    result = num1 * num2
    operator_name = "Multiplication"
elif operator == '4':
    result = num1 / num2
    operator_name = "Division"
elif operator == '5':
    result = num1 % num2
    operator_name = "Modulus"
else:
    print("Invalid operator!")

#Result with the operator name
if result is not None and operator_name is not None:
    print(f"The result of {operator_name} is: {result}")
