import random
"""
list77=list(range(1,100+1))
print(list77)
for i in range(0,100)
    rnd1=random.randint(0,99)
    rnd2=random.randint(0,99)
    list77[rnd1]=list77[rnd2],list77[rnd2]=list77[rnd1]
"""
data=list()
for i in range(0,100):
    rnd=random.randint(1,100)
    data.append(rnd)
print(data)
for i in range(0,100):
    if data[i]==77:
        print('77->',i+1)
        break
    else:
        continue
else:
    print('77->なし')

"""
# コレクションを回しながら、カウンタ変数も使いたい場合
for i,num in enumerate(data):
    if num == 77:
        print('77->',i)
        break
else:
    print('77->なし')
"""
