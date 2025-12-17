
num = int(input("Enter a number: "))

binary_representation = ""

if num == 0:
    binary_representation = "0"
else:
    while num > 0:
        remainder = num % 2
        binary_representation = str(remainder) + binary_representation
        num = num // 2

print(f"The binary representation is {binary_representation}")