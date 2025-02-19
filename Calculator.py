def extract_number_from_string(text):
    l=[]
    for t in text.split(" "):
        for e in t.split(","):
            try:
                l.append(float(e)) 
            except ValueError():
                pass
    return l

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

def hcf(a,b):
    H=a if a<b else b
    while H>=1: 
        if a%H==0 and b%H==0:
            return H
        H-=1
        
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
        
def sqrt(a):
    return a**0.5

def end():
    print("Thank you for using smart calculator")
    input("Press enter key to exit")
    exit()
    
def sorry():
    print("this instruction is beyond my ability")
    
    
operations0={'CLOSE':end,'END':end,'TERMINATE':end,'EXIT':end,'QUIT':end}
operations1={'SQUARE':sqrt}    
operations2={
    'PLUS':add,'SUM':add,'ADDITION':add,'ADD':add,'SUBTRACTION':sub,
    'SUBTRACT':sub,'MINUS':sub,'DIFFERENCE':sub,'PRODUCT':multi,'MULTIPLICATION':multi,
    'MULTIPLY':multi,'DIVIDE':div,'DIVISION':div,'LCM':lcm,'HCM':hcf}

def main():
    print("WELCOME TO THE SMART CALCULATOR")
    while True:
        print()
        text = input("enter any text:-\n")
        for word in text.split(" "):
            if word.upper() in operations2.keys():
                try:
                    l=extract_number_from_string(text)
                    r=operations2[word.upper()](l[0],l[1])
                    print("result is:-",r)
                except:
                    print("somthing is wrong please,try again")
                finally:
                    break
            elif word.upper() in operations0.keys():
                 operations0[word.upper()]()
                 break
            elif word.upper() in operations1.keys():
                l=extract_number_from_string(text)
                r=operations1[word.upper()](l[0])
                print("result is:-",r)
                break
        else:
            sorry()
            
if __name__=="__main__":
    main()
            