
from tkinter import *
from tkinter.ttk import *
import xlrd
import math
import cmath
import os
import pyttsx3
from tkinter import filedialog, IntVar
w=Tk()
a1=pyttsx3.init()
a1.setProperty('rate', 135)
voices = a1.getProperty('voices')
a1.setProperty('voice', voices[1].id)
a1.say("Welcome  and  Thank you! for choosing GCG")
a1.runAndWait()
w.geometry('500x300')
w.title("WELCOME TO G-CODE GENERATOR")
global i_4
i_4=0
def exi():
    exit()
def enter():
    global K
    k=n_9.get()
    K=int(k)
    a1.say("Click Next to continue.")
    a1.runAndWait()
def getcode():
    global vr4
    global vr5
    global n_3
    global vr1
    global vr11
    global vr2
    global vr3
    a1.say("Then click NEXT to continue.")
    a1.runAndWait()

    p = []
    y1 = []
    x1 = []
    x2 = []
    y2 = []
    r1 = []
    cx1 = []
    cy1 = []
    sa = []
    ta = []
    ma = []
    mina = []
    Name = []

    wb = xlrd.open_workbook(loc, logfile=open(os.devnull, 'w'))

    sheet = wb.sheet_by_index(0)

    sheet.cell_value(0, 0)

    for i in range(sheet.ncols):
        p.append(sheet.cell_value(0, i))

    for i in range(len(p)):
        if p[i] == "Name":
            m = i
    for j in range(1, sheet.nrows):
        Name.append(sheet.cell_value(j, m))
    for l in range(len(p)):
        if p[l] == "Start X":
            m = l
    for j in range(1, sheet.nrows):
        x1.append(sheet.cell_value(j, m))
    for l in range(len(x1)):
        if x1[l] == "":
            x1[l] = 0

    for i in range(len(p)):
        if p[i] == "Start Y":
            m = i
    for j in range(1, sheet.nrows):
        y1.append(sheet.cell_value(j, m))
    for l in range(len(y1)):
        if y1[l] == '':
            y1[l] = 0

    for i in range(len(p)):
        if p[i] == "End X":
            m = i
    for j in range(1, sheet.nrows):
        x2.append(sheet.cell_value(j, m))
    for l in range(len(x2)):
        if x2[l] == '':
            x2[l] = 0

    for j in range(len(p)):
        if p[j] == "End Y":
            m = j
    for j in range(1, sheet.nrows):
        y2.append(sheet.cell_value(j, m))

    for l in range(len(y2)):
        if y2[l] == '':
            y2[l] = 0
    for i in range(len(p)):
        if p[i] == "Center X":
            m = i
    for j in range(1, sheet.nrows):
        cx1.append(sheet.cell_value(j, m))
    for l in range(len(cx1)):
        if cx1[l] == '':
            cx1[l] = 0
    for j in range(len(p)):
        if p[j] == "Center Y":
            m = j
    for j in range(1, sheet.nrows):
        cy1.append(sheet.cell_value(j, m))
    for l in range(len(cy1)):
        if cy1[l] == '':
            cy1[l] = 0
    for h in range(len(p)):
        if p[h] == "Radius":
            m = h
    for j in range(1, sheet.nrows):
        r1.append(sheet.cell_value(j, m))
    for l in range(len(r1)):
        if r1[l] == '':
            r1[l] = 0
    for h in range(len(p)):
        if p[h] == "Start Angle":
            m = h
    for j in range(1, sheet.nrows):
        sa.append(sheet.cell_value(j, m))
    for l in range(len(sa)):
        if sa[l] == '':
            sa[l] = 0
    for i in range(len(p)):
        if p[i] == "Total Angle":
            m = i
    for j in range(1, sheet.nrows):
        ta.append(sheet.cell_value(j, m))
    for i in range(len(ta)):
        if ta[i] == '':
            ta[i] = 0
    for i in range(len(p)):
        if p[i] == "Major Radius":
            m = i
    for j in range(1, sheet.nrows):
        ma.append(sheet.cell_value(j, m))
    for i in range(len(ma)):
        if ma[i] == '':
            ma[i] = 0
    for j in range(len(p)):
        if p[j] == "Minor Radius":
            m = j
    for j in range(1, sheet.nrows):
        mina.append(sheet.cell_value(j, m))
    for j in range(len(mina)):
        if mina[j] == '':
            mina[j] = 0
    for i in range(len(x1)):
        ta[i] = float(ta[i])
        sa[i] = float(sa[i])
        ma[i] = float(ma[i])
        x1[i] = float(x1[i])
        x2[i] = float(x2[i])
        y1[i] = float(y1[i])
        y2[i] = float(y2[i])
        mina[i] = float(mina[i])
        cx1[i] = float(cx1[i])
        cy1[i] = float(cy1[i])
        r1[i] = float(r1[i])
    M = vr1.get()
    b1 = vr4.get()
    b2 = vr5.get()
    T = vr2.get()
    S = vr3.get()
    Mul=vr11.get()
    F = (S / 100) + 30
    H = T
    z11 = n_3.get()
    z22 = float(z11)

    for i in range(len(x1)):
        if x1[i] == 0 and y1[i] == 0 and x2[i] == 0 and y2[i] == 0:
            if Name[i] == 'Arc':
                ea = (ta[i] + sa[i])
                sas = sa[i]
                a = math.cos(math.radians(sas))
                b = math.sin(math.radians(sas))
                c = math.cos(math.radians(ea))
                d = math.sin(math.radians(ea))
                x1[i] = cx1[i] + (r1[i] * a)
                y1[i] = cy1[i] + (r1[i] * b)
                x2[i] = cx1[i] + (r1[i] * c)
                y2[i] = cy1[i] + (r1[i] * d)
            elif Name[i] == 'Ellipse':
                x1[i] = cx1[i] + ma[i]
                y1[i] = cy1[i]
                x2[i] = cx1[i] - ma[i]
                y2[i] = cy1[i]
            elif Name[i] == 'Circle':
                x1[i] = cx1[i] + r1[i]
                y1[i] = cy1[i]
                x2[i] = cx1[i] - r1[i]
                y2[i] = cy1[i]
    for k in range(len(x1)):
        for h in range(len(x1)):
            for i in range(len(x1)):
                if x2[h - 1] == x1[i] and y2[h - 1] == y1[i]:
                    name1 = Name[h]
                    ta_1 = ta[h]
                    r1_1 = r1[h]
                    cx1_1 = cx1[h]
                    cy1_1 = cy1[h]
                    sa_1 = sa[h]
                    ma_1 = ma[h]
                    mina_1 = mina[h]
                    n_1 = x1[h]
                    m_1 = y1[h]
                    o_1 = x2[h]
                    p_1 = y2[h]
                    Name[h] = Name[i]
                    ta[h] = ta[i]
                    r1[h] = r1[i]
                    cx1[h] = cx1[i]
                    cy1[h] = cy1[i]
                    sa[h] = sa[i]
                    ma[h] = ma[i]
                    mina[h] = mina[i]
                    x2[h] = x2[i]
                    y2[h] = y2[i]
                    x1[h] = x1[i]
                    y1[h] = y1[i]
                    Name[i] = name1
                    r1[i] = r1_1
                    ta[i] = ta_1
                    sa[i] = sa_1
                    ma[i] = ma_1
                    mina[i] = mina_1
                    cx1[i] = cx1_1
                    cy1[i] = cy1_1
                    x2[i] = o_1
                    y2[i] = p_1
                    x1[i] = n_1
                    y1[i] = m_1
                else:
                    pass
    if b1 == 1:
        if b2 == 1:
            print("G21 G94")
        elif b2 == 2:
            print('G21 G93')
    elif b1 == 2:
        if b2 == 1:
            print('G20 G94')
        elif b2 == 2:
            print('G20 G90')
    print("G91 G28 X0 Y0 Z0")
    print("M06 T0", T, sep='')
    if M == 1:
        print("M03 S", S, sep='')
    elif M == 2:
        print("M04 S", S, sep='')
    print("G90 G54 G00 X{0} Y{1}".format(0, 0))
    print("G43 H{0} Z1".format(H))
    print("G01 Z0.2 F{0}".format(F))
    if z22 < 0:
        pass
    else:
        z22 = -z22
    A = math.floor(z22 / -0.5)
    if Mul==1:
        if z22 > -0.5:
            Z = z22
            for i in range(len(x1)):
                if Name[i] == "Arc":
                    ea = (ta[i] + sa[i])
                    sas = sa[i]
                    a = math.cos(math.radians(sas))
                    b = math.sin(math.radians(sas))
                    c = math.cos(math.radians(ea))
                    d = math.sin(math.radians(ea))
                    x_0 = cx1[i] + (r1[i] * a)
                    y_0 = cy1[i] + (r1[i] * b)
                    X_0 = cx1[i] + (r1[i] * c)
                    Y_0 = cy1[i] + (r1[i] * d)
                    v = ea - sas
                    if (v == ta[i]):
                        sek = (ea + sas) / 2
                        if (sek < sas and sak > ea):
                            sek = sek + 180
                        e = math.cos(math.radians(sek))
                        h = math.sin(math.radians(sek))
                        x_2 = cx1[i] + (r1[i] * e)
                        y_2 = cy1[i] + (r1[i] * h)
                        print("G00 Z0.2")
                        print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                        print("G01 Z{0}".format(Z))
                        print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x_2, y_2, r1[i]))
                        print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X_0, Y_0, r1[i]))
                    else:
                        sak = (ea + sas) / 2
                        sam = (sas + sek) / 2
                        san = (ea + sek) / 2
                        if (sak > sas and sak < ea):
                            sak = 180 + sak
                        e = math.cos(math.radians(sak))
                        h = math.sin(math.radians(sak))
                        x_2 = cx1[i] + (r1[i] * e)
                        y_2 = cy1[i] + (r1[i] * h)
                        print("G00 Z0.2")
                        print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                        print("G01 Z{0}".format(Z))
                        print("G02 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x_2, y_2, r1[i]))
                        print("G02 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X_0, Y_0, r1[i]))
                elif Name[i] == "Ellipse":
                    x_0 = cx1[i] + ma[i]
                    y_0 = cy1[i]
                    X_0 = cx1[i] - ma[i]
                    Y_0 = cy1[i]
                    x_1 = cx1[i]
                    y_1 = cy1[i] + mina[i]
                    X_1 = cx1[i]
                    Y_1 = cy1[i] - mina[i]
                    print("G00 Z0.2")
                    print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                    print("G01 Z{0}".format(Z))
                    if (ma[i] > mina[i] and ma[i] < 100):
                        v = x_0
                        q = y_0
                        while (y_0 != y_1):
                            y_0 = y_0 + 0.2
                            if (y_0 > y_1):
                                y_0 = y_1
                            L = (y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (L > 1):
                                l1 = cmath.sqrt(1 - L)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - L)
                                W = ma[i] * l1
                            x_0 = cx1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                        while (y_1 != Y_0):
                            y_1 = y_1 - 0.2
                            if (y_1 < Y_0):
                                y_1 = Y_0
                            l = (y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = ma[i] * l1
                            x_1 = cx1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                        while (Y_0 != Y_1):
                            Y_0 = Y_0 - 0.2
                            if (Y_0 < Y_1):
                                Y_0 = Y_1
                            L = (Y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (L > 1):
                                l1 = cmath.sqrt(1 - L)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - L)
                                W = ma[i] * l1
                            X_0 = cx1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                        while (Y_1 != q):
                            Y_1 = Y_1 + 0.2
                            if (Y_1 > q):
                                Y_1 = q
                            L = (Y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (L > 1):
                                l1 = cmath.sqrt(1 - L)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - L)
                                W = ma[i] * l1
                            X_1 = cx1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                    if (mina[i] > ma[i] and mina[i] < 100):
                        v = x_0
                        q = y_0
                        while (x_0 != x_1):
                            x_0 = x_0 - 0.2
                            if (x_0 < x_1):
                                x_0 = x_1
                            l = (x_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1

                            y_0 = cy1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                        while (x_1 != X_0):
                            x_1 = x_1 - 0.2
                            if (x_1 < X_0):
                                x_1 = X_0
                            l = (x_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1
                            y_1 = cy1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                        while (X_0 != X_1):
                            X_0 = X_0 + 0.2
                            if (X_0 > X_1):
                                X_0 = X_1
                            l = (X_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1
                            Y_0 = cy1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                        while (X_1 != v):
                            X_1 = X_1 + 0.2
                            if (X_1 > v):
                                X_1 = v
                            l = (X_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1
                            Y_1 = cy1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                    if (ma[i] > mina[i] and ma[i] > 100):
                        v = x_0
                        q = y_0
                        while (y_0 != y_1):
                            y_0 = y_0 + 15
                            if (y_0 > y_1):
                                y_0 = y_1
                            L = (y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (L > 1):
                                l1 = cmath.sqrt(1 - L)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - L)
                                W = ma[i] * l1
                            x_0 = cx1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                        while (y_1 != Y_0):
                            y_1 = y_1 - 15
                            if (y_1 < Y_0):
                                y_1 = Y_0
                            l = (y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = ma[i] * l1
                            x_1 = cx1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                        while (Y_0 != Y_1):
                            Y_0 = Y_0 - 15
                            if (Y_0 < Y_1):
                                Y_0 = Y_1
                            L = (Y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (L > 1):
                                l1 = cmath.sqrt(1 - L)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - L)
                                W = ma[i] * l1
                            X_0 = cx1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                        while (Y_1 != q):
                            Y_1 = Y_1 + 15
                            if (Y_1 > q):
                                Y_1 = q
                            L = (Y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                            if (L > 1):
                                l1 = cmath.sqrt(1 - L)
                                l2 = l1.real
                                W = ma[i] * l2
                            else:
                                l1 = math.sqrt(1 - L)
                                W = ma[i] * l1
                            X_1 = cx1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                    if (mina[i] > ma[i] and mina[i] > 100):
                        v = x_0
                        q = y_0
                        while (x_0 != x_1):
                            x_0 = x_0 - 15
                            if (x_0 < x_1):
                                x_0 = x_1
                            l = (x_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1

                            y_0 = cy1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                        while (x_1 != X_0):
                            x_1 = x_1 - 15
                            if (x_1 < X_0):
                                x_1 = X_0
                            l = (x_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1
                            y_1 = cy1[i] + W
                            print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                        while (X_0 != X_1):
                            X_0 = X_0 + 15
                            if (X_0 > X_1):
                                X_0 = X_1
                            l = (X_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1
                            Y_0 = cy1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                        while (X_1 != v):
                            X_1 = X_1 + 15
                            if (X_1 > v):
                                X_1 = v
                            l = (X_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                            if (l > 1):
                                l1 = cmath.sqrt(1 - l)
                                l2 = l1.real
                                W = mina[i] * l2
                            else:
                                l1 = math.sqrt(1 - l)
                                W = mina[i] * l1
                            Y_1 = cy1[i] - W
                            print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                elif Name[i] == "Circle":
                    x = cx1[i] + r1[i]
                    y = cy1[i]
                    X = cx1[i] - r1[i]
                    Y = cy1[i]
                    print("G00 Z0.2")
                    print("G00 X{0:.4f} Y{1:.4f}".format(x, y))
                    print("G01 Z{0}".format(Z))
                    print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X, Y, r1[i]))
                    print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x, y, r1[i]))

                elif Name[i] == 'Line':
                    print("G00 Z0.2")
                    print("G00 X{0:.4f} Y{1:.4f}".format(x1[i], y1[i]))
                    print("G01 Z{0}".format(Z))
                    print("G01 X{0:.4f} Y{1:.4f}".format(x2[i], y2[i]))

            print("G00 Z10")
        else:
            for q in range(1, A + 1):
                if q < A:
                    Z = -0.5 * q
                else:
                    Z = z22

                for i in range(len(x1)):
                    if Name[i] == "Arc":
                        ea = (ta[i] + sa[i])
                        sas = sa[i]
                        a = math.cos(math.radians(sas))
                        b = math.sin(math.radians(sas))
                        c = math.cos(math.radians(ea))
                        d = math.sin(math.radians(ea))
                        x_0 = cx1[i] + (r1[i] * a)
                        y_0 = cy1[i] + (r1[i] * b)
                        X_0 = cx1[i] + (r1[i] * c)
                        Y_0 = cy1[i] + (r1[i] * d)
                        v = ea - sas
                        if (v == ta[i]):
                            sek = (ea + sas) / 2
                            if (sek < sas and sak > ea):
                                sek = sek + 180
                            e = math.cos(math.radians(sek))
                            h = math.sin(math.radians(sek))
                            x_2 = cx1[i] + (r1[i] * e)
                            y_2 = cy1[i] + (r1[i] * h)
                            print("G00 Z0.2")
                            print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                            print("G01 Z{0}".format(Z))
                            print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x_2, y_2, r1[i]))
                            print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X_0, Y_0, r1[i]))
                        else:
                            sak = (ea + sas) / 2
                            sam = (sas + sek) / 2
                            san = (ea + sek) / 2
                            if (sak > sas and sak < ea):
                                sak = 180 + sak
                            e = math.cos(math.radians(sak))
                            h = math.sin(math.radians(sak))
                            x_2 = cx1[i] + (r1[i] * e)
                            y_2 = cy1[i] + (r1[i] * h)
                            print("G00 Z0.2")
                            print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                            print("G01 Z{0}".format(Z))
                            print("G02 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x_2, y_2, r1[i]))
                            print("G02 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X_0, Y_0, r1[i]))
                    elif Name[i] == "Ellipse":
                        x_0 = cx1[i] + ma[i]
                        y_0 = cy1[i]
                        X_0 = cx1[i] - ma[i]
                        Y_0 = cy1[i]
                        x_1 = cx1[i]
                        y_1 = cy1[i] + mina[i]
                        X_1 = cx1[i]
                        Y_1 = cy1[i] - mina[i]
                        print("G00 Z0.2")
                        print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                        print("G01 Z{0}".format(Z))
                        if (ma[i] > mina[i] and ma[i] < 100):
                            v = x_0
                            q = y_0
                            while (y_0 != y_1):
                                y_0 = y_0 + 0.2
                                if (y_0 > y_1):
                                    y_0 = y_1
                                L = (y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (L > 1):
                                    l1 = cmath.sqrt(1 - L)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - L)
                                    W = ma[i] * l1
                                x_0 = cx1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                            while (y_1 != Y_0):
                                y_1 = y_1 - 0.2
                                if (y_1 < Y_0):
                                    y_1 = Y_0
                                l = (y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = ma[i] * l1
                                x_1 = cx1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                            while (Y_0 != Y_1):
                                Y_0 = Y_0 - 0.2
                                if (Y_0 < Y_1):
                                    Y_0 = Y_1
                                L = (Y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (L > 1):
                                    l1 = cmath.sqrt(1 - L)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - L)
                                    W = ma[i] * l1
                                X_0 = cx1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                            while (Y_1 != q):
                                Y_1 = Y_1 + 0.2
                                if (Y_1 > q):
                                    Y_1 = q
                                L = (Y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (L > 1):
                                    l1 = cmath.sqrt(1 - L)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - L)
                                    W = ma[i] * l1
                                X_1 = cx1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                        if (mina[i] > ma[i] and mina[i] < 100):
                            v = x_0
                            q = y_0
                            while (x_0 != x_1):
                                x_0 = x_0 - 0.2
                                if (x_0 < x_1):
                                    x_0 = x_1
                                l = (x_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1

                                y_0 = cy1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                            while (x_1 != X_0):
                                x_1 = x_1 - 0.2
                                if (x_1 < X_0):
                                    x_1 = X_0
                                l = (x_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1
                                y_1 = cy1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                            while (X_0 != X_1):
                                X_0 = X_0 + 0.2
                                if (X_0 > X_1):
                                    X_0 = X_1
                                l = (X_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1
                                Y_0 = cy1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                            while (X_1 != v):
                                X_1 = X_1 + 0.2
                                if (X_1 > v):
                                    X_1 = v
                                l = (X_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1
                                Y_1 = cy1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                        if (ma[i] > mina[i] and ma[i] > 100):
                            v = x_0
                            q = y_0
                            while (y_0 != y_1):
                                y_0 = y_0 + 15
                                if (y_0 > y_1):
                                    y_0 = y_1
                                L = (y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (L > 1):
                                    l1 = cmath.sqrt(1 - L)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - L)
                                    W = ma[i] * l1
                                x_0 = cx1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                            while (y_1 != Y_0):
                                y_1 = y_1 - 15
                                if (y_1 < Y_0):
                                    y_1 = Y_0
                                l = (y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = ma[i] * l1
                                x_1 = cx1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                            while (Y_0 != Y_1):
                                Y_0 = Y_0 - 15
                                if (Y_0 < Y_1):
                                    Y_0 = Y_1
                                L = (Y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (L > 1):
                                    l1 = cmath.sqrt(1 - L)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - L)
                                    W = ma[i] * l1
                                X_0 = cx1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                            while (Y_1 != q):
                                Y_1 = Y_1 + 15
                                if (Y_1 > q):
                                    Y_1 = q
                                L = (Y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                                if (L > 1):
                                    l1 = cmath.sqrt(1 - L)
                                    l2 = l1.real
                                    W = ma[i] * l2
                                else:
                                    l1 = math.sqrt(1 - L)
                                    W = ma[i] * l1
                                X_1 = cx1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                        if (mina[i] > ma[i] and mina[i] > 100):
                            v = x_0
                            q = y_0
                            while (x_0 != x_1):
                                x_0 = x_0 - 15
                                if (x_0 < x_1):
                                    x_0 = x_1
                                l = (x_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1

                                y_0 = cy1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                            while (x_1 != X_0):
                                x_1 = x_1 - 15
                                if (x_1 < X_0):
                                    x_1 = X_0
                                l = (x_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1
                                y_1 = cy1[i] + W
                                print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                            while (X_0 != X_1):
                                X_0 = X_0 + 15
                                if (X_0 > X_1):
                                    X_0 = X_1
                                l = (X_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1
                                Y_0 = cy1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                            while (X_1 != v):
                                X_1 = X_1 + 15
                                if (X_1 > v):
                                    X_1 = v
                                l = (X_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                                if (l > 1):
                                    l1 = cmath.sqrt(1 - l)
                                    l2 = l1.real
                                    W = mina[i] * l2
                                else:
                                    l1 = math.sqrt(1 - l)
                                    W = mina[i] * l1
                                Y_1 = cy1[i] - W
                                print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                    elif Name[i] == "Circle":
                        x = cx1[i] + r1[i]
                        y = cy1[i]
                        X = cx1[i] - r1[i]
                        Y = cy1[i]
                        print("G00 Z0.2")
                        print("G00 X{0:.4f} Y{1:.4f}".format(x, y))
                        print("G01 Z{0}".format(Z))
                        print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X, Y, r1[i]))
                        print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x, y, r1[i]))

                    elif Name[i] == 'Line':
                        print("G00 Z0.2")
                        print("G00 X{0:.4f} Y{1:.4f}".format(x1[i], y1[i]))
                        print("G01 Z{0}".format(Z))
                        print("G01 X{0:.4f} Y{1:.4f}".format(x2[i], y2[i]))

                print("G00 Z10")
    else:
        for i in range(len(x1)):
            if Name[i] == "Arc":
                ea = (ta[i] + sa[i])
                sas = sa[i]
                a = math.cos(math.radians(sas))
                b = math.sin(math.radians(sas))
                c = math.cos(math.radians(ea))
                d = math.sin(math.radians(ea))
                x_0 = cx1[i] + (r1[i] * a)
                y_0 = cy1[i] + (r1[i] * b)
                X_0 = cx1[i] + (r1[i] * c)
                Y_0 = cy1[i] + (r1[i] * d)
                v = ea - sas
                if (v == ta[i]):
                    sek = (ea + sas) / 2
                    if (sek < sas and sak > ea):
                        sek = sek + 180
                    e = math.cos(math.radians(sek))
                    h = math.sin(math.radians(sek))
                    x_2 = cx1[i] + (r1[i] * e)
                    y_2 = cy1[i] + (r1[i] * h)
                    print("G00 Z0.2")
                    print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                    print("G01 Z{0}".format(z22))
                    print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x_2, y_2, r1[i]))
                    print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X_0, Y_0, r1[i]))
                else:
                    sak = (ea + sas) / 2
                    sam = (sas + sek) / 2
                    san = (ea + sek) / 2
                    if (sak > sas and sak < ea):
                        sak = 180 + sak
                    e = math.cos(math.radians(sak))
                    h = math.sin(math.radians(sak))
                    x_2 = cx1[i] + (r1[i] * e)
                    y_2 = cy1[i] + (r1[i] * h)
                    print("G00 Z0.2")
                    print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                    print("G01 Z{0}".format(z22))
                    print("G02 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x_2, y_2, r1[i]))
                    print("G02 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X_0, Y_0, r1[i]))
            elif Name[i] == "Ellipse":
                x_0 = cx1[i] + ma[i]
                y_0 = cy1[i]
                X_0 = cx1[i] - ma[i]
                Y_0 = cy1[i]
                x_1 = cx1[i]
                y_1 = cy1[i] + mina[i]
                X_1 = cx1[i]
                Y_1 = cy1[i] - mina[i]
                print("G00 Z0.2")
                print("G00 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                print("G01 Z{0}".format(z22))
                if (ma[i] > mina[i] and ma[i] < 100):
                    v = x_0
                    q = y_0
                    while (y_0 != y_1):
                        y_0 = y_0 + 0.2
                        if (y_0 > y_1):
                            y_0 = y_1
                        L = (y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (L > 1):
                            l1 = cmath.sqrt(1 - L)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - L)
                            W = ma[i] * l1
                        x_0 = cx1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                    while (y_1 != Y_0):
                        y_1 = y_1 - 0.2
                        if (y_1 < Y_0):
                            y_1 = Y_0
                        l = (y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = ma[i] * l1
                        x_1 = cx1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                    while (Y_0 != Y_1):
                        Y_0 = Y_0 - 0.2
                        if (Y_0 < Y_1):
                            Y_0 = Y_1
                        L = (Y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (L > 1):
                            l1 = cmath.sqrt(1 - L)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - L)
                            W = ma[i] * l1
                        X_0 = cx1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                    while (Y_1 != q):
                        Y_1 = Y_1 + 0.2
                        if (Y_1 > q):
                            Y_1 = q
                        L = (Y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (L > 1):
                            l1 = cmath.sqrt(1 - L)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - L)
                            W = ma[i] * l1
                        X_1 = cx1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                if (mina[i] > ma[i] and mina[i] < 100):
                    v = x_0
                    q = y_0
                    while (x_0 != x_1):
                        x_0 = x_0 - 0.2
                        if (x_0 < x_1):
                            x_0 = x_1
                        l = (x_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1

                        y_0 = cy1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                    while (x_1 != X_0):
                        x_1 = x_1 - 0.2
                        if (x_1 < X_0):
                            x_1 = X_0
                        l = (x_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1
                        y_1 = cy1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                    while (X_0 != X_1):
                        X_0 = X_0 + 0.2
                        if (X_0 > X_1):
                            X_0 = X_1
                        l = (X_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1
                        Y_0 = cy1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                    while (X_1 != v):
                        X_1 = X_1 + 0.2
                        if (X_1 > v):
                            X_1 = v
                        l = (X_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1
                        Y_1 = cy1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                if (ma[i] > mina[i] and ma[i] > 100):
                    v = x_0
                    q = y_0
                    while (y_0 != y_1):
                        y_0 = y_0 + 15
                        if (y_0 > y_1):
                            y_0 = y_1
                        L = (y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (L > 1):
                            l1 = cmath.sqrt(1 - L)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - L)
                            W = ma[i] * l1
                        x_0 = cx1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                    while (y_1 != Y_0):
                        y_1 = y_1 - 15
                        if (y_1 < Y_0):
                            y_1 = Y_0
                        l = (y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = ma[i] * l1
                        x_1 = cx1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                    while (Y_0 != Y_1):
                        Y_0 = Y_0 - 15
                        if (Y_0 < Y_1):
                            Y_0 = Y_1
                        L = (Y_0 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (L > 1):
                            l1 = cmath.sqrt(1 - L)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - L)
                            W = ma[i] * l1
                        X_0 = cx1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                    while (Y_1 != q):
                        Y_1 = Y_1 + 15
                        if (Y_1 > q):
                            Y_1 = q
                        L = (Y_1 - cy1[i]) ** 2 / (mina[i]) ** 2
                        if (L > 1):
                            l1 = cmath.sqrt(1 - L)
                            l2 = l1.real
                            W = ma[i] * l2
                        else:
                            l1 = math.sqrt(1 - L)
                            W = ma[i] * l1
                        X_1 = cx1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
                if (mina[i] > ma[i] and mina[i] > 100):
                    v = x_0
                    q = y_0
                    while (x_0 != x_1):
                        x_0 = x_0 - 15
                        if (x_0 < x_1):
                            x_0 = x_1
                        l = (x_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1

                        y_0 = cy1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_0, y_0))
                    while (x_1 != X_0):
                        x_1 = x_1 - 15
                        if (x_1 < X_0):
                            x_1 = X_0
                        l = (x_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1
                        y_1 = cy1[i] + W
                        print("G01 X{0:.4f} Y{1:.4f}".format(x_1, y_1))
                    while (X_0 != X_1):
                        X_0 = X_0 + 15
                        if (X_0 > X_1):
                            X_0 = X_1
                        l = (X_0 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1
                        Y_0 = cy1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_0, Y_0))
                    while (X_1 != v):
                        X_1 = X_1 + 15
                        if (X_1 > v):
                            X_1 = v
                        l = (X_1 - cx1[i]) ** 2 / (ma[i]) ** 2
                        if (l > 1):
                            l1 = cmath.sqrt(1 - l)
                            l2 = l1.real
                            W = mina[i] * l2
                        else:
                            l1 = math.sqrt(1 - l)
                            W = mina[i] * l1
                        Y_1 = cy1[i] - W
                        print("G01 X{0:.4f} Y{1:.4f}".format(X_1, Y_1))
            elif Name[i] == "Circle":
                x = cx1[i] + r1[i]
                y = cy1[i]
                X = cx1[i] - r1[i]
                Y = cy1[i]
                print("G00 Z0.2")
                print("G00 X{0:.4f} Y{1:.4f}".format(x, y))
                print("G01 Z{0}".format(z22))
                print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(X, Y, r1[i]))
                print("G03 X{0:.4f} Y{1:.4f} R{2:.4f}".format(x, y, r1[i]))

            elif Name[i] == 'Line':
                print("G00 Z0.2")
                print("G00 X{0:.4f} Y{1:.4f}".format(x1[i], y1[i]))
                print("G01 Z{0}".format(z22))
                print("G01 X{0:.4f} Y{1:.4f}".format(x2[i], y2[i]))

        print("G00 Z10")



    print("G91 G28 X0 Y0 Z0")
    print("M05")
    print("M30")
    print("\n")
    print("\n")
    print("\n")
    if i_4==K:
        a1.say("There's your G-code ! Thank You!")
        a1.runAndWait()
    else:
        a1.say("Fill the sheet that pops up and after filling the sheet click 'GETCODE'.")
        a1.runAndWait()
def file():
    a1.say("choose the excel file that you have got for the plot in Autocad !")
    a1.runAndWait()
    global loc
    loc=filedialog.askopenfilename(initialdir='/')


def next():
    global temp
    global i_4
    global vr1
    global vr2
    global vr3
    global vr4
    global vr5
    global vr11
    global n_3
    global i_4
    if i_4==0:
        w.destroy()
        temp = Tk()
        h = temp.winfo_screenheight()
        wid = temp.winfo_screenwidth()
        temp.geometry("%sx%s" % (int(0.75 * int(wid)), int(h)))
        temp.title("WELCOME TO G-CODE GENERATOR")
        vr1 = IntVar()
        a1.say("Fill the sheet that pops up")
        a1.runAndWait()
        a1.say("After filling the sheet click get code!")
        a1.runAndWait()
        t4 = Label(temp, text="Direction of spindle :", font=("times new roman", 12, "bold")).place(x=300, y=60)
        r1 = Radiobutton(temp, text="CLOCK-WISE", variable=vr1, value=1)
        r1.place(x=500, y=60)
        r2 = Radiobutton(temp, text="ANTICLOCK-WISE", variable=vr1, value=2)
        r2.place(x=700, y=60)
        t3 = Label(temp, text="Depth of Cut :", font=("times new roman", 12, "bold"))
        t3.place(x=350, y=480)
        t9 = Label(temp, text="Multiple depths(with an increament of 0.5) :", font=("times new roman", 12, "bold"))
        t9.place(x=155, y=520)
        vr11 = IntVar()
        r33 = Radiobutton(temp, text="Yes", variable=vr11, value=1).place(x=500, y=520)
        r44 = Radiobutton(temp, text='No', variable=vr11, value=2).place(x=700, y=520)
        n_3 = StringVar()
        e3 = Entry(temp, textvar=n_3)
        e3.place(x=500, y=480)
        vr2 = IntVar()
        r3 = Radiobutton(temp, text="Flat head", variable=vr2, value=1).place(x=500, y=140)
        r4 = Radiobutton(temp, text='Bull head', variable=vr2, value=2).place(x=500, y=160)
        r5 = Radiobutton(temp, text='Ball head', variable=vr2, value=3).place(x=500, y=180)
        r6 = Radiobutton(temp, text="Drill", variable=vr2, value=4).place(x=500, y=200)
        r7 = Radiobutton(temp, text='Slot Cutter', variable=vr2, value=5).place(x=500, y=220)
        r8 = Radiobutton(temp, text="Threading tap", variable=vr2, value=6).place(x=500, y=240)
        r9 = Radiobutton(temp, text='Face Cutter', variable=vr2, value=7).place(x=500, y=260)
        vr3 = IntVar()
        r11 = Radiobutton(temp, text='Aluminium', variable=vr3, value=1500).place(x=500, y=300)
        r12 = Radiobutton(temp, text='Brass', variable=vr3, value=1550).place(x=500, y=320)
        r13 = Radiobutton(temp, text='Copper', variable=vr3, value=1600).place(x=500, y=340)
        r14 = Radiobutton(temp, text='Steel', variable=vr3, value=1650).place(x=500, y=360)
        r15 = Radiobutton(temp, text='Titanium', variable=vr3, value=1700).place(x=500, y=380)
        r16 = Radiobutton(temp, text='Wood', variable=vr3, value=1750).place(x=500, y=400)
        r17 = Radiobutton(temp, text='fibre glass', variable=vr3, value=1800).place(x=500, y=420)
        r18 = Radiobutton(temp, text='Plastic', variable=vr3, value=1850).place(x=500, y=440)
        t5 = Label(temp, text="Select a File(.xls) :", font=("times new roman", 12, "bold")).place(x=315, y=100)
        t6 = Label(temp, text="Tool :", font=("times new roman", 12, "bold")).place(x=400, y=140)
        t3 = Label(temp, text="Material used :", font=("times new roman", 12, "bold")).place(x=340, y=300)
        butt = Button(temp, text='Select a file', command=file).place(x=500, y=100)
        t8 = Label(temp, text="Unit :", font=("times new roman", 12, "bold")).place(x=410, y=560)
        t9 = Label(temp, text="Feed Unit :", font=("times new roman", 12, "bold")).place(x=375, y=600)
        vr5 = IntVar()
        vr4 = IntVar()
        r19 = Radiobutton(temp, text='Inch', variable=vr4, value=2).place(x=500, y=560)
        r20 = Radiobutton(temp, text='mm', variable=vr4, value=1).place(x=700, y=560)
        r21 = Radiobutton(temp, text='inches/min', variable=vr5, value=2).place(x=500, y=600)
        r22 = Radiobutton(temp, text='mm/min', variable=vr5, value=1).place(x=700, y=600)
        butt1 = Button(temp, text='GET CODE', command=getcode).place(x=350, y=680)
        butt2 = Button(temp, text='NEXT', command=next).place(x=550, y=680)
        i_4 = i_4 + 1
        temp.mainloop()

    elif 0<i_4<K:
        temp.destroy()
        temp = Tk()
        h = temp.winfo_screenheight()
        wid = temp.winfo_screenwidth()
        temp.geometry("%sx%s" % (int(0.75 * int(wid)), int(h)))
        temp.title("WELCOME TO G-CODE GENERATOR")
        vr1 = IntVar()
        t4 = Label(temp, text="Direction of spindle :", font=("times new roman", 12, "bold")).place(x=300, y=60)
        r1 = Radiobutton(temp, text="CLOCK-WISE", variable=vr1, value=1)
        r1.place(x=500, y=60)
        r2 = Radiobutton(temp, text="ANTICLOCK-WISE", variable=vr1, value=2)
        r2.place(x=700, y=60)
        t3 = Label(temp, text="Depth of Cut :", font=("times new roman", 12, "bold"))
        t3.place(x=350, y=480)
        t9 = Label(temp, text="Multiple depths(with an increament of 0.5) :", font=("times new roman", 12, "bold"))
        t9.place(x=155, y=520)
        vr11=IntVar()
        r33 = Radiobutton(temp, text="Yes", variable=vr11, value=1).place(x=500, y=520)
        r44 = Radiobutton(temp, text='No', variable=vr11, value=2).place(x=700, y=520)
        n_3 = StringVar()
        e3 = Entry(temp, textvar=n_3)
        e3.place(x=500, y=480)
        vr2 = IntVar()
        r3 = Radiobutton(temp, text="Flat head", variable=vr2, value=1).place(x=500, y=140)
        r4 = Radiobutton(temp, text='Bull head', variable=vr2, value=2).place(x=500, y=160)
        r5 = Radiobutton(temp, text='Ball head', variable=vr2, value=3).place(x=500, y=180)
        r6 = Radiobutton(temp, text="Drill", variable=vr2, value=4).place(x=500, y=200)
        r7 = Radiobutton(temp, text='Slot Cutter', variable=vr2, value=5).place(x=500, y=220)
        r8 = Radiobutton(temp, text="Threading tap", variable=vr2, value=6).place(x=500, y=240)
        r9 = Radiobutton(temp, text='Face Cutter', variable=vr2, value=7).place(x=500, y=260)
        vr3 = IntVar()
        r11 = Radiobutton(temp, text='Aluminium', variable=vr3, value=1500).place(x=500, y=300)
        r12 = Radiobutton(temp, text='Brass', variable=vr3, value=1550).place(x=500, y=320)
        r13 = Radiobutton(temp, text='Copper', variable=vr3, value=1600).place(x=500, y=340)
        r14 = Radiobutton(temp, text='Steel', variable=vr3, value=1650).place(x=500, y=360)
        r15 = Radiobutton(temp, text='Titanium', variable=vr3, value=1700).place(x=500, y=380)
        r16 = Radiobutton(temp, text='Wood', variable=vr3, value=1750).place(x=500, y=400)
        r17 = Radiobutton(temp, text='fibre glass', variable=vr3, value=1800).place(x=500, y=420)
        r18 = Radiobutton(temp, text='Plastic', variable=vr3, value=1850).place(x=500, y=440)
        t5 = Label(temp, text="Select a File(.xls) :", font=("times new roman", 12, "bold")).place(x=315, y=100)
        t6 = Label(temp, text="Tool :", font=("times new roman", 12, "bold")).place(x=400, y=140)
        t3 = Label(temp, text="Material used :", font=("times new roman", 12, "bold")).place(x=340, y=300)
        butt = Button(temp, text='Select a file', command=file).place(x=500, y=100)
        t8 = Label(temp, text="Unit :", font=("times new roman", 12, "bold")).place(x=410, y=560)
        t9 = Label(temp, text="Feed Unit :", font=("times new roman", 12, "bold")).place(x=375, y=600)
        vr5 = IntVar()
        vr4 = IntVar()
        r19 = Radiobutton(temp, text='Inch', variable=vr4, value=2).place(x=500, y=560)
        r20 = Radiobutton(temp, text='mm', variable=vr4, value=1).place(x=700, y=560)
        r21 = Radiobutton(temp, text='inches/min', variable=vr5, value=2).place(x=500, y=600)
        r22 = Radiobutton(temp, text='mm/min', variable=vr5, value=1).place(x=700, y=600)
        butt1 = Button(temp, text='GET CODE', command=getcode).place(x=350, y=680)
        butt2 = Button(temp, text='NEXT', command=next).place(x=550, y=680)
        i_4 = i_4 + 1

        temp.mainloop()

    else:
        exit()
butt1=Button(w,text='ENTER',command=enter).place(x=150,y=180)
butt3=Button(w,text='NEXT',command=next).place(x=250,y=180)

a1.say("Enter number of tools require to make the model,in the window that pops up.")
a1.runAndWait()
l4=Label(w,text="number of tools require to make the model :",font=("times new roman",12,"bold")).place(x=50,y=60)
a1.say("After entering the number of tools click enter!.")
a1.runAndWait()
n_9=StringVar()
e3=Entry(w,textvar=n_9)
e3.place(x=350,y=60)
w.mainloop()