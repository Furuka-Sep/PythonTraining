def eat(breakfast, lunch,dinner='イヌ',desserts=()):
    print('朝は{}を食べた!'.format(breakfast))
    print('昼は{}を食べた!'.format(lunch))
    print('夜は{}を食べた!'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べた!'.format(d))
eat('いぬ','犬','イヌ',('ねこ','INU','dog'))
