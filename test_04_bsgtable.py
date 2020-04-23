import pyodbc
import tkinter as tk
from tkinter import ttk
from BSG_table import BSGTable


window = tk.Tk()
window.geometry("1200x800")
window.title("BSGroup :: Cockpit Configuration : ")

      
        

frame = ttk.Frame(window)
frame.pack(side=tk.TOP, fill=tk.BOTH, padx=0, pady=0)

def populate_function():
    conn = pyodbc.connect("Driver={SQL Server};Server=localhost;Database=Cockpit2020;UID=sa;PWD=bsgroup1_;")
    sql_query = "SELECT [id] = [application_setting_id], [key] = [application_setting_key], [valuetext] = [application_setting_valuetext], [valueint] = [application_setting_valueint], [valuedropdown] = [application_setting_valuedropdown], [valuedate] = [application_setting_valuedate] FROM [dbo].[test]"
    cursor = conn.cursor()
    data = []
    cursor.execute(sql_query)
    for r in cursor:
        row = dict()
        row['id'] = r.id
        row['values'] = (   
            r.id
            ,r.key
            ,r.valuetext
            ,r.valueint
        )
        data.append(row)
    conn.close()
    return data

def update_function(id, columnname, newValue):
    print ("update: " + str(id) + " on [" + columnname + "] with: " + str(newValue))

def delete_function(id):
    print ("delete: " + str(id))

table_definition = {
    "columns": [
        {
            "head": "ID",
            "name": "id",
            "width": 100
        }
        ,{
            "head": "Key",
            "name": "key",
            "width": 100,
        }
        ,{
            "head": "Value Text",
            "name": "valuetext",
            "width": 300,
            "edit": "text",
            "regex": "^[a-z]{5} [0-9]$"
        }
        ,{
            "head": "Value Integer",
            "name": "valueint",
            "width": 300,
            "edit": "integer"
        }
        #,{
        #    "head": "Value Dropdown",
        #    "name": "valuedropdown",
        #    "width": 300,
        #    "edit": "dropdown",
        #    "values": [
        #        { "id": 1, "value": "text 21"},
        #        { "id": 2, "value": "text 32"},
        #        { "id": 3, "value": "text 33"},
        #        { "id": 4, "value": "text 94"},
        #        { "id": 5, "value": "text 95"},
        #        { "id": 6, "value": "text 86"}
        #    ]
        #}   
    ],
    
}

table = BSGTable(frame, table_definition, populate_function, update_function, delete_function)

window.mainloop()