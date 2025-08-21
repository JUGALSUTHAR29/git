import csv 
fp=open('emp.csv','r')
emp_data=list(csv.reader(fp))

print(type(emp_data))
print(emp_data)

for emp in list(emp_data)[1:]:
    print(emp[1])

fp.close()