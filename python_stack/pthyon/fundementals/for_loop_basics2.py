# Biggie Size
def bigSize(a):
    for i in range(len(a)):
        if a[i] >= 0:
            a[i] = "big"
    return a

# Count Positives
def countPos(a):
    count = 0
    for i in range(len(a)):
        if a[i] >= 0:
            count += 1
    a[len(a) -1] = count
    return a

# Sum total
def sumTotal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

# Average
def avrg(a):
    avrg = 0
    for i in range(len(a)):
        avrg += a[i]
    return avrg / len(a)

# Length
def lngth(a):
    x = 0
    for x in range(len(a)):
        x += 1
    return x

# Minimum
def min(a):
    if len(a) <1:
        return False
    min = a[0]
    for i in range(len(a)):
        if min > a[i]:
            min = a[i]
    return min

# Maximum
def max(a):
    if len(a) < 1:
        return False
    max = a[0]
    for i in range(len(a)):
        if max < a[i]:
            max = a[i]
    return max

# Ultimate Analysis
def ultAnls(a):
    analysis = {}
    analysis['sumTotal'] = sumTotal(a)
    analysis['average'] = avrg(a)
    analysis['minimum'] = min(a)
    analysis['maximum'] = max(a)
    analysis['length'] = lngth(a)
    return analysis0

# Reverse list
def reverse(a):
    for i in range(int(len(a) / 2)):
        temp = a[i]
        a[i] = a[len(a) - i - 1]
        a[len(a) - i - 1] = temp
    return a