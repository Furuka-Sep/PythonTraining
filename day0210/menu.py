import random
menu = ['ピクミン','チャッピー','コガネモチ',
        'ヘビガラス','オオパンモドキ','アメボウズ']
plice = [200,240,330,400,300,1]
money = random.randint(1000,2000)
while True:
    if len(menu) == 0:
        print('すべて売り切れました')
        break
    elif money < min(plice):
        print('もう一番安いメニューすら買えなくなってしまったようです')
        break
    else:
        print('メニュー表\n')
        for i in range(len(menu)):
            print('{} {} {}円'.format(i,menu[i],plice[i]))
        print('\n所持金{}円'.format(money))
        buy=int(input('購入したいご飯の番号を入力してください>'))
        if money-plice[buy] <= 0:
            print('\nお金が足りないようです\n')
            continue
        else:
            money-=plice.pop(buy)
            print('{}を購入しました\n'.format(menu.pop(buy)))
