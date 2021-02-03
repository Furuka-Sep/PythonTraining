import pprint
#1
data=[[100-(i*10+j) for j in range(10)]for i in range(10)]
pprint.pprint(data)
#2
data2=[[]for i in range(5)]
pprint.pprint(data2)
#3
data3=[[i*10-j*10 for j in range(10)]for i in range(10)]
pprint.pprint(data3)
#4
data4=[[for j in range(5)]for i in range(5)]
