userinfo=input('名前と血液型を","で区切って1行で入力>')
[name,blood]=userinfo.split(',')
blood=blood.upper().strip()
print('{}さんは{}型なので献血対象ではありません'.format(name,blood))

for s in('Hello'):
    print (s)
