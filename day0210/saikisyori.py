def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)
x=int(input('大きい方の整数を入れてください'))
y=int(input('小さい方の整数を入れてください'))
num=gcd(x,y)
print('最大公約数は{}です'.format(num))
