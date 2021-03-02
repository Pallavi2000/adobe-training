#Find sum of odd digits in a number

number = int(input("Enter a number "))
temp = number
sum_of_odd_digits = 0

while number != 0:
    remainder = number % 10
    number //= 10

    if remainder % 2 != 0:
        sum_of_odd_digits += remainder

print("The sum of odd digits of the given number",temp,"is",sum_of_odd_digits)