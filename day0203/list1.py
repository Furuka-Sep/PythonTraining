import pprint
#10個のインデックスを持つlistを10個格納したlistの生成
"""
data=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
print(data)
"""
W=10
H=10
data=list()
for i in range(H):
    temp=list()
    for j in range(W):
        temp.append(0)
    data.append(temp)
pprint.pprint(data)#みやすくなる
