#Program to find nth prime number

import os
number = int(input("Enter a number s"))

if number == 1:
    print("The ",number,"th prime number is 2")
    exit("Program Ends ..")

i = 3
count = 1

while count < number:
    flag = True
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            flag = False
            break
    
    if flag:
        count += 1
    
    i += 1

print("The ",number,"th prime number is ",(i - 1))
