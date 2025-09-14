
def generateParanthesis(current,p,c,n,result):

    if p == n and c ==n :
        result.append(current)
        return
    
    if p<n:
        generateParanthesis(current+"(",p+1,c,n,result)

    if c<p :
        generateParanthesis(current+")",p,c+1,n,result)


def generateParanthesisBrackets(current, p, c, bp, bc, n, m, result2, stack):
    # Optional: to trace the recursion
    print("STACK:", stack, "CURRENT:", current)
    
    if p == n and c == n and bp == m and bc == m:
        result2.append(current)
        return

    if p < n:
        generateParanthesisBrackets(current + "(", p + 1, c, bp, bc, n, m, result, stack + "(")

    if c < p and stack and stack[-1] == "(":
        generateParanthesisBrackets(current + ")", p, c + 1, bp, bc, n, m, result, stack[:-1])

    if bp < m:
        generateParanthesisBrackets(current + "{", p, c, bp + 1, bc, n, m, result, stack + "{")

    if bc < bp and stack and stack[-1] == "{":
        generateParanthesisBrackets(current + "}", p, c, bp, bc + 1, n, m, result, stack[:-1])
def getPairs(current,pp,pc,bp,bc,n,m,stack,arr):
    
    if pp ==  n and pc == n and bp == m  and bc== m:
        arr.append(current)
        return
    
    if pp<n:
        getPairs(current+"(",pp+1,pc,bp,bc,n,m,stack + "(",arr)
        
    if pc<pp  and stack[-1] == "(":
        getPairs(current+")",pp,pc+1,bp,bc,n,m,stack[:-1],arr)
        
    if bp<m:
        getPairs(current+"{",pp,pc,bp+1,bc,n,m,stack+"{",arr)
        
    if bc< bp and stack[-1] == "{":
         getPairs(current+"}",pp,pc,bp,bc+1,n,m,stack[:-1],arr)

result = []
result2 = []
n = 2
m= 2
stack  = ""
generateParanthesis("",0,0,n,result)
print(result)

#getPairs("",0,0,0,0,n,m,"",result2)


generateParanthesisBrackets("",0,0,0,0,n,m,result2,"")
print(result2)