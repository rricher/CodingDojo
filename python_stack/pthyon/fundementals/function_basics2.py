#countdown
def countdown(a):
    x = []
    for i in range(a, -1, -1):
        x.append(i)
    return x

# Print and Run
def printRun(a):
    print(a[0])
    return a[1]

# First plus Length
def plusLength(a):
    return a[0] + len(a)

# Values greater than second
def greatSecond(a):
    if len(a) < 2:
        return False
    x = []
    for i in range(0, len(a)):
        if a[i] > a[1]:
            x.append(a[i])
    print(len(x))

# This length, That value
def leghtVal(a, b):
    x = []
    for i in range(a):
        x.append(b)
    return x