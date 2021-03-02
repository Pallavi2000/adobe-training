#Program to find series of 1 - n + n(2) - n(3) + n(4) + ..... +/- n(m)

m = int(input("Enter the value of m "))
number = int(input("Enter the number "))
sum_of_series = 1

for i in range(1, m + 1):
    if i % 2 != 0:
        sum_of_series -= pow(number, i)
    else:
        sum_of_series += pow(number, i)

print("Sum of Series is ",sum_of_series)
