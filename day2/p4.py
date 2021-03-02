#Program to print nth term of combined series

def printFiboTerm(n):
    if n == 1:
        return 1

    elif n == 2:
        return 2

    else:
        fib1 = 1
        fib2 = 2

        for i in range(3,n + 1):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
    
        return fib3

def printPrimeTerm(n):
    if n == 1:
        return 2

    i = 3
    count = 1

    while count < n:
        flag = True
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                flag = False
                break
    
        if flag:
            count += 1
    
        i += 1
    
    return (i - 1)


number = int(input("Enter a number "))

if number % 2 == 0:
    print("The fibo term is ", printFiboTerm(number // 2))

else:
    print("The prime term is ", printPrimeTerm((number // 2) + 1))