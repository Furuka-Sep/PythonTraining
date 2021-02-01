dict1=dict() #空のdict
dict1['apple']='りんご'
dict1['orange']='オレンジ'
print(dict1)

print(len(dict1)) #2
dict1['banana']='ばなな'

del dict1['orange']
print(dict1)

print(dict1['apple']) #りんご

#print(dict1['pine']) #error
print(dict1.get('pine'))#None

if'apple' in dict1:
    print('あるよ')

if 'pine' not in dict1:
    print('ないよ')

if 'りんご' in dict1.values():
    print('あるよ')
