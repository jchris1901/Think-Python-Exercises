# Exercise 4.1

from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

#1

def square(t):
    for i in range(4):
        fd(t,100)
        lt(t)

square(bob)

#2

def square2(t,l):
    for i in range(4):
        fd(t,l)
        lt(t)

x = int(raw_input("Enter Length : "))
square2(bob,x)

#3

def polygon(t,l,n):
    for i in range(n):
        fd(t,l)
        lt(t,360/n)

y = int(raw_input("Enter Length : "))
z = int(raw_input("Enter number of edges : "))
polygon(bob,y,z)

#4

def arc(t, r, angle):
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    lt(t, step_angle/2)
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)
    rt(t, step_angle/2)


def circle(t, r):
    arc(t, r, 360)

circle(bob,100)

#5

arc(bob, 100, 180)


wait_for_user()
