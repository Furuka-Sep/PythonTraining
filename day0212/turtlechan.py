import turtle
t=turtle.Turtle()
t.shape('turtle')
leng=500
while True:
	n=int(input('カメちゃんに何角形を描いてもらう?(3以上の半角整数)>>'))
	if n==0:
		turtle.bye()
		break
	t.clear()
	angle=360/n
	for i in range(n):
		t.left(angle)
		t.forward(leng/n)
print('bye')
