num1 = int(input("enter num 1 :"))
num2 = int(input("enter num 2 (as divider):"))

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print("The result of division is:", result)
