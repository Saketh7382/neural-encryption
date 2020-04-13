#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:47:23 2020

@author: cp
"""

from os import path
from tkinter import *
from tkinter.filedialog import askopenfilename
from encryptor import Encryptor
from functions import Functionalities

class Application:
    flag = 1
    window = Tk()
    window.geometry("445x470")
    #window.resizable(0, 0) 
    window.title("Neural Encryptor")
    e = Encryptor()
    func = Functionalities() 
    
        
    def encrypt_function(self):
        if path.exists("./network/encryptor/network.json"):
            self.filename = askopenfilename(initialdir =  "/home/cp/Documents/Hackathon", title = "Select A File")
            s = self.func.beginEncryption(self.filename)
            self.labelText.set(s)
        else:
            s = "Encryptor is not installed in your system"
            s += "\nPlease Install the Encryptor"
            self.labelText.set(s)
        
    def decrypt_function(self):
        if path.exists("./network/encryptor/network.json"):
            self.filename = askopenfilename(initialdir =  "./data/encrypted", title = "Select A File")
            s = self.func.beginDecryption(self.filename)
            self.labelText.set(s)
        else:
            s = "Encryptor is not installed in your system"
            s += "\nPlease Install the Encryptor"
            self.labelText.set(s)
        
    def check_efficiency(self):
        if path.exists("./network/encryptor/network.json"):
            s = self.func.checkEfficiency()
            self.labelText.set(s)
        else:
            s = "Encryptor is not installed in your system"
            s += "\nPlease Install the Encryptor"
            self.labelText.set(s)
        
    def destroy_session(self, window):
        window.destroy()
        
   
     
    expression = ""  
     
    input_text = StringVar()
    labelText = StringVar()
    
    
    btns_frame =  Frame(window, width = 55, height = 272.5)
     
    btns_frame.pack(side= TOP)
    
    btns_frame2 =  Frame(window, width = 55, height = 72.5, bg = "grey")
     
    btns_frame2.pack(side= BOTTOM)

    
    label =  Label(btns_frame, 
                  text = "Welcome to Neural Encryptor", 
                  fg = "Red",
                  width = 55,
                  height = 3, 
                  bd = 0, 
                  bg = "#cfa").grid(row = 0, 
                                    column = 0,
                                    )
    
     
    
    encrypt =  Button(btns_frame, 
                   text = "Encrypt a file", 
                   fg = "black", 
                   font=('Times new roman', 12, 'bold'),
                   width = 50,
                   height = 3, 
                   bd = 2, 
                   bg = "#fff", 
                   cursor = "hand2", 
                   command = lambda: Application().encrypt_function()).grid(row = 1, 
                                              column = 0, )
     
    decrypt =  Button(btns_frame, 
                   text = "Decrypt a file", 
                   fg = "black",
                   font=('Times new roman', 12, 'bold'),
                   width = 50,
                   height = 3, 
                   bd = 2, 
                   bg = "#fff", 
                   cursor = "hand2", 
                   command = lambda: Application().decrypt_function()).grid(row = 2, 
                                              column = 0,)
    
    efficiency =  Button(btns_frame, 
                   text = "Check Efficiency of the encryptor", 
                   fg = "black",
                   font=('Times new roman', 12, 'bold'),
                   width = 50,
                   height = 3, 
                   bd = 2, 
                   bg = "#fff", 
                   cursor = "hand2", 
                   command = lambda: Application().check_efficiency()).grid(row = 3, 
                                              column = 0,)
    
    destroy =  Button(btns_frame, 
                   text = "Exit", 
                   fg = "black",
                   font=('Times new roman', 12, 'bold'),
                   width = 50,
                   height = 3, 
                   bd = 2, 
                   bg = "#fff", 
                   cursor = "hand2", 
                   command = lambda: Application().destroy_session(Application().window)).grid(row = 4, 
                                              column = 0,)
    
    message =  Label(btns_frame, 
                  textvariable = labelText, 
                  fg = "Black",
                  font=('Times new roman', 12, 'bold'),
                  width = 55, 
                  height = 4, 
                  highlightbackground="black", 
                  highlightcolor="black", 
                  highlightthickness=1,
                  bd = 0, 
                  ).grid(row = 5, 
                                    column = 0,
                                    columnspan = 2,
                                    ipady = 11,
                                    )
     
    
    s = "Developed by : Saketh G"
    
    label2 =  Label(btns_frame2, 
                  text = s, 
                  fg = "Black", 
                  width = 55, 
                  height = 1, 
                  bd = 0, 
                  bg = "#cfa").grid(row = 6, 
                                    column = 0,
                                    columnspan = 2
                                    )
     
