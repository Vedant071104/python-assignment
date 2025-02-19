#write the python script to print all the distinct element from the list. use set to solve the problem.
l1=[20,30,10,40,20,69,54,69,20,10,50,40]
print(set(l1))


# creat a two set from given set of number to seperate the even odd number.

s1={10,23,45,64,77,48,21,12,90,100}
oddset=set()
evenset=set()
for e in s1:
    if e%2:
        oddset.add(e)
    else:
        evenset.add(e)
        print("even number:-",evenset,"odd number:-",oddset)




# give a set of five player name. write the pyton script to form all the possible
#pair of player that is selecting two player at a time.

S2={"rohit","ruturaj","virat","jasprit","surya"}
p1=list(S2)
for i in range(4):
     for j in range(i+1,5):
         print(p1[i],p1[j])
         
# you have list of  name of candidate some of them wearing red cap some of them wearing 
# black shoes and some of them wearing both now tou have to give the ist of name of the candidate 
# wearing black shoes thei is another list wearing red cap. write the pyhon script to find out name 
# of student wearing redcap and blackshoes.

blackshoes=["a","b","c","d","e",]
redcap=["a","g","h","l","b","f","r"]
for c in set(blackshoes).intersection(set(redcap)):
    print(c)
    
# write he pyhon script to creat tha tuple weare each tuple has two element representing dise upper 
# face number take number n input from input and generate all possible tuple in a such way that tuple 
# element sums to n.
N=int(input("enter the number"))
s1=set()
if N>=2 and N<=12:
    for i in range(1,7):
        for j in range(1,7):
            if i+j==N:
                s1.add(i,j)
print(s1)
    



        
        


