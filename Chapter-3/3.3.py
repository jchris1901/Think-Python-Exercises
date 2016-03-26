# Exercise 3.3

# Right Justify
word = raw_input("Enter a word:")
def right_justify(a):
    length = len(a)
    print " " * (69 - length) ,
    print a

right_justify(word)
