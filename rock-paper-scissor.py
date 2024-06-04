import random as ra
d={1:'ROCK',2:'PAPER',3:'SCISSOR'}
while(True):
    print("Let's play Rock-Paper-Scissor\nCHOOSE '1' FOR ROCK\nCHOOSE '2' FOR PAPER\nCHOOSE '3' FOR SCISSOR\nCHOOSE '4' TO EXIT\n")
    x=int(input("Enter your choice : "))
    if(x==4):
        print("\n\nThanks For Playing !\n\n")
        break
    r=ra.randint(1,3)
    print(f"\nYou chose {d[x]} , computer chose {d[r]}.\n")
    if(d[x]==d[r]):
        print("Its a tie\n")
        y=input("Enter any key to play again.")
    elif((x==1 and r==2)or(x==2 and r==3)or(x==3 and r==1)):
        print("YOU LOSE\n")
        y=input("Enter any key to play again.")
    else:
        print("YOU WON\nCONGRATULATIONS !\n")
        y=input("Enter any key to play again.")
    print("\n\n")
    

