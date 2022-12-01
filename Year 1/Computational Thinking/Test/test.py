from distutils.ccompiler import new_compiler


a = 1                   #5
while True:             #4
    a = a + 2           #1
    print(a)            #6
    if a > 10:          #3
        break           #2

print("---------")


# 5, 4, 1, 6, 3, 2
a = 1                   #5
while True:             #4
    if a > 10:          #3
        break           #2
    a = a + 2           #1
    print(a)            #6

x = 6
y = 3

if (x > 6) and (y < 3):
    print("A")
elif (x != y) or (y > 0):
    print("B")
else:
    print("C")


a = "abra"
b = "cad"
string = (b + a) * 2
print(string[9::-3])

print("Kirill".count("l"))


colours = ["r", "g", "b"]
new_colours = colours + ["a", "m"]
print(new_colours[4])

print(-3 % 9)

print(4 * (3 + 8 + 9) % 4 * 3)


x = -1
y = -1

if (x > 6) and (y < 3):
    print("A")
elif (x != y) or (y > 0):
    print("B")
else:
    print("C")



def fun(A = 2, B = 3):
    print(A)
    print(B)
    A = 3

A = 4
fun(B = A)
print(A)