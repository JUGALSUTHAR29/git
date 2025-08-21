# employees=[{'eid':101,'ename':'rahul g','gender':'male'},
#            {'eid':102,'ename':'priyanka g','gender':'female'},
#            {'eid':103,'ename':'ragiv g','gender':'male'},
#            {'eid':104,'ename':'soniya g','gender':'female'},
#            {'eid':105,'ename':'narendre m','gender':'male'},
#            ]
# for employee in employees:
#         print("ename:",employee['ename'])

        # del employee['ename']
        # print(employee)
        # crud operation use 
        # create
d1={}
emp={'eid':101,
             'ename':'rahul',
             'esal':45000,
             'email':'rg@gmail.com'}
        #read
print(d1)
print(type(d1))
print(emp)

        # how to read dict value?
        # using key

print(emp['eid'])         #101
print(emp['ename'])   #rahul
print(emp['loc'])   #key error

# update
emp['ename']='rahul godara'
print(emp)
emp['avail']=True
print(emp)
# daily learn one module at least

