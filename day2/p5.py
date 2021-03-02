'''Print Series
    * * * * * * * * * * *
    * *               * *
    *   *           *   *
    *     *       *     *
    *       *   *       *
    *         P         *
    *       *   *       *
    *     *       *     *
    *   *           *   *
    * *               * *
    * * * * * * * * * * *
'''

number = int(input("Enter a odd number "))

for i in range(1, number + 1):
    if i == 1 or i == number:
        for j in range(1, number + 1):
            print("*", end =" ")
    else:
        for j in range(1, number + 1):
            if j == 1 or j == number:
                print("*", end =" ")
            else:
                if i == j and i == number // 2 + 1:
                    print("P", end = " ")
                elif i == j or j == number - i + 1:
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
    
    print("")