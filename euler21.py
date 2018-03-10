#returns proeperDivs for a number
def properDivs(x):
    if (x==1):
        return [1]
    res = []
    maxim = int(x/2)+1
    for i in range(1,maxim):
        if(x%i == 0):
            res.append(i)
    return res

def dn(x):
    total = 0
    arr = properDivs(x)
    for x in arr:
        total+= x
    return total

# returns array of all d(n)'s on a range from 1 to x
def alldns(x):
    res = []
    for i in range(1,x+1):
        res.append(dn(i))
    return res

# returns true or false if x and y are amicable. Takes array of all d(n)'s
def isAmicable(x,y, array):
    #we pass an array with all d(n)'s already calcuated beacause evaluating 'if (d(x) == y and d(y) == x)
    #every time is very slow
    if (array[x-1] == y and array[y-1] == x):
        return True
    else:
        return False

def allAmicables(x, array):

    bagOfAmicables = []
    number = 1

    while (number <= x):
        for n in range(number, x+1):
            if (isAmicable(number,n, array) and n != number):

                bagOfAmicables.append(number)
                bagOfAmicables.append(n)
        print number
        number += 1

    return bagOfAmicables

dn10000 = alldns(10000)
alles = allAmicables(10000, dn10000)

total = 0
for s in alles:
    total += s
print total
