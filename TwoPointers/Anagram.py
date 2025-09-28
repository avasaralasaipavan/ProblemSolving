from collections import Counter


class Anagram:
    def isPermutation(self,str1,str2):

        return Counter(str1) == Counter(str2) 
    
    def getAnagrams(self,s,p,n):
        path = []

        windowSize = len(p)
        start = 0
        end = windowSize
       # n = len(s)
        while end<=n:
            if self.isPermutation(s[start:end],p) :
                path.append(start)
            start+=1
            end+=1
        return path

s = "baa"
p = "aa"
n= len(s)
st = Anagram()
print(st.getAnagrams(s,p,n))