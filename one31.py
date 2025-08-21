employees=[{"eid":1,"ename":"peep","email":"peeep111@gmail.com"}]
# male_employees=[]

# for emp in employees:
#     if emp['gender']=='male':
#         male_employees.append(emp)
def get_male_emp(emp):
  return emp['gender']=='Male'
male_employees=list(filter(get_male_emp,employees))
print(len(male_employees))