"""
for i in range(1,10):
    if i % 2==0:
        continue
    for j in range(1,10):
        print(i*j,end=',')
        if i*j >50:
            break
    print()
print()
"""
height=int(input('何段の階段を作る?>'))
for i in range(height):
    for j in range(i+1):
        print('*',end='')
    print()
