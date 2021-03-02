#Program to find nth fibinocci number
number = int(input("Enter a number "))

if number == 1:
    print("The first fibinocci number is 1")

elif number == 2:
    print("The second fibinocci number is 2")

else:
    fib1 = 1
    fib2 = 2

    for i in range(3,number + 1):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    
    print("The ",number,"th fibinocci number is ",fib3)
