def welcome(u):
    print('ようこそ{}さん'.format(u['name']))
    u['age'] = u['age']+1
    print('あなたは来年{}歳ですので凶です'/format(u['age']))
username=input('名前を入力してください>>')
userage=int(input('ねんれいを入力してください>>'))
user={'name':username,'age':userage}
copied_user=user.copy()
welcome(copied_user)
