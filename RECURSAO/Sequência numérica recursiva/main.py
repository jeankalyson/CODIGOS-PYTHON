def recursao(n,res):
    res.append(n)
    if(n==1):
        return
    elif(n%2==0):
        n=int(n/2)
        recursao(n,res)
    else:
        n=int(n*3+1)
        recursao(n,res)
n=int(input())
res = []
recursao(n,res)
print(*res)
