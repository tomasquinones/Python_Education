import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentreate and ask again',
    'My reply is no'
    'Outlook not so good',
    'Very doubtful']

print('Ask a Question, Press Enter')
keyPress = input()
print(messages[random.randint(0, len(messages) - 1)])
