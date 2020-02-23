# Chapter 8 Python Crash Course Parrot

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True

while active: 
    message = input(prompt)
    if message == 'quit' or message == 'q':
        active = False
    else:
        print(message)

