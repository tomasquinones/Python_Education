import os
os.chdir('./')

myFiles = os.getcwd()

print(str(os.listdir()))

helloFile = open('hello.txt', a)
helloContent = helloFile.read()
helloContent = 