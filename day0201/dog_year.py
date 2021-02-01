"""
print('犬の名前を入力してください>')
dog_name=input()
print(dog_name,'と入力されました')
"""
"""
dog_name=input('犬のなまえを入力してください>')
print(dog_name,'と入力されました')
"""
dog_name=input('犬のなまえを入力してください>')
dog_age=input('犬のねんれいを入力してください>')
#human_age=dog_age*7 inputで受け取った値は文字として扱われる為、intに変換
human_age=int(dog_age)*7
print(dog_name,'は',dog_age,'さいです。これは人のねんれいでいうと',human_age,'さいになります',sep='')
#sep=''によって","部分の半角スペースを消している
