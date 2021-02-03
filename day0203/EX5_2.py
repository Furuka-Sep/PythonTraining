def is_leapyear(y):
    return(y % 400 == 0 or(y % 4 == 0 and y % 100 != 0))
current_year=int(input('現在の西暦を教えてください...'))
if is_leapyear(current_year):
    print('西暦{}年はうるう年です'.format(current_year))
else:
    print('西暦{}年はうるう年ではありません'.format(current_year))
