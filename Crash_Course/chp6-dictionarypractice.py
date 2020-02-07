# practicing with dictionaries

my_bikes = {
    'hard tail' : 'salsa',
    'fat bike' : 'surly',
    'folding' : 'brompton',
    'touring' : 'masi',
    }

print(my_bikes)

print(f"my mountain bike is a {my_bikes['hard tail']}")

for key, value in my_bikes.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")
    