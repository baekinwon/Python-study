# * coding:utf 8 *
from tkinter import *
import webbrowser
a = Tk()
a.geometry('400x300+100+200')
a.title("시간표")
ch1 = IntVar()
ch2 = IntVar()
def w_1(): #아침조회
    webbrowser.open("https://us02web.zoom.us/j/9453745562?pwd=cFNuWXVrL2NFSjByMEllajZuMGgxdz09")
def w_2(): #빅분
    webbrowser.open("https://us04web.zoom.us/j/6506885395?pwd=ZTRVOWJicUlZVHgyMUE5dVZ1OFJKQT09")
def w_3():#영어
    webbrowser.open("https://zoom.us/j/2435254903?pwd=ZE5ldUpxK1lTYVErdFFMUkNOZnhDQT09")
def w_4():#구글 미트
    webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
def w_5():#한국사
    webbrowser.open("https://us02web.zoom.us/j/3037298476?pwd=MEFpR251N1BqQnJsc3dnY3F5RW1mdz09")
def w_6():#문학
    webbrowser.open("https://zoom.us/j/2680355224?pwd=RVVDeXNMeFpJNGVTTmdYcHRSTjFvZz09")
def w_7():#수학
    webbrowser.open("https://zoom.us/j/9130644035?pwd=b213b25jWWJKeHNvRUlMbUlUeHhCUT09")
def w_8():#일본어
    webbrowser.open("https://zoom.us/j/5900838939?pwd=UlAyUU5KV3FGcGdXV3A0emhuc21IZz09")
def w_9():#운건
    webbrowser.open("https://us02web.zoom.us/j/5879314926?pwd=b3lRQmJMSktMUS9IZ0x3OGRHWDRMdz09")
def w_10():#응프
    webbrowser.open("https://zoom.us/j/5604977447?pwd=ZnlpMjYxNmRqK2tSOEdEWmV6TUM3UT09")
def w_11():#사회
    webbrowser.open("https://zoom.us/j/5560411264?pwd=SEI3Z3Q4akU5N2ROa0dwWTBpZlFNdz09")
####################################################################
btn = Button(a,text="아침조회",command=w_1).grid(row=3,column=0)
btn_1 = Button(a,text="빅분",command=w_2).grid(row=4,column=0)
btn_2 = Button(a,text="빅분",command=w_2).grid(row=6,column=0)
btn_3 = Button(a,text="영어",command=w_3).grid(row=7,column=0)
btn_4 = Button(a,text="자율",command=w_4).grid(row=8,column=0)
btn_5 = Button(a,text="한국사",command=w_5).grid(row=9,column=0)
btn_6 = Button(a,text="진로",command=w_4).grid(row=10,column=0)
btn_7 = Button(a,text="문학",command=w_6).grid(row=11,column=0)
###################################################################
btn1 = Button(a,text="영어",command=w_3).grid(row=4,column=3)
btn2 = Button(a,text="수학",command=w_7).grid(row=6,column=3)
btn3 = Button(a,text="일본어",command=w_8).grid(row=7,column=3)
btn4 = Button(a,text="운건",command=w_9).grid(row=8,column=3)
btn5 = Button(a,text="자료",command=w_4).grid(row=9,column=3)
btn6 = Button(a,text="자료",command=w_4).grid(row=10,column=3)
btn7 = Button(a,text="빅분",command=w_2).grid(row=11,column=3)
#####################################################################
btna = Button(a,text="영어",command=w_3).grid(row=4,column=6)
btnb = Button(a,text="과학",command=w_4).grid(row=6,column=6)
btnc = Button(a,text="한국사",command=w_5).grid(row=7,column=6)
btnd = Button(a,text="데베",command=w_1).grid(row=8,column=6)
btne = Button(a,text="응프",command=w_10).grid(row=9,column=6)
btnf = Button(a,text="응프",command=w_10).grid(row=10,column=6)
btng = Button(a,text="응프",command=w_10).grid(row=11,column=6)
############################################################################
btnaa = Button(a,text="한국사",command=w_5).grid(row=4,column=9)
btnbb= Button(a,text="일본어",command=w_8).grid(row=6,column=9)
btncc = Button(a,text="운건",command=w_9).grid(row=7,column=9)
btndd = Button(a,text="응프",command=w_10).grid(row=8,column=9)
btnee = Button(a,text="사회",command=w_11).grid(row=9,column=9)
btnff = Button(a,text="수학",command=w_7).grid(row=10,column=9)
btngg = Button(a,text="영어",command=w_3).grid(row=11,column=9)
############################################################################
btnaa_1= Button(a,text="데베",command=w_1).grid(row=4,column=12)
btnbb_2= Button(a,text="데베",command=w_1).grid(row=6,column=12)
btncc_3 = Button(a,text="데베",command=w_1).grid(row=7,column=12)
btndd_4 = Button(a,text="문학",command=w_6).grid(row=8,column=12)
btnee_5 = Button(a,text="창체",command=w_1).grid(row=9,column=12)
btnff_6 = Button(a,text="창체",command=w_1).grid(row=10,column=12)
############################################################################
a.mainloop()