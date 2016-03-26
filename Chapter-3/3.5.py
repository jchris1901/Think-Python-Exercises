# Exercise 3.5 - Grid

for i in range(0,21):
    if( i%5 == 0):
        print " *",
        for j in range(3):
            print " -" * 4,
            print " *",
        print "\n",
    else:
        print " |",
        for j in range(3):
            print " " * 8,
            print " |",
        print "\n",
