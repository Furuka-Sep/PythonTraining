scores={70,80,55,80}
scores.add(80)
print(scores)
print('要素数は{}'.format(len(scores)))
print('合計は{}'.format(sum(scores)))

list1=[1,1,3,1,4,5,6,1,1,6,3,2,4]
print(len(set(list1)))#6

scores={'network':60,'database':80,'security':60}
members={'松田','浅木','工藤'}
print(tuple(members))
print(list(scores))
print(set(scores.values()))

dict1=dict(zip(['赤','緑','青'],['r','g','b']))
print(dict1)

matsuda_scores={'network':60,'database':80,'security':50}
asagi_scores={'network':80,'database':75,'security':92}
member_scores={
        '松田':matsuda_scores,
        '浅木':asagi_scores
}
print(member_scores['浅木']['security'])
print(len(member_scores))

member_hobbies={
        '松田':{'SNS','麻雀','自転車'},
        '浅木':{'麻雀','食べ歩き','数学','数学'}
}
print(member_hobbies)
print(member_hobbies['浅木'])

common_hobbies=member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies)

a=[1,2,3]
b=[4,5,6]
c=[a,b]

print(c)
print(c[0])
print(c[1][2])

A={1,2,3,4}
B={2,3,4,5}
print(A|B)#和集合
print(A&B)#積集合
print(A-B)#差集合
print(A^B)#対象差
