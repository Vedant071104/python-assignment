#Q.1) write the python function to remove the duplication element from given list
def removeDuplicates(l1):
    return list(set(l1))
#Q.2) write the python function 
def frequence(l1):
    l2=removeDuplicates(l1)
    dict={}
    for k in l2:
        dict[k]=l1.count()
        return dict
#Q.3)
def abstractnumberfromText(Text):
    num=[]
    for word in Text.split(" "):
        for i in word.split(","):
            if type(eval(i))==int or type(eval(i))==float:
                num.append(float(i)) 
                return num

#Q.4)
    



