import random
NPC=[1 if i==0 else 0 for i in range(5)]
PLAYER=[4 if i==0 else 1 for i in range(2)]
random.shuffle(NPC)
"""
for i in range(5):
    if i==0:
        NPC.append('皇帝')
        PLAYER.append('奴隷')
    else:
        NPC.append('市民')
        PLAYER.append('市民')
"""
for i in range(2):
    if i==0:
        PLAYER.append(4)
    else:
        PLAYER.append(1)

print('ようこそeカードゲームへ')
input('>>enter')
VoD=True
count=0

while VoD==True:
    count+=1
    print('{}戦目'.format(count))
    print('手持ちのカード:市民{}枚 奴隷{}枚'.format(PLAYER[0],PLAYER[1]))
    choice=int(input('カード選択:[市民]なら[0]、[奴隷]なら[1]を入力>>'))
    print('カードオープン!')
    input('>>enter')
    if choice==1 and NPC[count]==1:
        print('あなた：奴隷 PC:皇帝')
        print('あなたの勝ち！')
        print('Congratulation!!')
        VoD=False
    elif choice==1 and NPC[count]==0:
        print('あなた：奴隷 PC:市民')
        print('あなたの負け！')
        print('GAME OVER')
        VoD=False
    elif choice==0 and NPC[count]==1:
        print('あなた：市民 PC:皇帝')
        print('あなたの負け！')
        print('GAME OVER')
        VoD=False
    else:
        print('あなた：市民 PC:市民')
        print('引き分け！')
        PLAYER[0]-=1
