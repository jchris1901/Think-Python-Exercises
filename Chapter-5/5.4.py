# Exercise 5.4

def is_triangle(a,b,c):
    if( a + b >= c):
        print "Yes!"
    else:
        print "No!"

x = int(raw_input(" Enter the minimum side : "))
y = int(raw_input(" Enter the second minimum side : "))
z = int(raw_input(" Enter the maximum side : "))

is_triangle(x,y,z)
