# Import the mysql connector library
# This library allows Python to communicate with MySQL
import mysql.connector


def connection():
    connection_details= 'connection string placeholder'



# Creates and returns a MySQL database connection object.
# This function is called by service modules whenever they need to interact with the database.

# Create a connection to the MySQL database
# Replace the values below with your own MySQL details
    connection_details = mysql.connector.connect(host= 'localhost', user='root', password='password', database='appdbproj')

    # Check if the connection was successful
    if connection_details.is_connected:

        print("Successful connection to MySQL database")

        return connection_details

    else:
        print("Connection Failed")

#  # ============================================================
# PYTHON ENTRY POINT CHECK
# ============================================================
#
# Every Python file has a built-in variable called __name__
#
# Python uses this variable to determine HOW the file is being used:
#
# ------------------------------------------------------------
# CASE 1: File is run directly
# Example:
#     python mysql_connection.py
#
# In this case Python sets:
#     __name__ = "__main__"
#
# Meaning:
#     "This file is the main program being executed"
#
# ------------------------------------------------------------
# CASE 2: File is imported into another file
# Example:
#     from mysql_connection import connection
#
# In this case Python sets:
#     __name__ = "mysql_connection"
#
# Meaning:
#     "This file is being used as a module (toolbox), not run directly"
#
# ============================================================




    # This block ONLY runs if this file is executed directly
    # (NOT when it is imported into another file)

    # We call the connection() function here to TEST it.
    # This is useful for debugging and verifying that:
    # - MySQL connection works
    # - credentials are correct
    # - database is reachable

  
if __name__ == "__main__":

    connection()

        
    
    





