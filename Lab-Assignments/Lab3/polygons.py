from turtle import *

def polygon (size, n):
    pendown()
    pencolor('red')
    pensize(5)
    for i in range(n):
        forward(size)
        left(360/n)

def polygon_recursive(size, n, level):
    pendown()
    if level == 0:
        pencolor('red')
        pensize(5)
        forward(size)    
    else:
        pencolor('red')
        pensize(5)
        forward(size)
        left(360/n)
        polygon_recursive(size, n, level - 1)

if __name__ == '__main__':
    s = Screen()     
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')

    polygon(100, 8)
    penup()
    goto(10, 10)
    polygon_recursive(80, 4, 1)

    exitonclick()
