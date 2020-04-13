#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:18:02 2020

@author: cp
"""
from os import path
from tkinter import * 
from encryptor import Encryptor

class Gui:
    flag = 1
    window = Tk()
    window.geometry("430x450")
    window.resizable(0, 0) 
    window.title("Installation Wizard")
    e = Encryptor()
    
#    def btn_click(self, item):
#        global expression
#        expression = expression + str(item)
#        input_text.set(expression)
#    
#    def btn_clear(self):
#        global expression
#        expression = ""
#        input_text.set("")
#     
#    def btn_equal(self):
#        global expression
#        result = str(eval(expression)) 
#        input_text.set(result)
#        expression = ""

        
    def execute(self,flag):
        if path.exists("./network/encryptor/network.json"):
            self.labelText.set("Application is already installed in your system\nClose this window and launch the application")
        else:
            global expression
            expression = ""
            self.labelText.set("Installing the encryptor\nSee terminal for details")
            self.e.main()
            self.labelText.set("Installation Finished")
            self.flag = 0
        
        
    def destroy_session(self, window):
        window.destroy()
        

     
    expression = ""
     
    
    
    
     
    input_text = StringVar()
    labelText = StringVar()
    
    
     
    input_frame = Frame(window, 
                        width = 312, 
                        height = 50, 
                        bd = 0, 
                        highlightbackground = "black", 
                        highlightcolor = "black", 
                        highlightthickness = 1)
     
    input_frame.pack(side = TOP)
     
    
     
    input_field = Entry(input_frame, 
                        font = ('arial', 18, 'bold'), 
                        textvariable = input_text, 
                        width = 50, bg = "#eee", 
                        bd = 0, justify = RIGHT)
     
    input_field.grid(row = 0, column = 0)
     
    input_field.pack(ipady = 10) 
     
    
    
    
    btns_frame = Frame(window, width = 312, height = 272.5)
     
    btns_frame.pack(side=TOP)
    
    btns_frame2 = Frame(window, width = 312, height = 72.5, bg = "grey")
     
    btns_frame2.pack(side=BOTTOM)
    
    label = Label(btns_frame, 
                  text = "Neural Encryptor", 
                  fg = "Red", 
                  width = 55, 
                  height = 3, 
                  bd = 0, 
                  bg = "#cfa").grid(row = 0, 
                                    column = 0, 
                                    columnspan = 2,
                                    )
    
     
    
    install = Button(btns_frame, 
                   text = "Install", 
                   fg = "black", 
                   font=('Times new roman', 12, 'bold'),
                   width = 24,
                   height = 3, 
                   bd = 2, 
                   bg = "#fff", 
                   cursor = "hand2", 
                   command = lambda: Gui().execute(Gui().flag)).grid(row = 1, 
                                              column = 0, )
     
    destroy = Button(btns_frame, 
                   text = "Exit", 
                   fg = "black",
                   font=('Times new roman', 12, 'bold'),
                   width = 24,
                   height = 3, 
                   bd = 2, 
                   bg = "#fff", 
                   cursor = "hand2", 
                   command = lambda: Gui().destroy_session(Gui().window)).grid(row = 1, 
                                              column = 1,)
     
    message = Label(btns_frame, 
                  textvariable = labelText, 
                  fg = "Black",
                  font=('Times new roman', 12, 'bold'),
                  width = 55, 
                  height = 12, 
                  bd = 0, 
                  ).grid(row = 2, 
                                    column = 0,
                                    columnspan = 2,
                                    pady = 5,
                                    )
    
    s = "Developed by : Saketh G"
    
    label2 = Label(btns_frame2, 
                  text = s, 
                  fg = "Black", 
                  width = 55, 
                  height = 1, 
                  bd = 0, 
                  bg = "#cfa").grid(row = 3, 
                                    column = 0,
                                    columnspan = 2
                                    )
     

Gui().window.mainloop()
