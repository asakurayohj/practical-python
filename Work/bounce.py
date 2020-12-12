# bounce.py
#
# Exercise 1.5

times = 1
rate = 3/5
bounceHeight = round(100 * rate)
while times < 11:
    print(times, bounceHeight)
    times += 1
    bounceHeight *= rate
