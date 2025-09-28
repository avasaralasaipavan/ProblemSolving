def method1(current,str,start):

    print(current)

    for i in range(start,len(str)):
        current.append( str[i])
        method1(current,str,i+1)
        current.pop()

#method1([],['a','b','c'],0)
def string_combinations(processed: str, unprocessed: str):
    if not unprocessed:
        print(processed)
        return

    # Include the first character
    string_combinations(processed + unprocessed[0], unprocessed[1:])

    # Exclude the first character
    string_combinations(processed, unprocessed[1:])

## processed and unprocessed method

def method2(p,up):
    if not up:
        print(p)
        return 
    
    method2(p,up[1:])
    method2(p+up[0],up[1:])
   
    

method2("","abc")