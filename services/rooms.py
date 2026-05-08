# ============================================================
# ROOMS SERVICE MODULE
# ============================================================
#
# PURPOSE:
# This module handles all operations related to:
# - Rooms
#
# DATABASE USED:
# MySQL (relational database)
#
# ARCHITECTURE ROLE:
# This file belongs to the SERVICE LAYER.
# It is responsible for retrieving and processing data
# from the database, not for user interaction or routing.
#
# RESPONSIBILITIES:
# - Execute SQL queries on rooms table
# - Fetch room data
# - Display formatted results to the user
# ============================================================


# Import reusable MySQL connection function
from mysql_connection import connection


# ============================================================
# FUNCTION: view_rooms
# ============================================================
#
# PURPOSE:
# Retrieves and displays all room records from the database.
#
# DATABASE OPERATION:
# Executes a simple SELECT query on the rooms table.
#
# ============================================================

def view_rooms():

    # Create a connection to the MySQL database
    # This uses the shared connection function from mysql_connection.py
    conn = connection()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # ========================================================
    # SQL QUERY EXPLANATION
    # ========================================================
    # This query retrieves all columns (*) from the rooms table.
    # It assumes the table contains information such as:
    # - room id
    # - room name or number
    # - capacity
    # - location (if applicable)
    # ========================================================

    query = "SELECT * FROM rooms"

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all rows returned by the database
    results = cursor.fetchall()

    # Print header for clarity in console output
    print("\n====================")
    print("      ROOMS         ")
    print("====================")

    # Loop through each room record
    for row in results:

        # Each row represents a room record from the database
        # The structure depends on your table schema
        print("Room Record:", row)

    # Close database connection to release resources
    conn.close()