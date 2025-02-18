
print("1. ADD")
print("2. SUBTRACT")
print("3. DIVIDE")
print("4. MULTIPLY")
print("5. MODULUS")
print("6. POWER")

operation = int(input("Choose an operation: "))

if(operation in [1,2,3,4,5,6]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


if operation == 1:
    # Addition
    result = float(num1) + float(num2)

elif operation == 2:
    # Subtraction
    result = float(num1) - float(num2)

elif operation == 3:
    # Division
    result = float(num1) / float(num2)

elif operation == 4:
    # Multiplication
    result = float(num1) * float(num2)

elif operation == 5:
    # Modulus
    result = float(num1) % float(num2)

elif operation == 6:
    # Power
    result = pow(num1, num2)
else:
    print("Invalid operation")

print("The result of operation is {}".format(result))