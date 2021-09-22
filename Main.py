from keyboard import *
from time import *
from pyautogui import *
from threading import *
from tkinter import *
from tkinter.font import *
from os import *

x2=" "
y2=""
x=""
y=""
change=True
timeCnt=0
exitBool=False

def reset():
    global x,y
    global x2,y2
    sleep(0.5)
    while True:
        x,y=position()
        if change:
            if x!=x2 or y!=y2:
                x2=x
                y2=y
                pos.config(text="({0},{1})".format(x,y))
        if exitBool==True:
            return 0

def log():
    global change,exitBool
    sleep(0.5)
    while True:
        if is_pressed("alt")==True:
            change=False
            pos.config(fg="red")
        elif is_pressed("alt")==False:
            change=True
            pos.config(fg="black")
            
def timeSet():
    global timeCnt
    txt=""
    sleep(0.5)
    while True:
        sleep(0.01)
        timeCnt+=0.01
        if timeCnt<60:
            txt=("누적 시간 : %.2f"%(timeCnt))
        elif timeCnt<3600 and timeCnt>=60:
            txt=("누적 시간 : %d분 %.2f초"%(timeCnt/60,timeCnt%60))
        timeLabel.config(text=txt)
        if exitBool==True:
            return 0

th=Thread(target=reset)
th2=Thread(target=log)
th3=Thread(target=timeSet)
th.start()
th2.start()
th3.start()

root=Tk()
root.title("좌표 확인")
root.geometry("220x100")

base_font=Font(size=20)
time_font=Font(size=10)

pos=Label(text="(x,y)",font=base_font)
pos.place(x=5,y=5)
timeLabel=Label(text="누적 시간 : 0초",fg="green",font=time_font)
timeLabel.place(x=5,y=50)

root.mainloop()
