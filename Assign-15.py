# Q.1) write the python script to print MysirG 5 time on screen
x=1
while x<=5:
    print("MysirG")
    x+=1

    
# Q.2) write the python script to print first 10 natural number.
x=1
while x<=10:
    print(x)
    x+=1
    
# Q.3) write the python script to print first 10 natural number in revers order.
a=10
while a>=1:
    print(a)
    a-=1
    
    
# Q.4) write the python script to print first 10 odd natural number.(1,3,5,7,9,11,13,15,17,19)
x=1
while x<=19:
    print(x)
    x+=2
    
# Q.5)write the python script to print first 10 odd natural number in revers order.
x=19
while x>=1:
    print(x)
    x-=2
    
    
a=1
while a>=3:
    print("Enter an even number")
    num=int(input())
    if num%2==0:
        print("You win")
        break
    a+=1
    if a==4:
        print("You loss")
     