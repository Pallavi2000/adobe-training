#Program to check if integer is a perfect square or not

number = int(input("Enter a number "))
rootNum = int(number ** 0.5)

if rootNum * rootNum == number:
    print(number,"is a perfect square number")
else:
    print(number, " is not a perfect square number")