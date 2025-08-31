def findDepth(strr):
    flag = 0 
    
    temp = 0
    for i in strr:
        if i == "(":
            temp+=1
        if i == ")":
            flag =  max(flag,temp)
            temp -= 1
    return flag


print(findDepth("(1+(2*3)+((8)/4))+1"))


