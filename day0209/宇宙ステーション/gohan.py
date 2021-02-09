import random
menu={'青ピクミン':200,'パンモドキ':240,'葉チャッピー':200,'コガネモチ':300,'ペレット草':50}
money=random.randint(1000,2000)
while True:
    print('メニュー表')
    n=0
    for i in menu.items():
        print('{} {} 円'.format(n,i))
        n+=1
    else:
        break
