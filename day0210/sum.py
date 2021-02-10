def sumdata(n):#手続型pg
    s=[i+1 for i in range(n)]
    return(sum(s))
def sumdata2(n): #最適解 関数型pg
    return sum(range(1,n+1))
def sumdata3(n):#再起処理
    if n=1:
        return n
    else:
        return n+sumdata3(n-1)
n=int(input('正の整数>>'))
print(sumdata2(n))
