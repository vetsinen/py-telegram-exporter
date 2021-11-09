import pickle

with open('opensupport.pickle', 'rb') as f:
    users = pickle.load(f)
# print(users)
print(len(users))

for user in users:
    if user['phone']:
        print(user['first_name'], user['phone'])
