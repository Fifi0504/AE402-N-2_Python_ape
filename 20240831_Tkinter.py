# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:52:17 2024

@author: UX6404_SL
"""

import tkinter as tk
import tkinter.messagebox

def clickMe():
    tkinter.messagebox.showinfo(title='提示',message='好痛')
window = tk.Tk()

window.title("我的第一個GUI程式")

window.geometry('300x300')

label = tk.Label(window,text="我的GUI")

label = tk.Label(window,text="我的GUI",bg="#05F",fg="#5FC")


label.pack()

entry = tk.Entry(window,width = 30)
entry.pack()

button = tk.Button(window,text = "按鈕",command = clickMe)
button.pack()

window.mainloop()






