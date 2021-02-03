#1~7の要素
x=[n for n in range(1,8)]
#[1,2,3,4,5,6,7]

#1~7の要素の2乗した値
x=[n**2 for n in range(1,8)]
#[1,4,9,16,25,36,49]

#1~7中偶数の要素
x=[n for n in range(1,8) if n % 2 == 0]
#[2,4,6]

#入れ子のfor
x=[i*10+j for i in range(1,3) for j in range(2,5)]
#[12,13,14,22,23,24]

#2次元リスト
x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
#[[17,18,19][27.28.29]]

#単位行列
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
#[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
