# Chapter 7 Even or Odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
elif number % 3 == 0:
    print(f"\nThe number {number} is divisible by 3, therefore, Odd")
else:
    print(f"\nThe number {number} is odd.")

