#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" 文档注释 """

__author__ = 'dwh'

# 2018/12/15 17:17

import tkinter as tk
4

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.hi_there = tk.Button(frame, text="打招呼", fg="blue")
        self.hi_there.pack()


root = tk.Tk()
app = App(root)

root.mainloop()
