



#Q.1) write the python script to take input from user. give them three chance to enter
#     to print even number if user enter even number under three chance print "you win"
#     if user get more then three chance to print even number then print "you loss". 
n=int(input("enter even number in three chance"))
i=1
while i<=3:
    print(n)
    if n%2==0:
        print("you win")
        break
    i+=1
if i==4:
    print("you lose")
        