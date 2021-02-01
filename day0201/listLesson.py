list1=[]
list2=list() #おなじ意味

list1.append(3)
print(list1)
list1.append(5)
print(list1[1])

list2.append(10)
list2.append(20)
print(list2)

list3=list1+list2
print(list3)

list4=list3*3
print(list4)

print(len(list4)) #12
print(sum(list4)) #合計114

del list4[0]
print(list4)

list4.remove(5) #見つけた最初の一つを削除
print(list4)

list5=list4[3:8]
print(list5)

print(list5[-1]) #最後の要素
