# Exercise 3.4 - Do Four function

x = raw_input("Enter the Argument :")
def function_argument(function,argument):
    function(argument)

def print_four(a):
    for i in range(4):
        print a

function_argument(print_four,x)
