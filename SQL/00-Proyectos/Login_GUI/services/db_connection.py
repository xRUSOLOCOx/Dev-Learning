import mysql.connector
from mysql.connector import Error

class DB_CONTROL:

    def database_connection():

        try:

            connection = mysql.connector.connect(
                
                user = "uapjadkmtfntek6k",
                password = "h4xkkRzsXOaX93uWEKql",
                database = "bwrpugboeefnvijbj8un",
                host = "bwrpugboeefnvijbj8un-mysql.services.clever-cloud.com"

                )
            
            return connection
        
        except Error as main_error:

            return f"Error: {main_error}"
    
    connection = database_connection()
    db_cursor = connection.cursor()

    