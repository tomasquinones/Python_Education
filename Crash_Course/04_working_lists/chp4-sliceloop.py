# looping through a slice() on a list

myList = ['franklin', 'washington', 'lincoln', 'obama', 'reagen', 'clinton']

print("Here are the first three presidents of my list")

for president in myList[:3]:
    print(president.title())
