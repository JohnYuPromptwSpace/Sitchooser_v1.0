from tkinter import *
from tkinter.font import Font
import random as r
import time as t

buttonList = []

def delbutton():       
    while buttonList:
        button = buttonList[0]
        button.destroy()
        buttonList.remove(button)

def genButton(textBtn):
    button = Label(sitFrame,text = textBtn ,bg = "white", fg = "black", font = Font(size=20), width=6, height=3, borderwidth=2, relief="groove", pady=7)
    return button

def renderButton():
    delbutton()
    peo = int(peoEntry.get())
    sitData = [x for x in range(1,peo+1)]
    r.shuffle(sitData)
    col = int(colEntry.get())
    
    for x in range(len(sitData)):
        currBtn = genButton(sitData[x])
        buttonList.append(currBtn)
        currBtn.grid(row=x//col, column=x%col, sticky=W+E+S+N)

def sitUpdate():
    sit1 = int(sit1Entry.get())
    sit2 = int(sit2Entry.get())
    for i in range(len(buttonList)):
        if buttonList[i]['text'] == sit1:
            btn1 = buttonList[i]
        elif buttonList[i]['text'] == sit2:
            btn2 = buttonList[i]
    btn1['text'] = sit2
    btn1['bg'] = '#76EE00'
    btn2['text'] = sit1
    btn2['bg'] = '#76EE00'
    window.update()
    t.sleep(0.1)
    btn1['bg'] = 'white'
    btn2['bg'] = 'white'
    

window = Tk()
window.configure(bg = 'white')
window.title("Sitchooser_v3.0")

uiFrame = Frame(window, bg='white')

peoLabel = Label(uiFrame, text="전체 인원수", bg = "white", pady=5).grid(row = 0, column = 0)
colLabel = Label(uiFrame, text="전체 줄 수", bg = "white", pady=5).grid(row = 0, column = 1)

peoEntry = Entry(uiFrame)
colEntry = Entry(uiFrame)

sitButton = Button(uiFrame, text = "자리 배정", bg = "white", fg = "black", width=13, command=renderButton)

reLabel = Label(uiFrame,text = "자리 변경(배정 후 번호 입력시 두 번호의 자리가 바뀜)", width=50, bg = "white").grid(row = 2, column = 0, columnspan=2, pady=(5,0))

peoLabel = Label(uiFrame, text="전체 인원수", bg = "white", pady=5).grid(row = 3, column = 0)
colLabel = Label(uiFrame, text="전체 줄 수", bg = "white", pady=5).grid(row = 3, column = 1)

sit1Entry = Entry(uiFrame)
sit2Entry = Entry(uiFrame)
sitChButton = Button(uiFrame,text = "자리 바꾸기", bg = "white", fg = "black", width=13, command=sitUpdate)

desklLabel = Label(uiFrame, text="교탁", bg = "white", pady=5, font=Font(size=20), borderwidth=2, relief="groove", width=7).grid(row = 4, column = 0, columnspan=3, pady=5)

peoEntry.grid(row = 1, column = 0)
colEntry.grid(row = 1, column = 1)
sitButton.grid(row = 0, column = 2, rowspan=2, sticky=N+W+S+E)
sit1Entry.grid(row = 3, column = 0)
sit2Entry.grid(row = 3, column = 1)
sitChButton.grid(row = 2, column = 2, rowspan=2, sticky=N+W+S+E)

sitFrame = Frame(window, bg = "white")

uiFrame.pack()
sitFrame.pack()

window.mainloop()