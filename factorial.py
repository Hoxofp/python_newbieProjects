factorial = int(input("Enter the number that you want to find its factorial: "))
total = 1
while factorial > 1:
    total = total * factorial
    factorial = factorial - 1
print(total)
