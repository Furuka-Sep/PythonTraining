#1
for i in range(9):
    for j in range(9):
        print('{}*{}={}'.format(i+1,j+1,(i+1)*(j+1)))
#2
for i in range(9):
    if (i+1)%2==0:
        continue
    for j in range(9):
        print('{}*{}={}'.format(i+1,j+1,(i+1)*(j+1)))
#3
for i in range(9):
    if (i+1)%2==0:
        continue
    for j in range(9):
        if(i+1)*(j+1) > 50:
            break
        print('{}*{}={}'.format(i+1,j+1,(i+1)*(j+1)))
