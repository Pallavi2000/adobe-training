#Find smallest digit in a number

number = int(input("Enter a number "))
temp = number
smallest = None

while number != 0:
    remainder = number % 10
    number //= 10

    if smallest == None or remainder < smallest:
        smallest = remainder

print("The smallest digit of the given number",temp,"is",smallest)