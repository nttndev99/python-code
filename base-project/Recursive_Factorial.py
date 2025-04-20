def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1) * n

number = int(input("Input n number: "))
print(factorial(number))
