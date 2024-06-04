import random as r
z=-1
i=0
lalp="abcdeffghijklmnopqrstuvwxyz"
ualp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
special="`~!@#$$%^&*-_=+,<>/?';:|"
password=""

print("Welcome to password generator.")
print("this program creates a strong password accoding to your needs.\n")
while(z<0):
    mini=int(input("Enter minimum number of characters required : "))
    maxi=int(input("Enter maximum number of characters allowed : "))
    z=maxi-mini
    if(z<0):
        print("Maximum length cannot be less than minimum length.\n Enter again - ")
size=r.randint(mini,maxi)
c1=int(input("Do you want to use both upper and lower case letters in your password ?\nENTER '1' FOR 'YES'\nENTER '2' FOR 'NO'\nEnter your choice : "))
c2=int(input("Do you want to use numbers in your password ?\nENTER '1' FOR 'YES'\nENTER '2' FOR 'NO'\nEnter your choice : "))
c3=int(input("Do you want to use special characters in your password ?\nENTER '1' FOR 'YES'\nENTER '2' FOR 'NO'\nEnter your choice : "))
while(i<size):
    x=r.randint(1,4)
    if(x==1):
        password+=lalp[r.randrange(0,(len(lalp)-1))]
        i+=1
    elif(x==2):
        if(c1==1):
            password+=ualp[r.randrange(0,(len(ualp)-1))]
            i+=1
        elif(c1==2):
            continue
    elif(x==3):
        if(c2==1):
            password+=num[r.randrange(0,(len(num)-1))]
            i+=1
        elif(c2==2):
            continue
    elif(x==4):
        if(c3==1):
            password+=special[r.randrange(0,(len(special)-1))]
            i+=1
        elif(c3==2):
            continue
print(f"Password generated  :  {password}")