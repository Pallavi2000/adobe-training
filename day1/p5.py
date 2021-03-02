#Find biggest digit in a number

number = int(input("Enter a number "))
temp = number
biggest = None

while number != 0:
    remainder = number % 10
    number //= 10

    if biggest == None or remainder > biggest:
        biggest = remainder

print("The biggest digit of the given number",temp,"is",biggest)