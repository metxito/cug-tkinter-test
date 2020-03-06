import tkinter as tk
from tkinter import ttk
import pyodbc 

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


CockpitConn = pyodbc.connect('Driver={SQL Server};Server=metx;Database=Cockpit2020;UID=sa;PWD=bsgroup1_;')

appVersion = "2020.1.001"


window = tk.Tk()
window.geometry("1200x800")
window.title("BSGroup :: Cockpit Configuration : (v" + appVersion + ")")



TopFrame = tk.Frame(window, width=1200, height=100)
TopFrame.pack(side="top", fill="both")
label = tk.Label(TopFrame, text="BSGroup Data Analytics AG :: Cockpit configuration", font=("Arial Bold", 20))
label.pack(side="left")


TreeFrame = tk.Frame(window, width=1200, height=700 )
TreeFrame.pack(side="left", fill="both")
treeScroll = ttk.Scrollbar(TreeFrame)
treeScroll.pack(side="right", fill="y")
tree = ttk.Treeview(TreeFrame, selectmode='browse', columns=("VS", "FN", "RP", "RL"), yscrollcommand = treeScroll)
tree.pack(side="left", fill="both")





tree.column("#0",minwidth=120, width=300, stretch="no")
tree.column("FN",minwidth=120, width=300, stretch="no") 
tree.column("VS",minwidth=30, width=60, stretch="no")
tree.column("RP",minwidth=30, width=60, stretch="no")
tree.column("RL",minwidth=30, width=60, stretch="no")

tree.heading("#0", text="Side bar name")
tree.heading("FN", text="Form configuration name")   
tree.heading("VS", text="Visible")   
tree.heading("RP", text="Reset parameters")   
tree.heading("RL", text="Roles")   
 

cursor = CockpitConn.cursor()
cursor.execute("WITH cte AS ( " + 
"SELECT " +  
"	[menu_configuration_id], " +  
"	[menu_configuration_parent_id], " +  
"	[lvl] = 0 " +  
"FROM  " +  
"	[cockpit].[menu_configuration] " +  
"WHERE  " +  
"	[menu_configuration_id] > 0 AND [menu_configuration_parent_id] IS NULL " +  
"UNION ALL " +  
"SELECT  " +  
"	[menu_configuration].[menu_configuration_id], " +  
"	[menu_configuration].[menu_configuration_parent_id], " +  
"	[lvl] = cte.[lvl] + 1 " +  
"FROM  " +  
"	cte " +  
"	JOIN [cockpit].[menu_configuration] ON cte.[menu_configuration_id] = [menu_configuration].[menu_configuration_parent_id] " +  
") " + 
"SELECT  " + 
"	[menu_configuration_parent_id]        = ISNULL(FORMAT(M.[menu_configuration_parent_id], '0'), ''), " + 
"	[menu_configuration_id]               = ISNULL(FORMAT(M.[menu_configuration_id], '0'), ''), " + 
"	[menu_configuration_sidebar_name]     = ISNULL(FORMAT(M.[menu_configuration_id], '0'), '') + ': ' + M.[menu_configuration_sidebar_name], " + 
"	[menu_configuration_visible]          = IIF(M.[menu_configuration_visible] = 1, 'Visible', ''), " + 
"	[menu_configuration_reset_parameters] = IIF(M.[menu_configuration_reset_parameters] = 1, 'Yes', ''), " + 
"	[form_configuration_name]             = ISNULL(M.[form_configuration_name], ''), " + 
"	[menu_configuration_role]             = M.[menu_configuration_role] " + 
#"	,* " + 
"FROM " + 
"	CTE " + 
"	JOIN [cockpit].[menu_configuration] AS M ON CTE.[menu_configuration_id] = M.[menu_configuration_id] " + 
"ORDER BY  " + 
"	CTE.[lvl] ASC, " + 
"	M.[menu_configuration_id] ASC "
)
for row in cursor:
    try:
        tree.insert(row.menu_configuration_parent_id, row.menu_configuration_id, row.menu_configuration_id, text=row.menu_configuration_sidebar_name, values=(row.menu_configuration_visible, row.form_configuration_name, row.menu_configuration_reset_parameters, row.menu_configuration_role), open=True)
    except Exception as err:
        print(err)
    #    popupmsg("Not supported just yet!")


treeScroll.config(command=tree.yview)

window.mainloop()