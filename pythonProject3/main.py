#GlowScript 3.1 VPython
import math

from vpython import *
from collections import deque
from random import randint

scene.forward = vector(0, -0.3, -2)
scene.background = color.gray(0.8)
r = 1
a1 = a2 = a3 = 0


def Rotatea(v, angl):
    angle = angl - randint(-13,13)
    k = vector(0, 0, 0)
    k.x = math.cos(math.radians(angle)) * v.x - math.sin(math.radians(angle)) * v.y
    k.y = math.sin(math.radians(angle)) * v.x + math.cos(math.radians(angle)) * v.y
    k.z = v.z
    k = norm(k)
    #print(k, angle, " CEC", math.sin(math.radians(angle)))
    return k


def Rotateb(v, angl):
    angle = angl - randint(-13, 13)
    k = vector(0, 0, 0)
    k.x = math.cos(math.radians(angle)) * v.x + math.sin(math.radians(angle)) * v.y
    k.y = -math.sin(math.radians(angle)) * v.x + math.cos(math.radians(angle)) * v.y
    k.z = v.z
    k = norm(k)
    return k


def Rotatec(v, angl):
    angle = angl - randint(-13, 13)
    k = vector(0, 0, 0)
    k.z = math.cos(math.radians(angle)) * v.z - math.sin(math.radians(angle)) * v.y
    k.y = math.sin(math.radians(angle)) * v.z + math.cos(math.radians(angle)) * v.y
    k.x = v.x
    k = norm(k)
    return k


def Rotated(v, angle):
    k = vector(0, 0, 0)
    k.z = math.cos(math.radians(angle)) * v.z + math.sin(math.radians(angle)) * v.y
    k.y = -math.sin(math.radians(angle)) * v.z + math.cos(math.radians(angle)) * v.y
    k.x = v.x
    k = norm(k)
    return k


axiom = "22220"
axmTemp = ""
itr = 8
angl = 25
thick = 0.8
stc = deque()
translate = {"1": "21",
             "0": "1[a20][b20][c20]d20"}
cl = vector(0.1, 0.9, 0.1)
ax = vector(0, 1, 0)
na = vector(0, 1, 0)
po = vector(0, -15, 0)

for k in range(itr):
    for ch in axiom:
        if ch in translate:
            axmTemp += translate[ch]
        else:
            axmTemp += ch
    axiom = axmTemp
    axmTemp = ""
print(axiom)

for ch in axiom:
    if ch == "a":
        ax = Rotatea(ax, angl)
    elif ch == "b":
        ax = Rotateb(ax, angl)
    elif ch == "c":
        ax = Rotatec(ax, angl)
    elif ch == "d":
        ax = Rotated(ax, angl)
    elif ch == "2":
        if randint(0, 10) > 4:
            cyl = cylinder(pos=po, size=vector(1, thick, thick), color=vector(0.4, 0.26, 0.13), axis=ax)
            po += ax
    elif ch == "1":
        cyl = cylinder(pos=po, size=vector(1, thick, thick), color=vector(0.4, 0.26, 0.13), axis=ax)
        po += ax
    elif ch == "0":
        r = randint(0, 10)
        if r < 3:
            cl = vector(0.1, 0.9, 0.1)
        elif r > 6:
            cl = vector(0.398, 0.472, 0.0)
        else:
            cl = vector(0.125, 0.73, 0.0)
        cyl = cylinder(pos=po, size=vector(0.5, thick*2, thick*2), color=cl, axis=ax)
        po += ax
    elif ch == "[":
        thick = thick * 0.85
        stc.append(thick)
        stc.append(po)
        stc.append(ax)
    elif ch == "]":
        ax = stc.pop()
        po = stc.pop()
        thick = stc.pop()