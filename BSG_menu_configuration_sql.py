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



def get_menu_information(menu_configuration_id):
    CockpitConn = pyodbc.connect(bsgcfg.sql_cockpit_connection)
    cursor = CockpitConn.cursor()
    query = ("SELECT " +
        "     [menu_configuration_id] " +
        "    ,[menu_configuration_parent_id] " +
        "    ,[form_configuration_name] " +
        "    ,[menu_configuration_sidebar_name] " +
        "    ,[menu_configuration_description_big] " +
        "    ,[menu_configuration_description_small] " +
        "    ,[menu_configuration_font_awesome_icon] " +
        "    ,[menu_configuration_reset_parameters] " +
        "    ,[menu_configuration_visible] " +
        "    ,[configurator_relevant] " +
        "    ,[menu_configuration_role] " +
        "    ,[menu_configuration_menu_id_parent] " +
        "    ,[modified_by] " +
        "    ,[modified_on] " +
        "FROM [cockpit].[menu_configuration] ")
    print (query) 
    cursor.execute(query)
    return cursor