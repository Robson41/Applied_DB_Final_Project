# ============================================================
# SPEAKERS SERVICE MODULE
# ============================================================
#
# PURPOSE:
# This module handles all operations related to:
# - Speakers
# - Sessions
#
# DATABASE USED:
# MySQL (relational database)
#
# ARCHITECTURE ROLE:
# This is part of the SERVICE LAYER.
# It sits between main.py (controller) and the database layer.
#
# RESPONSIBILITY:
# - Execute SQL queries
# - Process database results
# - Return/display formatted output
# ============================================================


# Import reusable database connection function

from mysql_connection import connection

# ============================================================
# FUNCTION: view_speakers_sessions
# ============================================================
#
# PURPOSE:
# Retrieves and displays all speakers and their associated sessions.
#
# DATABASE OPERATION:
# Uses a SQL JOIN between:
# - speakers table
# - sessions table
#
# RELATIONSHIP:
# speakers.id = sessions.speaker_id
#
# ============================================================

def view_speakers_sessions():
    # Create a connection to the MySQL database
    # This uses the reusable function from mysql_connection.py
    conn = connection()

    # Create a cursor object
    # The cursor is used to execute SQL queries

    cursor = conn.cursor()
       # ========================================================
    # SQL QUERY EXPLANATION
    # ========================================================
    # We are joining two tables:
    #
    # speakers:
    #   - contains speaker information (name, id)
    #
    # sessions:
    #   - contains session details (title, time, speaker_id)
    #
    # JOIN condition ensures we match each session
    # with its correct speaker.
    # ========================================================
    query = """
    SELECT speakers.name, sessions.title, sessions.time
    FROM speakers
    JOIN sessions ON speakers.id = sessions.speaker_id
    """

    # Execute the SQL query on the database
    cursor.execute(query)

    # Fetch all rows returned by the query
    results = cursor.fetchall()

    # Fetch all rows returned by the query
    print('============================================')
    print('Speakers & Session Data')
    print('============================================')

    # Loop through each record returned from database
    for row in results:
        print("Speaker Name :", row[0])
        print("Session Title:", row[1])
        print("Session Time :", row[2])
        print("------------------------------")
    
    conn.close()

    
