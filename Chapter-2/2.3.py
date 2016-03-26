# Exercise 2.3

# 1 Volume of Sphere with radius 5
volume = (4 * 3.14 * 5 * 5 *5)/3
print volume

print "\n"

# 2 Cost of 60 copies
store_price = 24.95 - ((24.95 * 40)/100)
first_copy = store_price + 3
rest = (store_price + 0.75) * 49
total = first_copy + rest
print total

print "\n"

# 3 Breakfast time
import datetime

start_time = datetime.datetime(1,1,1,6,52,0)
stop_time = start_time + datetime.timedelta(0,2286) #2286 seconds comes from 2 * 8:15 and 3 * 7:12
print stop_time.time()
