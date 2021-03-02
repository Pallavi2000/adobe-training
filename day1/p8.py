# Program to find count of prime digits in it

number = int(input("Enter a number to find count of prime digits in it : "))
tempNum = number

count_of_prime = 0

def check_prime(rem_num):

    # if rem_num == 1:
    #     flag = 0
    #     return flag
    for i in range(2,(rem_num // 2) + 1):
        
        if rem_num % i == 0:
            flag = 0
            break
        else:
            flag = 1
    return flag
           
    
while number != 0:
    remainder = number % 10
    number = number // 10

    result = check_prime(remainder)
    if result == 1:
        count_of_prime += 1

print(count_of_prime)