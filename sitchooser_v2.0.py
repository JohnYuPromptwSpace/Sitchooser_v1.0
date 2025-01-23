from tkinter import *
import random as r
import tkinter.font as font
import time as t

window = Tk()
window.title("Sitchooser_v1.0 - inspired by Jiwon Yu - 2021.11.")

cl = []
bl = []


per =0
line = 0
pn_1 = 0
pn_2 = 0

def getentry():
    global per, line
    per = int(ep.get())
    line = int(el.get())

def getentrypn():
    global  pn_1, pn_2
    pn_1 = int(epn.get())
    pn_2 = int(epnn.get())    

def chosn(w):
    global per
    cs = 0

    while cs in cl or cs == 0:
        cs = r.randint(1,per)
    return cs

def renderbutton(ti,tj,xr,r=0):
    buttontext = cl[ti*line+xr]
    button = Button(bf,text = buttontext ,bg = "white", fg = "black", font = font.Font(size=20))
    button.grid(row = ti+r, column = xr ,sticky = W + E + N + S, ipadx=20, ipady=20)
    bl.append(button)

def makebutton():
    global per, line
    i, j = 0, 0
    for i in range(per//line):
        for j in range(line):
            renderbutton(i, j,j)
    for x in range(per % line):
        renderbutton(i, j, x , 1)

def update():
    deleat()
    getentry()
    for i in range(per):
        cl.append(0)
    makebutton()
    cl.clear()
    for i in range(per):
        button = bl[i]
        bn = chosn(i)
        cl.append(bn)
        if bn == 0:
            bn = " - "
        button["text"] = bn
        
def changesit():
    global per, pn_1, pn_2

    getentrypn()
    getentry()
    for i in range(per):
        button = bl[i]
        buttont = button["text"]
        if buttont == pn_1:
            button["text"] = pn_2
            b1 = button
        elif buttont == pn_2:
            button["text"] = pn_1
            b2 = button
        
    b1.flash()
    b2.flash()
        
def deleat():       
    while 0 < len(bl):
        button = bl[0]
        button.destroy()
        bl.remove(button)

uif = Frame(window)
bf = Frame(window)
uif.pack()
bf.pack()
lp = Label(uif,text = "인원수").grid(row = 1, column = 0)
ll = Label(uif,text = "세로줄").grid(row = 1,column = 1)

ep = Entry(uif)
el = Entry(uif)
reb = Button(uif,text = "  배정  ", bg = "white", fg = "black",command = update)
ll = Label(uif,text = "자리 변경(배정후 번호 입력시 두 번호의 자리가 바뀜)").grid(row = 3,column = 0,columnspan = 2)
epn = Entry(uif)
epnn = Entry(uif)
csb = Button(uif,text = "  자리 바꾸기  ", bg = "white", fg = "black",command = changesit)

ep.grid(row = 2,column = 0)
el.grid(row = 2,column = 1)
reb.grid(row = 2, column = 2)
epn.grid(row = 4,column = 0)
epnn.grid(row = 4,column = 1)
csb.grid(row = 4,column = 2)


window.mainloop()