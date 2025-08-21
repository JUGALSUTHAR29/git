import csv,json
fp1=open('user_data.json','r')
user_data=json.load(fp1)
print(user_data)
users=user_data['users']
print(len(users))


import csv,json
fp1=open('user_data.json','r')
user_data=json.load(fp1)
users=user_data['users']
#tranform
new_users=[]
for user in users:
    new_users.append({'userid':user['id'],
                      'fname':user['firstName'],
                      'age':user['age'],
                      'gender':user['gender']
                      }
                     )

print(new_users)


json.dump(new_users,fp2)
print("new json file created")
fp1.close()
fp2.close()