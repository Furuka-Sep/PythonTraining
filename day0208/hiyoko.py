import random
n=int(input('仕分けるひよこの数を入力してください>'))
hiyoko=[random.randint(1,2) for _ in range(0,n)]
hit=0
for i in range(n):
    print('ひよこ仕分け開始')
    choice=input('ひよこ{}は雌雄どちらですか?雄:y/雌/n>>'.format(i+1))
    if choice=='y' and hiyoko[i]==1:
        print('○')
        hit+=1
    elif choice=='n' and hiyoko[i]==2:
        print('○')
        hit+=1
    else:
        print('×')
print('お疲れ様です。全てのひよこを仕分けました！')
print('あなたは{}匹中{}匹のひよこを正確に仕分けることが出来ました!'.format(n,hit))
