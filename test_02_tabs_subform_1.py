import tkinter as tk
from tkinter import ttk

class tksubtab1: 
    
    def __init__(self, tktab):
        self.mainTab = tktab

    def make_gui(self):
        frame_top = tk.Frame(self.mainTab, width=300, height=500)
        frame_top.configure(bg='green')
        frame_top.pack(side="top", fill="both", padx=0, pady=0)
        tk.Label(frame_top, text="Hola lkjasdkljas aslkdja slkdj", font=("Arial Bold", 15)).pack(side="top")
