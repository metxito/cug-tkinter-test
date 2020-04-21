import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from BSGFrame_applsets_sql import bsgframe_applsets_sql

class bsgframe_applsets: 

    


    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent)

        ## Frame Buttons
        self.frame_buttons = tk.Frame(self.frame)
        self.frame_buttons.pack(side=tk.TOP, expand=0, padx=5, pady=5, ipadx=5, ipady=5, anchor=tk.NW)
        info_btn_apply = tk.Button (self.frame_buttons, text=" Refresh settings ", command = self.__refresh)
        info_btn_apply.pack(side=tk.LEFT, expand=0, padx=5, pady=5)
        info_btn_apply_3 = tk.Button (self.frame_buttons, text=" other ", command = self.__refresh)
        info_btn_apply_3.pack(side=tk.RIGHT, expand=0, padx=5, pady=5)


        ## Frame Treeview
        self.main_frame = tk.Frame(self.frame)
        self.main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1, padx=5, pady=5)

        columns = ("ID", "Key", "Value")
        self.treeview = ttk.Treeview(self.main_frame, height=18, show="headings", columns=columns) # 
        self.treeview.configure(selectmode=tk.BROWSE)
        self.treeview.column("ID", width=100, anchor=tk.W) # indicates column, not displayed
        self.treeview.column("Key", width=200, anchor=tk.W)
        self.treeview.column("Value", width=400, anchor=tk.W)

        self.treeview.heading("ID", text="ID", anchor=tk.W) # Show header
        self.treeview.heading("Key", text="Key", anchor=tk.W)
        self.treeview.heading("Value", text="Value", anchor=tk.W)
        
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH)
        self.treeview.bind('<Double-1>', self.set_cell_value)
        
        self.dobleblick = 1

    def set_cell_value(self, event):
        if self.dobleblick == 0:
            return
        item = self.treeview.identify('item', event.x, event.y)    
        if item:
            self.dobleblick = 0
            for ch in self.frame_buttons.winfo_children():
                ch.configure(state=tk.DISABLED)
            print(self.treeview.item(item))
            item_values = self.treeview.item(item, "values")
            column = self.treeview.identify_column(event.x)
            row = self.treeview.index(item) + 1
            c = int(str(column).replace('#',''))
            r = int(str(row).replace('I',''))

            cposx = 0
            cwidth = 0
            for i in range(c):
                xc =  self.treeview.column(i)
                if i < c-1:
                    cposx += xc["width"]
                else:
                    cwidth = xc["width"]

            cwidthtext = int(cwidth/7)
            self.treeview.configure(selectmode=tk.NONE)
            entryedit = tk.StringVar()
            entryedit.set(item_values[c-1])
            txtentryedit = tk.Entry(self.main_frame, text="", textvariable=entryedit, width=cwidthtext)
            txtentryedit.place(x=cposx, y=6+r*20)
            def saveedit():
                newvalue = entryedit.get()
                txtentryedit.destroy()
                ok_button.destroy()
                self.treeview.set(item, column=column, value=newvalue)
                self.treeview.configure(selectmode=tk.BROWSE)
                for ch in self.frame_buttons.winfo_children():
                    ch.configure(state=tk.NORMAL)
                self.dobleblick = 1
            ok_button = ttk.Button(self.main_frame, text='OK', width=4, command=saveedit)
            ok_button.place(x=cposx+cwidth-(4*7), y=2+r*20)
        else:
            pass

    def __refresh(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        settings = bsgframe_applsets_sql.get_settings()
        for row in settings:
            self.treeview.insert(
                        "", 
                        row.id, 
                        text=row.key, 
                        values=(
                            row.id,
                            row.key,
                            row.value
                        ),
                        open=True)