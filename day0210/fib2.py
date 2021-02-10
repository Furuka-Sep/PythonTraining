import time
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(20,41,5):
    start=time.time()
    result=fibo(i)
    end=time.time()
    duration=end-start
    print(i,result,duration)
