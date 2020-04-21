import pyodbc 

class bsgconfig:

    cockpit_connection = ""
    
    @classmethod
    def set_connection(cls, connection_string):
        cls.cockpit_connection = connection_string

    @classmethod
    def test_connection(cls):
        #try:
        conn = pyodbc.connect(cls.cockpit_connection)
        sql_query = "SELECT "
        sql_query += "[server] = @@SERVERNAME "
        sql_query += ",[catalog] = DB_NAME() "
        #sql_query += ",[version] = [application_setting_value] "
        #sql_query += "FROM [cockpit].[application_setting] "
        #sql_query += "WHERE [application_setting_key] = 'version' " 
        
        row = conn.execute(sql_query).fetchall()
        return row[0]
            
        #except:
        #    print("error connection")
            
            
#sql_cockpit_connection = 'Driver={SQL Server};Server=localhost;Database=Cockpit2020;UID=sa;PWD=bsgroup1_;'
#
#cockpite_roles = []
#CockpitConn = pyodbc.connect(sql_cockpit_connection)
#cursor = CockpitConn.cursor()
#cursor.execute("SELECT [role_id],[role_name] FROM [cockpit].[role_configuration]")
#for row in cursor:
#    cockpite_roles.append((row.role_id, row.role_name))
#
#del CockpitConn
#del cursor
#    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    