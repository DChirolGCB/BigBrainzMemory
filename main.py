'''
Filename: f:\ProjetsPython\_2022\BB_Memory\main.py
Path: f:\ProjetsPython\_2022\BB_Memory
Created Date: Saturday, January 1st 2022, 10:39:34 pm
Author: David Chirol

Copyright (c) 2022 Your Company
'''
import tkinter as tk
import random
from tkinter import *
 
button_list = ['dummy']
class button_box :
    def __init__ (self, button, ID_number) :
        self.ID_number = ID_number
        self.button = button
 
    def clicked (self, event) :
        print (f'You pressed button number {self.ID_number}')
root = Tk ()
 
button_number = 1
for y in range (8) :
    for x in range (8) :
        color = random.choice(['white', 'green'])
        print(color)
        button = Button (width = 10, height = 5, text = button_number, background = color)
        button.config (relief = 'solid', borderwidth = 1)
        button.grid (row = y, column = x)
        button_list.append (button_box (button, button_number))
        button.bind ('<Button-1>', lambda e: button.config(bg='red'), button_list[button_number].clicked)
        button_number += 1

mainloop ()