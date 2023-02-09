# One line If statement
a = 10
b = 13
#Ternary operator
print("a is greater") if a > b else print("b is greater")

if True:
    print("a")
else:
    print("b")

if False: print("b")
else: print("c")

print("a") if False else print("b")

number = 5
message = "Even" if number % 2 == 0 else "Odd"

print(message)

if number % 2 == 0:
    msg = "Even"
else:
    msg = "Odd"
print(msg)