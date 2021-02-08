import random

ans=random.randint(1,100)
max_count=5

print('1~100の数字の中に正解が一つあります')
print('その数字を',max_count,'回以内に当てて頂きます')

for i in range(1,max_count+1):
    print(i,'回目です。回答をお願い致します')
    num=int(input())
    if num==ans:
        print('…お見事、正解です')
        break
    elif i==max_count:
        pass
    elif num > ans:
        print('残念ながら不正解です。')
        print('正解の数字はもっと低いようです')
    else:
        print('残念ながら不正解です。')
        print('正解の数字はもっと高いようです')
else:
    print('正解の数字は',ans,'でした。')
    print('あなたの負けで御座います')
