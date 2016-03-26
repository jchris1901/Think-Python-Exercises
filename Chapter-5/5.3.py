# Exercise 5.3 - Fermat's Theorem

def check_fermat(a,b,c,n):
    if((pow(a,n) + pow(b,n)) == pow(c,n)):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

w = int(raw_input("Enter the value of a : ")) # Here we specify int because by default python reads everything as strings
x = int(raw_input("Enter the value of b : "))
y = int(raw_input("Enter the value of c : "))
z = int(raw_input("Enter the value of n : "))
if ( z > 2):
    check_fermat(w,x,y,z)
else:
    print "Value of n is less than 2"
