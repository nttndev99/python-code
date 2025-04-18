def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

numberp = int(input("Press Number: "))
print(odd_or_even(numberp))
