import pickle

with open('TropicanaBoltalka.pickle', 'rb') as f:
    users = pickle.load(f)
# print(users)
print(len(users))

for user in users:
    if user['contact']:
        print(user['first_name'], user['phone'], user['username'], user['id'])
