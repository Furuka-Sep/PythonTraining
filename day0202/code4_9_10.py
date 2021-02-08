#code4_9
"""
ages=[28,50,8,20,78,25,22,10,27,33]
num=5
samples=list()
for age in ages:
    if 20 <= age < 30:
        if len(samples) < num:
            samples.append(age)
print(samples)
"""
#code4_10
ages=[28,50,8,20,'にちゃい',78,25,22,10,27,33,'何歳に見える？']
num=5
samples=list()
for data in ages:
    if not isinstance(data,int):#intではない値が入っていた場合
        print('真面目に答えない輩が居たようです')
        continue #スキップして続ける
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples)
