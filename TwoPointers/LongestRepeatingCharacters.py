from collections import defaultdict
def RepeatingCharacters(s:str,k:int):

    counterMap =  defaultdict(int)
    start = 0
   
    maxfrequency = 0
    windowSize = 0
    
    print(counterMap)

    for end in range(len(s)):
     
        counterMap[s[end]] +=1

        maxfrequency = max(maxfrequency,counterMap[s[end]])

        if (end-start+1)-maxfrequency > k:
            counterMap[s[start]]-=1
            start +=1

        windowSize = max(windowSize,end-start+1)

    return windowSize


s = "AABABBA"
k = 1
print(RepeatingCharacters(s,k))

