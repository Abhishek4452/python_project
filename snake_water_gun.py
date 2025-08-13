
import random
def comp(computer):
    if computer == 1:
        print("computer = snake ")
    elif computer ==2:
        print("computer = water ")
    else:
        print("computer = gun")

def result(a,b):
    #matrix
    mat = [[0,1,-1],[-1,0,1],[1,-1,0]]

    if mat[a][b]== 0:
        print(" GAME DRAW !!! ")
    elif mat[a][b]== 1:
        print(" YOU WIN !!!")
    else:
        print(" YOU LOSS !!!")

print('           welcome to snake water gun  game                 ')
#            s w g
#computer =   
#user = s    d w l
#       w    l d w 
#       g    w l d 


print("SNAKE  = 1 \nWATER = 2 \nGUN =3 ")
user = int(input("enter input :"))

choice =[1,2,3]
computer = random.choice(choice)
comp(computer)


result(user-1,computer-1)

