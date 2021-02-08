import turtle
import random
t1=turtle.Turtle()
t1.shape('turtle')
t1.color('blue')
t2=turtle.Turtle()
t2.shape('turtle')
t2.color('red')
t3=turtle.Turtle()
t3.shape('turtle')
t3.color('green')

def make_square(t1,t2,t3):
	for i in range(4):
		t1.forward(random.randint(20,70))
		t1.right(random.randint(10,350))
		t2.forward(random.randint(20,70))
		t2.right(random.randint(10,350))
		t3.forward(random.randint(20,70))
		t3.right(random.randint(10,350))
def make_spiral(t1,t2,t3):
	for i in range(36):
		make_square(t1,t2,t3)
		t1.right(random.randint(1,359))
		t2.right(random.randint(1,359))
		t3.right(random.randint(1,359))
make_spiral(t1,t2,t3)
t1.right(random.randint(1,359))
t2.right(random.randint(1,359))
t3.right(random.randint(1,359))
make_spiral(t1,t2,t3)
turtle.mainloop()
