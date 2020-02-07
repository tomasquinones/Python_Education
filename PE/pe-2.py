#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

x = 1
y = 1
total = 0
sequence = [1,1]

# First, figure out the entire Fibonacci sequence up to 4000000
while total < 4000000:
    total = x + y
    x = y
    y = total
    sequence.append(total)
    print(sequence)

evenTotal = 0
## Second, add up the even terms of the Fibonacci sequence
for term in sequence:
    if term % 2 == 0:
        evenTotal += term
        print(evenTotal)

""" This ended up solving problem 2, but it could probably be refactored into one loop """

