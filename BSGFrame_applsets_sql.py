import pyodbc
from BSG_config import bsgconfig


class bsgframe_applsets_sql:

    @staticmethod
    def get_settings():
        conn = pyodbc.connect(bsgconfig.cockpit_connection)
        sql_query =  "SELECT "
        sql_query += "[id] = [application_setting_id], "
        sql_query += "[key] = [application_setting_key], "
        sql_query += "[value] = [application_setting_value] "
        sql_query += "FROM [cockpit].[application_setting]"
        
        cursor = conn.cursor()
        cursor.execute(sql_query)

        return cursor