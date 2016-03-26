# Exercise 5.2

def do_n(function,number):
    for i in range(4):
        function()

def example_function():
    print "Function Called"

do_n(example_function,4)
