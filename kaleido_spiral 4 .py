import turtle
from iter tools import cycle

colors= cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_shape(size,angle,shift,shape):
	turtle.pencolor(next(colors))
	next_shape=''
	if shape=='circle':
		turtle.circle(size)
		next_shape='square':
			for 1 in range(4):
				turtle.forward(size.2)
				turtle.left(90)
			next_shape='circle'
		turtle.right(angle)
		turtle.forward(shift)
		draw_shape(size+5,angle+1,shift+1,
		next_shape)
turtle.bg color('black')
turtle.speed('fast')
turtle.pen size(4)
draw_shape(30,0,1,'circle')
