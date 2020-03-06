import BSG_config as bsgcfg
import pyodbc 

def get_menu_configuration():
    CockpitConn = pyodbc.connect(bsgcfg.sql_cockpit_connection)
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
    "	[form_configuration_name]             = ISNULL(M.[form_configuration_name], '') " + 
    #"	,* " + 
    "FROM " + 
    "	CTE " + 
    "	JOIN [cockpit].[menu_configuration] AS M ON CTE.[menu_configuration_id] = M.[menu_configuration_id] " + 
    "ORDER BY  " + 
    "	CTE.[lvl] ASC, " + 
    "	M.[menu_configuration_id] ASC "
    )
    return cursor


def get_menu_information():
    print("hola")