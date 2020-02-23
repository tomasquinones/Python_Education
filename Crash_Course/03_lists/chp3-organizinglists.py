# organizing a List

myThings = ['bicycles', 'books', 'art supplies', 'camping gear', 'musical instruments', 'clothing', 'tools']

# using the sorted() method instead of sort()

print('here is the original list')
print(myThings)
print('This is sorted temporarily')
print(sorted(myThings))
print('Here is the original lists again')
print(myThings)



# using the sort() method permanently sorts the List

print(myThings)
print('now sorted alphabetical')
myThings.sort()
print(myThings)

print('now sorted reverse alpha')
myThings.sort(reverse=True)
print(myThings)
