# '''
# 1 for snake
# -1 for water
# 0 for Gun
# '''

# import random


# computer = random.choice([-1,0,1])

# youstr = input("Enter your choice: ")
# youdict = {"s" : 1, "w" : -1,"g" : 0}
# reversedict = {1 :"Snake", -1 : "Water", 0 :"Gun"}

# you = youdict[youstr]
# print(f"You chose {reversedict[you]} \n Computer chose {reversedict[computer]}")


# if (you == computer):
#     print("It's a draw!")

# '''

# else:

#     if (you == -1 and computer== 0): # Water vs Gun
#         print("You Lose!")

#     elif (you == -1 and computer== 1): # Water vs Snake
#         print("You Won!")

#     elif (you == 1 and computer== 0): # Snake vs Gun
#         print("You Lose!")

#     elif (you == 1 and computer== -1): # Snake vs Water
#         print("You Won!")

#     elif (you == 0 and computer== -1): # Gun vs Water
#         print("You Lose!")

#     elif (you == 0 and computer== 1): # Gun vs Snake
#         print("You Won!")

#     else:
#         print("Something went wrong!")
        
# '''
 
# elif((computer-you) ==-1 or(computer - you) == 2):
#     print("You Lose!")

# else:
#     print("You Won!")