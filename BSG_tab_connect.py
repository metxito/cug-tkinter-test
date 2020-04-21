import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from BSG_config import bsgconfig

class bsg_form_connect: 
    
    def __init__(self, tktab):
        self.mainTab = tktab
        self.main_frame = tk.Frame(self.mainTab)
        self.main_frame.pack(side=tk.TOP, expand=0, padx=3, pady=100)


        self.connection_string = tk.StringVar()


        tk.Label(self.main_frame, text="Connection String ").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(self.main_frame, text="", textvariable=self.connection_string, width=100).grid(row=1, column=1, columnspan=3, sticky=tk.W)
        self.connection_string.set("Driver={SQL Server};Server=localhost;Database=Cockpit2020;UID=sa;PWD=bsgroup1_;")
        
        tk.Label(self.main_frame, text=" ").grid(row=2, column=0, columnspan=1, sticky=tk.W)
        self.info_btn_apply = tk.Button (self.main_frame, text=" Connect to Cockpit ", command = self.__connect)
        self.info_btn_apply.grid(row=3, column=1, columnspan=1, sticky=tk.W)

        tk.Label(self.main_frame, text=" ").grid(row=4, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self.main_frame, text=" ").grid(row=5, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self.main_frame, text=" ").grid(row=6, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self.main_frame, text="Server:").grid(row=7, column=0, columnspan=1, sticky=tk.W)
        self.lbl_server = tk.Label(self.main_frame, text="")
        self.lbl_server.grid(row=7, column=1, columnspan=1, sticky=tk.W)

        tk.Label(self.main_frame, text="Catalog:").grid(row=8, column=0, columnspan=1, sticky=tk.W)
        self.lbl_catalog = tk.Label(self.main_frame, text="")
        self.lbl_catalog.grid(row=8, column=1, columnspan=1, sticky=tk.W)

        tk.Label(self.main_frame, text="Server:").grid(row=9, column=0, columnspan=1, sticky=tk.W)
        self.lbl_version = tk.Label(self.main_frame, text="")
        self.lbl_version.grid(row=9, column=1, columnspan=1, sticky=tk.W)



    def __connect(self):
        
        bsgconfig.set_connection(self.connection_string.get())
        row = bsgconfig.test_connection()

        self.lbl_server.configure(text=row.server)
        self.lbl_catalog.configure(text=row.catalog)
        self.lbl_version.configure(text=row.version)
