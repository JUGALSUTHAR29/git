# str = "i am a programer i am learning python "
# print(str.endswith("hon "))


# str = "donsysy1112"
# # print(len(str))
# len = len(str)
# print(len)

# str = "hii,$ I am a programer $ how are you" 
# print(str.count("$"))


# marks = int(input("enter student marks : "))

# if marks >= 90:
#     grade = "A"
# elif marks >= 70 and marks < 90:
#     grade = "B+"
# elif marks >= 60 and marks < 70:
#     grade = "B"
# elif marks >= 36 and marks < 60:
#     grade = "C"
# else:
#     grade = "FAIL"

# print("grade of student =>", grade)



# ----------------------------
# ----------------------------



# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))

# # BMI calculation
# bmi = weight / (height ** 2)

# # Determine category
# if bmi < 18.5:
#     status = "Underweight"
# elif bmi >= 18.5 and bmi < 25:
#     status = "Normal weight"
# elif bmi >= 25 and bmi < 30:
#     status = "Overweight"
# else:
#     status = "Obese"

# # Output result
# print("Your BMI is:", round(bmi, 2))
# print("Health Status:", status)
# ------------------------------------
# # ------------------------------------

# list_of_movies_name=[]
# (list_of_movies_name.append(input("enter the first movie name: ")))
# (list_of_movies_name.append(input("enter the second movie name: ")))
# (list_of_movies_name.append(input("enter the third movie name: ")))
# print(list_of_movies_name)
# list1=[1,2,3]
# list2=[1,4,1]
# copylist2=list2.copy()
# copylist2.reverse()

# if(copylist2 == list2):
#         print("palindrom")
# else:
#         print("not palindrom")
        
# info = {
#         "name":'sanjiv',
#         "eid":101,
#         "esal":45000,
#         "loc":'banglore',
#         "pin_code":35555
# }
# print(info)
# ----------------------------
# ----------------------------


# import requests

# url = 'https://jsonplaceholder.typicode.com/users'


# response = requests.get(url)

# if response.status_code == 200:
#     users = response.json()  
#     print("Usernames:\n")
#     for user in users:
#         print(user['username'])
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")
# import requests

# url = 'https://fakestoreapi.com/products'
# response = requests.get(url)

# if response.status_code == 200:
#     products = response.json()
    
#     print("Beauty Products:\n")
#     for product in products:
#         if product['category'].lower() == 'jewelery':
#             print(f"- {product['title']}")
# else:
#     print("Failed to fetch data.")

import requests

url = 'https://fakestoreapi.com/products'
response = requests.get(url)

if response.status_code == 200:
    products = response.json()
    
    print("Beauty Products (Using while loop):\n")
    i = 0
    while i < len(products):
        product = products[i]
        if product['category'].lower() == 'jewelery':
            print(f"- {product['title']}")
        i =+ 1
else:
    print("Failed to fetch data.")
    
