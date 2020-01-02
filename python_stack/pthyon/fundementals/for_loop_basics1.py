# Basic
for i in range(151):
    print(i)
# Multiples of five
for i in range(5, 1005, 5):
    print(i)
# Counting the Dojo way
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
#Whoa. That suckers huge
x = 0
for i in range(500001):
    if i % 2 != 0:
        x += i
print(x)
# Countdown by fours
for i in range(2018, 0, -4):
    print(i)
# Flexible counters
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)