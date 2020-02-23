# list comprehensions

print("This prints the squares for numbers 1-10")
squares = [value**2 for value in range(1, 11)]
print(squares)

print("This counts to 20 inclusive")
count20 = [value for value in range(1, 21)]
print(count20)

print("This counts to one million by 100s")
oneMillionByTen = [value for value in range(1, 1000001, 100)]
print(oneMillionByTen)

