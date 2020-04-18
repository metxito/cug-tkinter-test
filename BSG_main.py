import tkinter as tk
from tkinter import ttk
from BSG_tab_connect import bsg_form_connect

window = tk.Tk()
window.geometry("1200x800")
window.title("BSGroup :: Cockpit Configuration : ")

        
tab_parent = ttk.Notebook(window)
tab_connect = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab_connect, text="Connect")
tab_parent.add(tab2, text="Application config")
tab_parent.pack(expand=1, fill='both')

form_connect = bsg_form_connect(tab_connect)
form_connect.make_gui()




window.mainloop()
