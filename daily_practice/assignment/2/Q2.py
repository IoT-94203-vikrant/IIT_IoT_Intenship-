num = int(input("Enter 5 digit number:"))
rev = 0
temp = num      
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print(f"{temp} is a palindrome")
else:
    print(f"{temp} is not a palindrome")

