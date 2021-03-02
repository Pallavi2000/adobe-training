#Print the number of pairs of {} if arranged properly

brackets = input("Enter a expression ")
open_count = close_count = 0

for bracket in brackets:
    if bracket == '{':
        open_count += 1
    else:
        close_count += 1 

    if open_count < close_count:
        break

if open_count == close_count:
    print("Expression is valid")
else:
    print("Expression is invalid")