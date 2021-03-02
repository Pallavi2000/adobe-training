#To find maximum maney earned by shreya and mom

numberOfShoePairs = int(input("Available shoe pairs "))
requiredShoePairs = int(input("Minimum shoe pairs can cary by the shreya and mom "))
shoePrices = list(map(int, input().split()))
moneyEarned = None

shoePrices.sort()

for i in range(0, requiredShoePairs):
    if shoePrices[i] < 0:
        if moneyEarned == None:
            moneyEarned = shoePrices[i] * -1
        else:
            moneyEarned += (shoePrices[i] * -1)
    else:
        if moneyEarned == None or moneyEarned < 0:
            break
        else:
            moneyEarned -= shoePrices[i] 

if moneyEarned != None and moneyEarned > 0:
    print("Money Earned by shreya and her mom",moneyEarned)
else:
    print("Not able to earn money")