#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jeng
#
# Created:     17/11/2014
# Copyright:   (c) jeng 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from sys import argv
from tkinter import *
import tkFileDialog
import training
import test
import re_bpnn_final
import time

視窗 = Tk()

frame = Frame(視窗, width=500, height=550)
frame.pack()


def 選():
    對照 = dict()
    對照[1]="左邊的貓"
    對照[2]="中間的貓"
    對照[3]="右邊的貓"
    狀況欄["text"]="你目前選了 " + 對照[選哪個.get()]

選哪個 = IntVar()

圖1 = PhotoImage(file="D:/類神經網路/貓/選項圖/選項1.gif")
選項1 = Radiobutton(視窗,image = 圖1, variable=選哪個, value=1,command=選)
選項1.place(relx=.01, rely=.6)

圖2 = PhotoImage(file="D:/類神經網路/貓/選項圖/選項2.gif")
選項2 = Radiobutton(視窗,image = 圖2, variable=選哪個, value=2,command=選)
選項2.place(relx=.35, rely=.6)

圖3 = PhotoImage(file="D:/類神經網路/貓/選項圖/選項3.gif")
選項3 = Radiobutton(視窗,image = 圖3, variable=選哪個, value=3,command=選)
選項3.place(relx=.69, rely=.6)

選項1.select()



狀況欄 = Label(視窗,text="請選擇下列想辨識的貓，然後按下測驗\n或是訓練網路",font=(20))
狀況欄.place(relx=.5, rely=.3,anchor="c")
#狀況欄.pack(side=BOTTOM,pady=30)



def 訓練():
    #狀況欄["text"]="訓練中..."
    #time.sleep(1.0)
    狀況欄["text"]=training.main()

訓練鈕 = Button(視窗,text="訓練",width=10,font=(20),command=訓練)
訓練鈕.place(relx=.1, rely=.1)
#訓練鈕.pack(side=LEFT,padx=20, pady=30)


def 測驗():
    #print(filename)
    #狀況欄["text"]=test.main(filename)
    pass

測驗鈕 = Button(視窗,text="測驗",width=10,font=(20),command=測驗)
測驗鈕.place(relx=.7, rely=.1)
#測驗鈕.pack(side=RIGHT,padx=20, pady=30)



def 輸入檔案並測驗():
    filename = tkFileDialog.askopenfilename()
    print(filename)
    狀況欄["text"]= "我覺得這是" + test.main(filename)


輸入檔案鈕 = Button(視窗,text="輸入檔案並測驗",width=15,font=(20),command=輸入檔案並測驗)
輸入檔案鈕.place(relx=.38, rely=.9)

視窗.title("DEMO")
視窗.mainloop()
