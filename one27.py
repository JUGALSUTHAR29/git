import json
fp1=open('user.json','r')
users=json.loads(fp1)
print(len(users))
print(type(users))
print(users)
