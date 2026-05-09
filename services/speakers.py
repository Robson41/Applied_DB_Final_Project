# ============================================================
# SPEAKERS SERVICE MODULE (FIXED VERSION)
# ============================================================
#
# PURPOSE:
# This module handles retrieval of speaker and session data
# from the MySQL database.
#
# DATABASE DESIGN NOTE:
# There is NO separate "speakers" table in this system.
# Instead, speaker information is stored directly in the
# "session" table under the column:
#   - speakerName
#
# ARCHITECTURE ROLE:
# This file is part of the SERVICE LAYER.
# It sits between:
#   main.py (controller)
#   and MySQL database (data layer)
#
# RESPONSIBILITIES:
# - Execute SQL queries
# - Retrieve session data
# - Format and display results
# - Close database connection safely
# ============================================================


# Import reusable MySQL connection function
from mysql_connection import connection


# ============================================================
# FUNCTION: view_speakers_sessions
# ============================================================
#
# PURPOSE:
# Retrieves all sessions and their associated speaker names
# from the database and displays them in a formatted output.
#
# DATABASE TABLE USED:
# - session
#
# COLUMNS USED:
# - speakerName
# - sessionTitle
# - sessionDate
#
# ============================================================

def view_speakers_sessions():

    # --------------------------------------------------------
    # Step 1: Establish database connection
    # --------------------------------------------------------
    conn = connection()

    # Create cursor object to execute SQL queries
    cursor = conn.cursor()

    # --------------------------------------------------------
    # Step 2: Define SQL query
    # --------------------------------------------------------
    # We query the session table directly because speaker
    # information is stored in the same table.
    # --------------------------------------------------------
    query = """
    SELECT speakerName, sessionTitle, sessionDate
    FROM session
    """

    # --------------------------------------------------------
    # Step 3: Execute query
    # --------------------------------------------------------
    cursor.execute(query)

    # Fetch all rows returned by the query
    results = cursor.fetchall()

    # --------------------------------------------------------
    # Step 4: Display results in CLI format
    # --------------------------------------------------------
    print('============================================')
    print('Speakers & Session Data')
    print('============================================')

    # Loop through each record and print formatted output
    for row in results:
        print("Speaker Name :", row[0])
        print("Session Title:", row[1])
        print("Session Date :", row[2])
        print("------------------------------")

    # --------------------------------------------------------
    # Step 5: Close database connection
    # --------------------------------------------------------
    conn.close()