# "1) Solved question 1 by creating 2 virtual environments & installed packages from requirements.txt"


# # 2


# x = input("Please enter your name: ")
# y = int(input("Please enter your marks: "))
# z = int(input("Please enter your phone number: "))
# a = "The name of the student is {}, his marks are {} and phone number is {}".format(x,y,z)
# print(a)

'''
x = input("Please enter your name: ")
y = int(input("Please enter your marks: "))
z = int(input("Please enter your phone number: "))
a = "The name of the student is {0}, his marks are {1} and phone number is {2}".format(x,y,z)
print(a)
'''


# # 3


# table = [str(7*i) for i in range(1,11)]

# a = "\n".join(table)

# print(a)


# # 4


# def divisible_by_5(n):
#     if (n%5==0):
#         return True
#     return False

# a = [1,234,123,765,23456,76510575,3456775,654235,976763534456053423, 1065064003250]

'''Method 1'''

# r = list(filter(divisible_by_5, a))
# print(list(r))

'''Method 2'''

# r = filter(divisible_by_5, a)
# print(list(r))


# # 5


# from functools import reduce
# h = [1,24,12,76,26,75,37,65,93,10]


# def greater(a,b):
#     if (a>b):
#         return a
#     return b


# g = reduce(greater,h)

# print(g)


# # 6


# "Created 'Practice_set' virtual environment"
# "pip freeze > requirements.txt"
# "pip install -r .\requirements.txt"


# # 7

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# app.run()