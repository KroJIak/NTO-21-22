import numpy as np
import math

q = list(map(int, input().split()))
sumcoor = [0, 0, 0]

def Rx(x, y, z, a):
    global sumcoor
    a = math.radians(a)
    shift = np.array([x,y,z])
    R = np.array([[1, 0, 0],
                  [0, math.cos(a), -math.sin(a)],
                  [0, math.sin(a), math.cos(a)]])
    shift = np.dot(shift, R)
    for i in range(3):
        sumcoor[i] += shift[i]
        print("shift[",i,"] = ",shift[i],sep="")
    print("sumcoor =", *sumcoor)
    print()
def Ry(x, y, z, a):
    global sumcoor
    a = math.radians(a)
    shift = np.array([x,y,z])
    R = np.array([[math.cos(a), 0, math.sin(a)],
                  [0, 1, 0],
                  [-math.sin(a), 0, math.cos(a)]])
    shift = np.dot(shift, R)
    for i in range(3):
        sumcoor[i] += shift[i]
        print("shift[",i,"] = ",shift[i],sep="")
    print("sumcoor =", *sumcoor)
    print()
def Rz(x, y, z, a):
    global sumcoor
    a = math.radians(a)
    shift = np.array([x,y,z])
    R = np.array([[math.cos(a), -math.sin(a), 0],
                  [math.sin(a), math.cos(a), 0],
                  [0, 0, 1]])
    shift = np.dot(shift, R)
    for i in range(3):
        sumcoor[i] += shift[i]
        print("shift[",i,"] = ",shift[i],sep="")
    print("sumcoor =", *sumcoor)
    print()
        
Rz(0, 0, 20, q[0])
Ry(400, 0, 0, q[1])
Ry(200, 0, 0, q[2])
Ry(200, 0, 0, q[2])
for i in range(3):
    sumcoor[i] = math.floor(sumcoor[i])
print(*sumcoor)
