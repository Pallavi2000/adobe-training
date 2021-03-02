#Program to find the count of digits in a number

number = int(input("Enter a number "))
temp = number
count = 0

while number != 0:
    remainder = number % 10
    number //= 10
    count += 1

print("The count of digit of the given number",temp,"is",count)