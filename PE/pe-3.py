# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

all_primes = []
non_primes = []

original_number = 600851475143
# original_number = 13195

for number in range(1, original_number):
    if original_number % number == 0:
        non_primes.append(number)
    else:
        continue

print(f"Testing {original_number}")
print(f"Non Primes: {non_primes}")

