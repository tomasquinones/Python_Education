# testing string splitting


user_url = 'https://ridewithgps.com/users/45898/'
user_id = user_url.split('/')

print(f"user_id: {user_id}")

for x in user_id:
    if x == '':
        user_id.remove(x)

user_id = user_id[-1]

print(f"user_id: {user_id}")