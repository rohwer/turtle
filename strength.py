from turtle import *
from math import *
#   color += step(.5+cos(st.y*PI)*.25,st.x);

right(90)
penup()
forward(window_height()//2)
pendown()

color('black')
begin_fill()

right(90)
forward(window_width()//2)
right(90)

forward(window_height())
right(90)

forward(window_width()//2)
right(90)

height = window_height()

for i in range(height):
    test = i // 10
    if test > 1 and test % 2 > 0:
        left(1)
    else: 
        right(1)
    forward(1)


end_fill()
exitonclick()
