import tkinter
import tkinter.messagebox
from tkinter import *

class my_gui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x900")
        self.str_frame = tkinter.Frame(self.main_window)
        self.int_frame = tkinter.Frame(self.main_window)
        self.dex_frame = tkinter.Frame(self.main_window)
        self.const_frame = tkinter.Frame(self.main_window)
        self.wis_frame = tkinter.Frame(self.main_window)
        self.char_frame = tkinter.Frame(self.main_window)
        self.races_frame = tkinter.Frame(self.main_window)

        self.str_label = tkinter.Label(self.main_window, text = 'Str = ')
        self.str_entry = tkinter.Entry(self.main_window, width = 10)

        self.int_label = tkinter.Label(self.main_window, text = 'Int = ')
        self.int_entry = tkinter.Entry(self.main_window, width = 10)

        self.dex_label = tkinter.Label(self.main_window, text = 'Dex = ')
        self.dex_entry = tkinter.Entry(self.main_window, width = 10)

        self.const_label = tkinter.Label(self.main_window, text = 'Const = ')
        self.const_entry = tkinter.Entry(self.main_window, width = 10)

        self.wis_label = tkinter.Label(self.main_window, text = 'Wis = ')
        self.wis_entry = tkinter.Entry(self.main_window, width = 10)

        self.char_label = tkinter.Label(self.main_window, text = 'Char = ')
        self.char_entry = tkinter.Entry(self.main_window, width = 10)

        self.races_box = Listbox(self.races_frame)
        self.races_box.insert(1, 'Human')
        self.races_box.insert(2, 'Elf')
        self.races_box.insert(3, 'Dragonborn')

        self.races_box.grid(row = 0, column = 2)

        self.str_label.grid(row = 0, column = 0)
        self.int_label.grid(row = 1, column = 0)
        self.dex_label.grid(row = 2, column = 0)
        self.const_label.grid(row = 3, column = 0)
        self.wis_label.grid(row = 4, column = 0)
        self.char_label.grid(row = 5, column = 0)

        self.str_entry.grid(row = 0, column = 1)
        self.int_entry.grid(row = 1, column = 1)
        self.dex_entry.grid(row = 2, column = 1)
        self.const_entry.grid(row = 3, column = 1)
        self.wis_entry.grid(row = 4, column = 1)
        self.char_entry.grid(row = 5, column = 1)

        #self.str_frame.pack()
        #self.int_frame.pack()
        #self.dex_frame.pack()
        #self.const_frame.pack()
        #self.wis_frame.pack()
        #self.char_frame.pack()
        self.main_window.grid()
        self.races_frame.grid(row = 0, column = 2)

        tkinter.mainloop()

chara = my_gui()
