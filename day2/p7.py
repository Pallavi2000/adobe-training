#Checking expression is valid or not using stack

brackets = input("Enter a expression ")
stack = []
flag = True
for bracket in brackets:
    if bracket == '{' or bracket == '(' or bracket == '[':
        stack.append(bracket)
    else:
        if bracket == '}' and stack.pop() != '{':
            flag = False
            break
        elif bracket == ')' and stack.pop() != '(':
            flag = False
            break
        elif bracket == ']' and stack.pop() != '[':
            flag = False
            break

if flag and len(stack) == 0:
    print("Valid Expression")
else:
    print("Invalid Expression")


#2nd method
brackets = input("Enter a expression ")
stack = []
flag = True
for bracket in brackets:
    if bracket == '{':
        stack.append('}')
    elif bracket == '(':
        stack.append(')')
    elif bracket == '[':
        stack.append(']')
    else:
        if bracket != stack.pop():
            flag = False
            break

if flag and len(stack) == 0:
    print("Valid Expression")
else:
    print("Invalid Expression")
