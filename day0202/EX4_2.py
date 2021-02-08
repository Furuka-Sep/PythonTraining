count=1
print('カレーを召し上がれ')
ans=True
while ans==True:
    print('{}皿のカレーを平らげました'.format(count))
    key=input('おかわりはいかがいたしますか？(y/n)>>')
    if key == 'y':
       count+=1
    else:
      ans=False
print('ごちそうさま')
