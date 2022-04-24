def userSum(a,b):
    sum = a + b
    
    return sum

print(userSum(10,10))

x = 1
y = 2

sum = userSum(x,y)

print(sum)

for i in range(5):
    for j in range(5):
        sum  = userSum(i,j)
        print("%s + %s = %s" % (i,j,sum))


