# Adding Elements to Lists

myThings = ['Bicycles', 'books', 'art supplies', 'camping gear', 'musical instruments', 'clothing', 'tools']
print(myThings)

myThings.append('titanium cookware')
print(myThings)

print("insert into 3rd position - bags")
myThings.insert(2, 'bags')
print(myThings)

print("removing clothing")
#using del if you know the index position
del myThings[-2]

poppedThing = myThings.pop()
print(poppedThing)

#remove by pop at index

thirdPopped = myThings.pop(2)
print(thirdPopped)

print(myThings)
