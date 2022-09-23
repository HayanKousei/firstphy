import sys

try:
    x = (input("x: "))
    y = (input("y: "))
except ValueError:
    print("Error, invalid input")
    sys.exit(1)

try:
    result = (int(x) / int(y)) 
except ZeroDivisionError:
    print("Error, Cannot divide by zero")
    sys.exit(1)

print(f"{x} / {y} = {result}")