'''
USAGE:fetch all users
API URL:https://jsonplaceholder.typicode.com/users
Method:GET
Required Fields: None
Access Type:P
'''
# import requests
# API URL:https://jsonplaceholder.typicode.com/users
# response= requests.get()



### import requests
#api_url='https://jsonplaceholder.typicode.com/users'
#response=requests.get(api_url)

#print(response)

#users=response.json()
#print(users)


import requests

api_url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(api_url)
print(response)  # This prints the response object (like <Response [200]>)

users = response.json()  # Converts JSON response to a Python list
print(users)  # This prints the list of users
