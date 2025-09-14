from typeguard import typechecked

@typechecked
def Combinations(p:str,up:str):

    if  len(up) == 0: 
        print(p)
        return
    
    ch = up[0]
    #print("The ch is : ",ch)
    for i in range(0,len(p)+1):
        f = p[0:i]
        s =  p[i:]
        #print(ch+f+s)
        Combinations(ch+f+s,up[1:])

Combinations("","abc")