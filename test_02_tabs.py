import tkinter as tk
from tkinter import ttk
from test_02_tabs_subform_1 import tksubtab1

window = tk.Tk()
window.geometry("1200x800")
window.title("BSGroup :: Cockpit Configuration : ")

      
        
tab_parent = ttk.Notebook(window)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="All Records")
tab_parent.add(tab2, text="Add New Record")
tab_parent.pack(expand=1, fill='both')


subtab1 = tksubtab1(tab1)
subtab1.make_gui()


frame_top2 = tk.Frame(tab2, width=300, height=500)
frame_top2.configure(bg='blue')
frame_top2.pack(side="top", fill="both", padx=0, pady=0)
tk.Label(frame_top2, text="Hola world", font=("Arial Bold", 15)).pack(side="top")


window.mainloop()
