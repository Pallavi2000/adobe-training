#Program to find sum of digit

number = int(input("Enter a number "))
temp = number
sum_of_digit = 0

while number != 0:
    remainder = number % 10
    number //= 10
    sum_of_digit += remainder 

print("The sum of the digit of the given number",temp,"is",sum_of_digit)