# draws a tree
import turtle

# set the canvas window
def set_canvas():
    s = turtle.Screen()     
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s

# set a turtle (a pen)
def set_pen(color):         
    t = turtle.Turtle()
    t.shape('turtle')  
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=10)
    return t

# draw a tree fractal using recursion
def draw_tree(t, branch, angle, n):
  if n > 0:
        t.pensize(n)
        t.forward(branch)
        length = branch * 0.9
        t.left(angle)
        draw_tree(t, length, angle, n-1)
        t.right(angle * 2)
        t.pensize(n)
        t.forward(branch/10)
        draw_tree(t, length, angle, n-1)
        t.pensize(n)
        t.left(angle)
        t.backward(branch*1.1)
  else: 
        t.forward(10)
        t.backward(10)
        t.pencolor('green')
        t.pensize(20)
        t.forward(2)
        t.backward(2)
        t.pencolor('brown')

# main program
if __name__ == '__main__':
    s = set_canvas()
    t = set_pen('brown')
    t.penup()
    t.goto(-45, -150)
    t.left(90)
    t.pendown()
    draw_tree(t, 60, 20, 6)
    turtle.exitonclick()
