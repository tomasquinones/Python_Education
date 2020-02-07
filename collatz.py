
def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(str(number))
        


print('Enter number:')
myNumber = ''


while myNumber != int():
    try:
        myNumber = int(input())
        collatz(myNumber)
        break
    except:
        print('Error, you must enter an integer.')


