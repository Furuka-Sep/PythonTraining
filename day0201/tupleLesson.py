tuple1=(3,5,7)#変更不可
print(len(tuple1))#3
print(tuple1[1])#5
print(sum(tuple1)) #15
list1=list(tuple1)
print(list1)
list1.append(10)
print(list1)

a,b,c=tuple1#a=3 b=5 c=7
print(a,b,c)
x=10
y=20
x,y=y,x
print(x)#20
