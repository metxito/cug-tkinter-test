import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import BSG_config as bsgcfg
import BSG_menu_configuration_sql as bsgsql


class BSG_menu_configuration: 
    #self._img = PhotoImage(file="resources\information_picto.gif")

    def __init__(self, version):
        self.MainVersion = version
        self.current_menu_id = None
        self.status = ""


    def __message(self, event):
        self.current_menu_id = self.tree.selection()


    def __apply_changes(self):
        var = tk.messagebox.askquestion(title="Holi", message="__apply_changes", parent=self.window)
        print (var)


    def __form_configuration(self):
        var = tk.messagebox.askokcancel(title="Holi", message="Do you want to continue?", parent=self.window)
        print (var)


    def __refresh_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.current_menu_id = None
        try:
            cursor = bsgsql.get_menu_configuration()
            for row in cursor:
                try:
                    self.tree.insert(
                        row.menu_configuration_parent_id, 
                        row.menu_configuration_id, 
                        row.menu_configuration_id, 
                        text=row.menu_configuration_sidebar_name, 
                        values=(
                            row.menu_configuration_visible, 
                            row.form_configuration_name, 
                            row.menu_configuration_reset_parameters
                        ),
                        open=True)
                except Exception as err:
                    print(err)
        except:
            print ("Error SQL")
           
        self.scroll_tree.config(command=self.tree.yview)


    def __info_reset(self):
        self.info_txt_id.set("")
        self.info_txt_parent_id.set("")
        self.info_txt_name.set("")
        self.info_txt_sidename.set("")
        self.info_txt_desc.set("")
        self.info_txt_desc2.set("")
        self.info_txt_awesome.set("")
        self.info_reset.set(1)
        self.info_visible.set(1)
        for w in self.info_roles:
            w.set(0)


    def __show_menu(self, event):
        if self.current_menu_id != None and self.current_menu_id != "" and self.current_menu_id != "new":
            sub_menu = tk.Menu(self.window, tearoff=0)
            if self.tree.parent(self.current_menu_id) == "" or self.status == "":
                sub_menu.add_command(label="Add sub element", command=self.__menu_add_sub_element)
            else:
                sub_menu.add_command(label="Add sub element", command=self.__menu_add_sub_element, state=tk.DISABLED)
            if self.status == "":
                sub_menu.add_command(label="Delete element", command=self.__menu_delete)
                sub_menu.add_command(label="Edit element", command=self.__menu_edit)
            else: 
                sub_menu.add_command(label="Delete element", command=self.__menu_delete, state=tk.DISABLED)
                sub_menu.add_command(label="Edit element", command=self.__menu_edit, state=tk.DISABLED)
            
            try:
                sub_menu.tk_popup(event.x_root, event.y_root, 0)
            finally:
                sub_menu.grab_release()


    def __change_status(self, element, newstate):
        try:
            if (element.winfo_class() != "Frame"):
                element.configure(state=newstate)
            else:
                for child in element.winfo_children():
                    self.__change_status(child, newstate)
        except:
            print(element.winfo_class())


    def __menu_edit(self):
        self.status = "edit"
        self.__info_reset()
        self.__change_status(self.frame_info, tk.NORMAL)
        element_into = bsgsql.get_menu_information(self.current_menu_id)
        self.info_txt_id = element_into.menu_configuration_id
        self.info_txt_parent_id = element_into.menu_configuration_parent_id
        self.info_txt_name = element_intro.form_configuration_name

    def __menu_add_sub_element(self):
        self.status = "newfromparent"
        self.__info_reset()
        self.__change_status(self.frame_info, tk.NORMAL)
        self.info_txt_parent_id.set(self.current_menu_id)
        

    def __menu_delete(self):
        tk.messagebox.showwarning(title="Warning :: TODO", Message="in the TODO list", parent=self.window)


    def Start(self):
        self.window = tk.Tk()
        self.window.geometry("1200x800")
        self.window.title("BSGroup :: Cockpit Configuration : (v" + self.MainVersion + ")")


        
        

        frame_top = tk.Frame(self.window, width=1200, height=100)
        frame_top.pack(side="top", fill="both", padx=10, pady=10)
        tk.Label(frame_top, text="BSG Cockpit 2020 :: Menu configuration", font=("Arial Bold", 15)).pack(side="top")
        tk.Label(frame_top, text=" ").pack(side="top")
        tk.Button (frame_top, text=" Refresh Menu Configuration ", command = self.__refresh_tree).pack(side="left")
        tk.Label(frame_top, text="   ").pack(side="left")
        tk.Button (frame_top, text=" Add new menu ", command = self.__refresh_tree).pack(side="left")

        frame_tree = tk.Frame(self.window, width=800)
        frame_tree.pack(side="left", fill="both", padx=10, pady=10)
        frame_info = tk.Frame(self.window, width=400)
        frame_info.pack()
        tk.Label(frame_info, text="Menu configuration :").grid(row=0, column=0, columnspan=3, sticky="W")
        tk.Label(frame_info, text=" ").grid(row=1, column=0, columnspan=3, sticky="W")
        

        self.info_txt_id = tk.StringVar()
        tk.Label(frame_info, text="ID ").grid(row=2, column=0, sticky="W")
        tk.Entry(frame_info, text="", textvariable=self.info_txt_id, width=10).grid(row=2, column=1, sticky="W")
        tk.Label(frame_info, text=".").grid(row=2, column=2, sticky="E")
        tk.Label(frame_info, text=".").grid(row=2, column=3, sticky="E")


        self.info_txt_parent_id = tk.StringVar()
        tk.Label(frame_info, text="Parent ID ").grid(row=3, column=0, sticky="W")
        tk.Entry(frame_info, text="", textvariable=self.info_txt_parent_id, width=10).grid(row=3, column=1, sticky="W")


        self.info_txt_name = tk.StringVar()
        tk.Label(frame_info, text="Form ").grid(row=4, column=0, sticky="W")
        tk.Entry(frame_info, text="", textvariable=self.info_txt_name, width=40).grid(row=4, column=1, columnspan=3, sticky="W")


        self.info_txt_sidename = tk.StringVar()
        tk.Label(frame_info, text="Sidebar name ").grid(row=5, column=0, sticky="W")
        tk.Entry(frame_info, text="", textvariable=self.info_txt_sidename, width=40).grid(row=5, column=1, columnspan=3, sticky="W")

        
        self.info_txt_desc = tk.StringVar()
        tk.Label(frame_info, text="Description ").grid(row=6, column=0, sticky="W")
        tk.Entry(frame_info, text="", textvariable=self.info_txt_desc, width=40).grid(row=6, column=1, columnspan=3, sticky="W")


        self.info_txt_desc2 = tk.StringVar()
        tk.Label(frame_info, text="Small description ").grid(row=7, column=0, sticky="W")
        tk.Entry(frame_info, text="", textvariable=self.info_txt_desc2, width=40).grid(row=7, column=1, columnspan=3, sticky="W")


        self.info_txt_awesome = tk.StringVar()
        tk.Label(frame_info, text="Awesome icon ").grid(row=8, column=0, sticky="W")
        tk.Entry(frame_info, text="", textvariable=self.info_txt_awesome, width=30).grid(row=8, column=1, columnspan=2, sticky="W")


        tk.Label(frame_info, text="Reset Parameters ").grid(row=9, column=0, sticky="W")
        self.info_reset = tk.IntVar(value=1)
        ttk.Radiobutton(frame_info, text="Yes", variable=self.info_reset, value=1).grid(row=9, column=1, sticky="W")
        ttk.Radiobutton(frame_info, text="No",  variable=self.info_reset, value=0).grid(row=9, column=2, sticky="W")


        tk.Label(frame_info, text="Visible ").grid(row=10, column=0, sticky="W")
        self.info_visible = tk.IntVar(value=1)
        ttk.Radiobutton(frame_info, text="Visible", variable=self.info_visible, value=1).grid(row=10, column=1, sticky="W")
        ttk.Radiobutton(frame_info, text="Hide",    variable=self.info_visible, value=0).grid(row=10, column=2, sticky="W")


        tk.Label(frame_info, text="Roles ").grid(row=11, column=0, sticky="w")
        frame_roles = tk.Frame(frame_info)
        frame_roles.grid(row=11, column=1, sticky="W")
        self.info_roles = []
        for r in bsgcfg.cockpite_roles:
            currentVar = tk.IntVar()
            self.info_roles.append(currentVar)
            tk.Checkbutton(frame_roles, text=r[1], variable=currentVar, onvalue=r[0]).pack(side="top", anchor="w")


        tk.Label(frame_info, text=" ").grid(row=12, column=0, sticky="W")
        tk.Label(frame_info, text=" ").grid(row=13, column=0, sticky="W")
        self.info_btn_apply = tk.Button (frame_info, text=" Update Configuration ", command = self.__apply_changes)
        self.info_btn_apply.grid(row=14, column=1, columnspan=4, sticky="W")


        tk.Label(frame_info, text=" ").grid(row=15, column=0, sticky="W")
        self.info_btn_form = tk.Button (frame_info, text=" Form Configuration ", command = self.__form_configuration)
        self.info_btn_form.grid(row=16, column=1, columnspan=4, sticky="W")
        

        self.frame_info = frame_info
        self.__change_status(self.frame_info, tk.DISABLED)

        self.__info_reset()


        self.scroll_tree = ttk.Scrollbar(frame_tree)
        self.scroll_tree.pack(side="right", fill="y")
        self.tree = ttk.Treeview(frame_tree, selectmode='browse', columns=("VS", "FN", "RP"), yscrollcommand = self.scroll_tree)
        self.tree.pack(side="left", fill="both")
        self.tree.column("#0",minwidth=120, width=300, stretch="no")
        self.tree.column("FN",minwidth=120, width=350, stretch="no") 
        self.tree.column("VS",minwidth=30, width=60, stretch="no")
        self.tree.column("RP",minwidth=30, width=60, stretch="no")
        self.tree.heading("#0", text="Side bar name")
        self.tree.heading("FN", text="Form configuration name")   
        self.tree.heading("VS", text="Visible")   
        self.tree.heading("RP", text="Reset parameters")   

        self.tree.bind('<<TreeviewSelect>>', self.__message)
        self.tree.bind("<Button-3>", self.__show_menu)

        #self.s = ttk.Style()
        #self.s.theme_use('classic')

        self.window.mainloop()
        
