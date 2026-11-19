a = int(input("enter a value: "))
b = int(input("enter value 2 :"))
c = int(input("enter value 3: "))
d = int(input("enter value 4: "))
e = int(input("enter value 5: "))
f = int(input("enter value 6: "))
g = int(input("enter value 7: "))
h = int(input("enter value 8: "))
i = int(input("enter value 9: "))
j = int(input("enter value 10: "))

avg = (a + b + c + d + e + f + g + h + i + j) / 10
print("avg =", avg)

if avg > a and avg > b and avg > c and avg > d and avg > e :
    print("%d is higher than %d, %d, %d, %d, %d, %d, %d, %d, %d" %(avg, a, b, c, d, e, f, g, h, i, j))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is just higher than %d" %(avg, a))
elif avg > b:
    print("%d is just higher than %d" %(avg, b))
elif avg > c:
    print("%d is just higher than %d" %(avg, c))
else:
  print("invalid input")