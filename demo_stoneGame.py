#Developer name : Mhaske Harshada satish
#Program name  : Stone paper scissors game
# date of performance : 9 August,2022
#Time  : 12:00 PM
#Under guidence of Mr.Amol Bhavsar Sir.

import random

stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

L=[stone,paper,scissors]
print("\n ----------------------------------------------^^^ Stone paper scissors Game ^^^-------------------------------------------------\n")
print("\n")
n=int(input("   How Many time you wanna play the game :"))

for i in range(n):
    user_choice=int(input(" Enter 0 for stone , 1 for paper and 2 for scissor ? :"))
    
    comp_choice=random.randint(0,2)
    print("     computer choice is : ",comp_choice)

    if (user_choice == comp_choice):
        print(f" your choice {L[user_choice]}\n computer choice {L[comp_choice]} \n game drop !!") 
    elif(user_choice==0 and comp_choice==1):
        print("your choice is stone ",L[user_choice],"computer choice is paper",L[comp_choice],"computer win !!") 
    elif(user_choice==0 and comp_choice==2):
        print("your choice is stone ",L[user_choice],"computer choice is scissors",L[comp_choice],"you win !!")
        
    elif(user_choice==1 and comp_choice==0):
        print(" your choice is paper ",L[user_choice]," computer choice is stone ",L[comp_choice]," \n you win !! ")
    elif(user_choice==1 and comp_choice==2):
        print(" your choice is paper ",L[user_choice]," computer choice is scissors ",L[comp_choice]," \n computer  win !! ")
        
    elif(user_choice==2 and comp_choice==0):
        print(" your choice is scissor ",L[user_choice]," computer choice is stone ",L[comp_choice]," \n computer win !! ")    
    elif(user_choice==2 and comp_choice==1):
        print(" your choice is scissor ",L[user_choice]," computer choice is paper ",L[comp_choice]," \n you win !! ")
        
    else:
         print("You enter invalid input try to give correct input and continue the game\n")
         continue
print("------------------------------------THANKS FOR PLAYING THE GAME-------------------------------------------------------------------------")

    

