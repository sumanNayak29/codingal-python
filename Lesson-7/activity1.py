# Python program to illustrate the use

# of 'is' identity operator



x = 10


if (type(x) is int):


    print("true")

else:

    print("false")


 
x = 15.5

if (type(x) is not float):

    print("true")

else:

    print("false")

 
x = 30

y = 30

if (x is y):

    print("x & y SAME identity")

 
y = 40

if (x is not y):

    print("x & y have DIFFERENT identity")