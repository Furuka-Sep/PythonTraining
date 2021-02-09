import random
print('～数あてゲーム～3桁の数を当ててください')
cont=True
answer=[random.randint(0,9) for i in range(3)]
while cont==True:
    hit=0
    ball=0
    prediction=list()
    for i in range(3):
        prediction.append(int(input('{}桁目の予想を入力[0~9]>>'.format(i+1))))
        if prediction[i]==answer[i]:
            hit+=1
        else:
            for j in range(3):
                if prediction[i]==answer[j]:
                    ball+=1
    if hit==3:
        print('正解です!')
        cont=False
    else:
        print('{}ヒット!{}ボール!'.format(hit,ball))
        n=int(input('続けますか？1:続ける 2:終了'))
        if n==2:
            print('正解は{}{}{}でした'.format(answer[0],answer[1],answer[2]))
            cont=False


