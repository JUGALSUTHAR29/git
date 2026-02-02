# def login():
#         print('login success')

# login()
# login()
# list

# def add():
#         print('add')
# add()
# add(10,20,30)
#  type error: add()


# def add(a,b):
#         print(a+b)
# add(10,20)  #30
# add(1,2)  #3
# add("rahul","sanjay")   #rahulsanjay
# add(1)  #type error

# default arg
def calc(a,b,c=100):
        print(a+b+c)
calc(1,2,3)
calc(1,2)


# var length args
def sum(a,b):
        print(a,b)
sum(1,2,3)  #type error
sum(1,2)