print('さぁ、眠りましょう？')
"""
count=0;
count+=1
print('ひつじが{}匹'.format(count))
count+=1
print('ひつじが{}匹'.format(count))
count+=1
print('ひつじが{}匹'.format(count))
print('おやすみ')
"""
"""
count=0
while count <3:
    count += 1
    print('ひつじが{}匹'.format(count))
print('おやすみ')
"""
is_awake=True
count=0
while is_awake == True:
    count+=1
    print('ひつじが{}匹...'.format(count))
    if count >=5:
        key=input('もう眠れそう？(うん：まだ...)')
        if  key=='うん':
            is_awake= False
print('おやすみなさい...')
