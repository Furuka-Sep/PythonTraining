def eat(breakfast, lunch='ラーメン',dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))
eat('納豆ご飯','ラーメン','カレーうどん')#<BAD
eat(breakfast='納豆ご飯',dinner='カレーうどん')
eat(dinner='カレーうどん',breakfast='納豆ご飯')
eat('納豆ごはん',dinner='カレーうどん')
#eat(dinner='カレーうどん','納豆ごはん')
#error:キーワードの無い物を後に持ってきてはダメ。
