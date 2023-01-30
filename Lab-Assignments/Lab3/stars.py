from turtle import *

def star(size, n, d = 2):
    pendown()
    pencolor('red')
    pensize(5)
    for i in range(n):
        right((360/n)*d)
        forward(size)
       
def star_recursive (size, n, level, d=2):
    pendown()
    pencolor('red')
    pensize(5)
    if level <= 0:
        right((360/n)*d)
        forward(size)
    else:
        right((360/n)*d)
        forward(size)
        level -= 1
        star_recursive(size, n, level-1)

if __name__ == '__main__':
    s = Screen()     
    s.setup(450, 410)
    s.bgcolor('black')
    s.title('Turtle Program')
    penup()
    
    star_recursive(50, 5, 5)
    star(100, 5)

    hideturtle()
    exitonclick()
