import pprint
H=10
W=10
data=[[0]*W]*H
pprint.pprint(data)
#使用しているアドレスが同じなのでdata[0][2]=3等にしたら
#data[i][2]は全て3になってしまう
