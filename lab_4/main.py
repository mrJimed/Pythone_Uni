import string as str
import random as rnd
import segno
import numpy as np
import matplotlib.pyplot as plt
import io


class pair:
    def __init__(self, qr, isQr):
        self.isQr = isQr
        self.qr = qr


def randStr(size):
    return ''.join(rnd.choice(str.ascii_letters) for _ in range(size))

def getQr():
    qr = []
    for _ in range(100):
        qr.append(np.array((segno.make(randStr(9))).matrix).ravel())
    return qr

def getNotQr():
    notqr = []
    for i in range(100):
        notqr.append([])
        for k in range(10):
            notqr[i].append(k // 6)
        for k in range(215):
            notqr[i].append(rnd.random())
    return notqr


def perc(sensor):
    b = 1500
    s = 0
    for i in range(225):
        s += int(sensor[i]) * w[i]
    if s>=b:
        return True
    else:
        return False

def decrease(sensor):
    for i in range(225):
        if int(sensor[i]) == 1:
            w[i] -= 1

def increase(sensor):
    for i in range(225):
        if int(sensor[i]) == 1:
            w[i] += 1


rnd.seed(version= 2)

w = [0 for _ in range(225)]
qr = getQr()
notqr = getNotQr()
p = []
for i in range(100):
    p.append(pair(qr[i], True))
    p.append(pair(notqr[i], False))

for i in range(20):
    rnd.shuffle(p)
    for k in range(200):
        j = rnd.randint(0, 199)
        r = perc(p[j].qr)
        if not p[j].isQr:
            if r:
                decrease(p[k].qr)
        else:
            if not r:
                increase(p[k].qr)

print(w)
plt.imshow(np.reshape(w,(15,15)))
plt.show()

w = [0 for _ in range(225)]
notqr = getNotQr()
qr = []
p = []
for _ in range(100):
    qr.append(np.array((segno.make('test')).matrix).ravel())
for i in range(100):
    p.append(pair(qr[i], True))
    p.append(pair(notqr[i], False))

for i in range(20):
    rnd.shuffle(p)
    for k in range(200):
        j = rnd.randint(0, 199)
        r = perc(p[j].qr)
        if not p[j].isQr:
            if r:
                decrease(p[k].qr)
        else:
            if not r:
                increase(p[k].qr)

print(w)
plt.imshow(np.reshape(w,(15,15)))
plt.show()