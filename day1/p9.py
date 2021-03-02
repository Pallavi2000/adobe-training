# Program to find sum of odd placed digits in a number

inputNum = int(input("Enter a number : "))
tempNum = inputNum
flag = True #for odd placed
sum1 = 0
sum2 = 0

while(tempNum != 0):
    remainder = tempNum % 10
    tempNum = tempNum // 10
    
    if remainder % 2 == 0:
        if flag:
            sum1 += remainder
        else:
            sum2 += remainder
    flag = not flag

# if flag:
#     print("Sum of odd placed even digits : ",sum1)
# else:
#     print("Sum of odd placed odd digits : ",sum2)

print("Sum of odd placed even digits : ",sum1)
print("Sum of odd placed odd digits : ",sum2)