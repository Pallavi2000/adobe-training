#Program to find series of n + n(2) + n(3) + ... n(m)

m = int(input("Enter the value of m "))
number = int(input("Enter the number "))
sum_of_series = 0

for i in range(1, m + 1):
    sum_of_series += pow(number, i)

print("Sum of Series is ",sum_of_series)
