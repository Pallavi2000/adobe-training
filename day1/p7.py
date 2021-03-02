# Program to find palindrome or not 

number = int(input("Enter a number to find palindrome or not : "))
tempNum = number
reverse = 0
while number != 0:
    remainder = number % 10
    number = number // 10
    reverse = reverse * 10 + remainder

if(reverse == tempNum):
    print(tempNum," is a palindrome")
else:
    print(tempNum," is not a palindrome")