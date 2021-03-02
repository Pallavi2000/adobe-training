#Program to count perfect squares in an array

def checkPerfectSquares(n):
    rootNum = int(n ** 0.5)

    if rootNum * rootNum == n:
        return True
    else:
        return False

number_of_bills = int(input("Enter the number of bills "))
#bills_array = list(map(int, input("Enter the bill values ").split()))[:number_of_bills]
bills_array = []
count_of_bills = 0

for i in range(0,number_of_bills):
    bills_array.append(int(input()))
    if checkPerfectSquares(bills_array[i]):
        count_of_bills += 1

print("The count of bills which are perfect squares",count_of_bills)