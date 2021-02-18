import string
"""
num = int(input('幅>>'))
strlist = [chr(i) for i in range(97, 97+26)]
for i in range(len(strlist)//num+(len(strlist)%num)):
    print(strlist[i*num:i*num+num])
"""
"""
for i in range(len(al)):
    print(al[i],end='')
    if (i+1) % n == 0:
        print()
print()
"""
#
"""

for i,c in enumerate(al):
    print(c,end='')
    if(i+1) % n == 0:
        print()
print()
"""
#最強
n = int(input('幅'))
al = string.ascii_lowercase
data =[]
for i in range(0,len(al),n):
    letter = al[i:i+n]
    print(letter)
    data.append(letter)
n2 = int(input('何行目(1~{})>>'.format(len(data))))
print(data[n2-1])
