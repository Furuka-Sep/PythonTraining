import random

#1
"""
num1=int(input('ダイス何回振る？...'))
list1=list()
for n in range(num1):
    list1.append(random.randint(1,6))
print(list1)
print('合計は{}でした'.format(sum(list1)))
"""
#2
"""
num2=int(input('ダイス何回振る？...'))
list2=list()
for n in range(num2):
    list2.append(random.randint(1,6))
print(list2)
print('出た目は{}の5種類'.format(set(list2)))
"""
#3
"""
num3=int(input('100~1000の範囲の偶数をいくつ生成する>>'))
list3=list()
for i in range(num3):
    list3.append(random.randrange(100,1000,2))
list3.sort()
print('{}個生成しました。降順に表示します{}'.format(num3,list3))
"""
#4
"""
user=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
list4=['グー','チョキ','パー']
pc=random.randint(0,2)
diff=(user+3-pc)%3
print('君は{},俺は{}'.format(list4[user],list4[pc]))
if user==pc:
    print('あいこじゃん')
elif diff==2:
    print('君の勝ち')
else:
    print('俺の勝ち')
"""
#5
"""
list5=list()
for i in range(1,100):
    list5.append(i)
random.shuffle(list5)
a=0;
b=0;
for i in range(5):
    a=list5[i]
    b=list5[i+1]
    if a > b:
        print('A:{},B:{}...Aの勝ち'.format(a,b))
    else:
        print('A:{},B:{}...Bの勝ち'.format(a,b))
    del list5[:1]
"""
#5 最適化?
"""
list5=list()
for i in range(1,100):
    list5.append(i)
random.shuffle(list5)
A=0;
B=0;
for i in range(5):
    a=list5.pop(0)
    b=list5.pop(0)
    if a > b:
        print('A:{},B:{}...Aの勝ち'.format(a,b))
        A+=1
    else:
        print('A:{},B:{}...Bの勝ち'.format(a,b))
        B+=1
win='';
if A > B:
    win='A'
else:
    win='B'
print('{}対{}で{}の勝ち'.format(A,B,win))
"""
#answer1
"""
import random
num=int(input('サイコロを何回ふる？>>'))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print('合計は',sum(dices),'でした')
"""
#answer2
"""
import random
num=int(input('サイコロを何回ふる?>>'))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print('出た目は',set(dices),'の',len(set(dices)),'種類')
"""
#answer3
"""
import random
num=int(input('100~1000の範囲の偶数をいくつ生成する>>'))
data=[random.randrange(100,1000,2) for _ in range(num)]
data.sort(reverse=True)
print(num,'個生成しました!降順に表示します',data)
"""
#answer4
"""
import random
while True:
	user=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
	pc=random.randint(0,2)
	hands=['グー','チョキ','パー']
	print(f'あなたは{hands[user]},PCは{hands[pc]}')
	if user==pc:
		print('あいこ')
		continue
	elif (user+3-pc)%3==1 :
		print('あなたの負け')
	else:
		print('あなたの勝ち')
	break
"""
#answer5
"""
import random
GAME_COUNT=5
balls=list(range(1,100))
random.shuffle(balls)
awin=bwin=0
for i in range(GAME_COUNT):
	print(f'{i+1}回戦')
	a,b=balls.pop(),balls.pop()
	if a>b:awin+=1;winner='A'
	else:bwin+=1;winner='B'
	print(f'A:{a},B:{b}...{winner}の勝ち')
print('{}対{}で{}の勝ち'.format(max(awin,bwin),min(awin,bwin),'A' if awin > bwin else 'B'))
"""
