import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BSGTable:


    def refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        data = self.populate_function()
        self.original_data = []
        i = 1
        for row in data:
            record = {}
            record['id'] = i 
            for c in self.table_definion['columns']:
                record['values'][c['name']] = row[c['name']]
            i += 1

        for row in data:
            self.table.insert("", row['id'], text=row['id'], values=row['values'], open=True)



    def edit_text (self, id, column, value, pos, size, textsize, regex):
        def stop_edit():
            txtentryedit.destroy()
            self.table.configure(selectmode=tk.BROWSE)
            self.dobleblick = 1
        def save_edit():
            newvalue = entryedit.get()
            if regex:
                regextest = re.compile(regex, re.I)
                match = regextest.match(str(newvalue))
                if bool(match) != True:
                    messagebox.showerror("Wrong entry", ("The new value is not valid. It should match with the regular expression: " + regex))
                    return
            self.populate_function(id, column, newvalue)
            stop_edit()
            self.refresh()
        def Key(event):
            if event.char == '\x1b':
                stop_edit()
            if event.char == '\r':
                save_edit()

        entryedit = tk.StringVar()
        entryedit.set(value)
        txtentryedit = tk.Entry(self.parent, text="", textvariable=entryedit, width=textsize)
        txtentryedit.place(x=pos['x'], y=pos['y'])
        txtentryedit.bind("<Key>", Key)

    def edit_integer (self, id, column, value, pos, size, textsize):
        def stop_edit():
            txtentryedit.destroy()
            self.table.configure(selectmode=tk.BROWSE)
            self.dobleblick = 1
        def save_edit():
            newvalue = entryedit.get()
            regextest = re.compile('^[0-9]*$', re.I)
            match = regextest.match(str(newvalue))
            if bool(match) != True:
                messagebox.showerror("Wrong entry", "The new value is not valid integer")
                return
            self.populate_function(id, column, newvalue)
            stop_edit()
            self.refresh()
        def Key(event):
            if event.char == '\x1b':
                stop_edit()
            if event.char == '\r':
                save_edit()

        entryedit = tk.StringVar()
        entryedit.set(value)
        txtentryedit = tk.Entry(self.parent, text="", textvariable=entryedit, width=textsize)
        txtentryedit.place(x=pos['x'], y=pos['y'])
        txtentryedit.bind("<Key>", Key)


    def edit_dropdown (self, id, column, value, pos, size, textsize, values):
        #def stop_edit():
        #    txtentryedit.destroy()
        #    self.table.configure(selectmode=tk.BROWSE)
        #    self.dobleblick = 1
        #def save_edit():
        #    newvalue = entryedit.get()
        #    self.populate_function(id, column, newvalue)
        #    stop_edit()
        #    self.refresh()
        #def Key(event):
        #    if event.char == '\x1b':
        #        stop_edit()
        #    if event.char == '\r':
        #        save_edit()

        entryedit = tk.StringVar()
        entryedit.set(value)
        txtentryedit = tk.Entry(self.parent, text="", textvariable=entryedit, width=textsize)
        txtentryedit.place(x=pos['x'], y=pos['y'])
        txtentryedit.bind("<Key>", Key)

    def doble_click(self, event):
        if self.dobleblick == 0:
            return
        item = self.table.identify('item', event.x, event.y)   
        if not item:
            return

        c = int(str(self.table.identify_column(event.x)).replace('#',''))-1
        column = self.table_definion['columns'][c]
        if column is None:
            return

        if not ("edit" in column):
            return

        self.dobleblick = 0
        self.table.configure(selectmode=tk.NONE)
        row = self.table.index(item) + 1
        r = int(str(row).replace('I',''))


        cposx = 0
        cwidth = 0
        for i in range(c+1):
            xc =  self.table.column(i)
            if i < c:
                cposx += xc["width"]
            else:
                cwidth = xc["width"]

        pos = {}
        pos['x'] = cposx
        pos['y'] = (r*20)+5
        size = {}
        size['x'] = cwidth
        size['y'] = 20
        textsize = int(cwidth/6)
        item = self.table.item(item)
        value = item['values'][c]
        id = item['text']
        regex = ""
        if "regex" in column:
            regex = column['regex']


        if column['edit'] == "text":
            self.edit_text (id, column['name'], value, pos, size, textsize, regex)
        elif column['edit'] == "integer":
                self.edit_integer (id, column['name'], value, pos, size, textsize)



        
            

    def __init__ (self, parent_frame, table_definition, populate_function, update_function, delete_function):
        self.table_definion = table_definition
        self.parent = parent_frame
        self.populate_function = populate_function
        self.populate_function = update_function
        self.populate_function = delete_function

        
        self.columns = []
        for c in table_definition['columns']:
            self.columns.append(c['name'])

        self.table = ttk.Treeview(self.parent, show="headings", columns=self.columns) # 
        self.table.configure(selectmode=tk.BROWSE)
        for c in table_definition['columns']:
            self.table.column(c['name'], width=c['width'], anchor=tk.W)
            self.table.heading(c['name'], text=c['head'], anchor=tk.W)

        self.table.pack(side=tk.LEFT, fill=tk.BOTH)
        self.table.bind('<Double-1>', self.doble_click)

        self.dobleblick = 1
        self.refresh()