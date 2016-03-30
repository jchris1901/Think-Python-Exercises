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

#def circle(t,r):
    
wait_for_user()
