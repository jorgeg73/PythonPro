import turtle
#from turtle import Turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)

while True:
    alex.forward(1)
    alex.left(1.15)
    if abs(alex.pos()) < 1:
        break