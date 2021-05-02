#1
print("---#1---")
def a():
    return 5
print(a())

# output
# 5


#2
print("\n\n---#2---")
def a():
    return 5
print(a()+a())

# output
# 10


#3
print("\n\n---#3---")
def a():
    return 5
    return 10
print(a())

# output
# 5


#4
print("\n\n---#4---")
def a():
    return 5
    print(10)
print(a())

# output
# 5


#5
print("\n\n---#5---")
def a():
    print(5)
x = a()
print(x)

# output
# 5
# None


#6
# print("\n\n---#6---")
# def a(b,c):
#     print (b+c)
# print(a(1,2) + a(2,3))

# output
# 3
# 5
# error no value is returned to be stored


#7
print("\n\n---#7---")
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# output
# 25


#8
print("\n\n---#8---")
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
	    return 10
    return 7
print(a())

# output
# 100
# 10


#9
print("\n\n---#9---")
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# output
# 7
# 14
# 21


#10
print("\n\n---#10---")
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# output
# 8


#11
print("\n\n---#11---")
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# output
# 500
# 500
# 300
# 500

#12
print("\n\n---#12---")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# output
# 500
# 500
# 300
# 500


#13
print("\n\n---#13---")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# output
# 500
# 500
# 300
# 300


#14
print("\n\n---#14---")
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# output
# 1
# 3
# 2


#15
print("\n\n---#15---")
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# output
# 1
# 3
# 5
# 10










# output
# 25

