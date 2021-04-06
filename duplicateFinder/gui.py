#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 00:10:24 2021

@author: lukashentschel
"""
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory

class GUI(object):

    
    
    def __init__(self, master, **kwargs):
        self._initVariables(**kwargs)
        self._initWindow(master)
        pass
    
    def _initWindow(self, master, width=600, height=500):
        
        master['bg'] = self.__colorDict['bg']
        canvas = tk.Canvas(master, width=width, height=height,
                            bg=self.__colorDict['bg'], bd=0)
        canvas.grid(rowspan=3, columnspan=3)
        
        #logo?
        logo = Image.open('logo.png')
        logo = ImageTk.PhotoImage(logo)
        logoLabel = tk.Label(image=logo)
        logoLabel.image = logo
        logoLabel.grid(column=1, row=0)
        
        #instructions
        instructions = tk.Label(master, text='Select a directoy,\nto start '\
                                'searching for duplicates!', font=('Raleway', 20),
                                bg=self.__colorDict['bg'], 
                                fg=self.__colorDict['fg'], 
                                highlightcolor=self.__colorDict['bg'] ,bd=0)
        instructions.grid(columnspan=3, column=0, row=1)
        
        #button
        self.__buttonText = tk.StringVar()
        self.__button = tk.Button(master, textvariable=self.__buttonText,
                                  font='Raleway', bg='darkgreen', fg='silver', 
                                  height=2, width=15, bd=0, 
                                  command=lambda : self._button(master))
        self.__buttonText.set('Directory')
        self.__button.grid(column=1, row=2)
        
    
    def _initVariables(self, **kwargs):
        self.__colorDict={
            'bg' : 'midnightblue',
            'fg' : 'darkmagenta'}
        pass
    
    def _button(self, master):
        #print("Yes Works fine!")
        self.__buttonText.set("loading...")
        path = askdirectory(parent=master, 
                            title='Choose a directory to start searching!')
        
        #Give path to app and search for duplicates
        print(path)
        
        #print the resulting duplicates an there path in text file 
        
        #aks for saving the file
        
        #Think about further operations?
        pass
    
    def _result(self, master, content):
        
        canvas = tk.Canvas(master, width=600, height=300, 
                            bg=self.__colorDict['bg'])
        canvas.grid(rowspan=3, columnspan=3)
        self.__textField = tk.Text(master, heigth=10, widht=50)
        self.__textField.instert(1.0, content)
        self.__textField.grid(column=1, row=1)
        
        
        pass
    
if __name__=='__main__':
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
    pass