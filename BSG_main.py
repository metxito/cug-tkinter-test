import tkinter as tk
from tkinter import ttk
from BSG_config import bsgconfig
from BSGFrame_applsets import bsgframe_applsets


class BSGMain:

    def Start(self):

        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("BSGroup :: Cockpit Configuration : ")


        ## Notebook        
        self.tabnotebook = ttk.Notebook(self.window)

        ## Notebook tabs
        self.tab_connect = ttk.Frame(self.tabnotebook)
        self.tabnotebook.add(self.tab_connect, text="Connect")

        self.frame_appl_settings = bsgframe_applsets(self.tabnotebook)
        self.tabnotebook.add(self.frame_appl_settings.frame, text="Application config")
        self.tabnotebook.tab(1, state=tk.DISABLED)

        self.tabnotebook.pack(expand=1, fill='both', padx=10, pady=10)

        ## Set frames into tabs






        ## TAB connect

        self.frame_connect = tk.Frame(self.tab_connect)
        self.frame_connect.pack(side=tk.TOP, expand=0, padx=50, pady=50, anchor=tk.NW)

        self.connection_string = tk.StringVar()
        tk.Label(self.frame_connect, text="Connection String ").grid(row=1, column=0, sticky=tk.W)
        self.txt_connection_string = tk.Entry(self.frame_connect, text="", textvariable=self.connection_string, width=100)
        self.txt_connection_string.grid(row=1, column=1, columnspan=3, sticky=tk.W)
        self.connection_string.set("Driver={SQL Server};Server=localhost;Database=Cockpit2020;UID=sa;PWD=bsgroup1_;")

        tk.Label(self.frame_connect, text=" ").grid(row=2, column=0, columnspan=1, sticky=tk.W)
        self.info_btn_apply = tk.Button (self.frame_connect, text=" Connect to Cockpit ", command = self.__connect)
        self.info_btn_apply.grid(row=3, column=1, columnspan=1, sticky=tk.W)

        tk.Label(self.frame_connect, text=" ").grid(row=4, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self.frame_connect, text=" ").grid(row=5, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self.frame_connect, text=" ").grid(row=6, column=0, columnspan=1, sticky=tk.W)
        tk.Label(self.frame_connect, text="Server:").grid(row=7, column=0, columnspan=1, sticky=tk.W)
        self.lbl_server = tk.Label(self.frame_connect, text="")
        self.lbl_server.grid(row=7, column=1, columnspan=1, sticky=tk.W)

        tk.Label(self.frame_connect, text="Catalog:").grid(row=8, column=0, columnspan=1, sticky=tk.W)
        self.lbl_catalog = tk.Label(self.frame_connect, text="")
        self.lbl_catalog.grid(row=8, column=1, columnspan=1, sticky=tk.W)

        tk.Label(self.frame_connect, text="Server:").grid(row=9, column=0, columnspan=1, sticky=tk.W)
        self.lbl_version = tk.Label(self.frame_connect, text="")
        self.lbl_version.grid(row=9, column=1, columnspan=1, sticky=tk.W)

        self.window.mainloop()


    def __connect(self):
        bsgconfig.set_connection(self.connection_string.get())
        row = bsgconfig.test_connection()
        self.lbl_server.configure(text=row.server)
        self.lbl_catalog.configure(text=row.catalog)
        #self.lbl_version.configure(text=row.version)
        self.txt_connection_string.configure(state=tk.DISABLED)
        self.info_btn_apply.configure(state=tk.DISABLED)
        self.tabnotebook.tab(1, state=tk.NORMAL)





