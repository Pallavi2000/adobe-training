#Find the sum of odd elements

numberOfRequests = int(input("Enter number of requests "))
p = list(map(int, input("Enter Requsts ").split()))
sum_of_memory = 0

for i in range(0,numberOfRequests):
    if i % 2 == 0:
        sum_of_memory += p[i]

if sum_of_memory < 0:
    print("The number of memory deallocation",sum_of_memory)
else:
    print("The number of memory allocation",sum_of_memory)
