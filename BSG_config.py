import pyodbc 


sql_cockpit_connection = 'Driver={SQL Server};Server=metx;Database=Cockpit2020;UID=sa;PWD=bsgroup1_;'

cockpite_roles = []
CockpitConn = pyodbc.connect(sql_cockpit_connection)
cursor = CockpitConn.cursor()
cursor.execute("SELECT [role_id],[role_name] FROM [cockpit].[role_configuration]")
for row in cursor:
    cockpite_roles.append((row.role_id, row.role_name))

del CockpitConn
del cursor
    