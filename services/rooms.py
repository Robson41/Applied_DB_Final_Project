# ============================================================
# ROOMS SERVICE MODULE (FIXED VERSION)
# ============================================================
#
# PURPOSE:
# Handles retrieval and display of room data from MySQL.
#
# DATABASE TABLE:
# - room  (NOT rooms)
#
# ARCHITECTURE ROLE:
# Service Layer (between main.py and database)
# ============================================================


# Import reusable MySQL connection function
from mysql_connection import connection


# ============================================================
# FUNCTION: view_rooms
# ============================================================
#
# PURPOSE:
# Fetches all room records and displays them in a readable format.
#
# IMPORTANT:
# Uses table name "room" (singular) based on schema.
# ============================================================

def view_rooms():

    # --------------------------------------------------------
    # Step 1: Connect to database
    # --------------------------------------------------------
    conn = connection()

    if conn is None:
        print("Database connection failed. Cannot retrieve rooms.")
        return

    cursor = conn.cursor()

    try:
        # ----------------------------------------------------
        # Step 2: SQL QUERY
        # ----------------------------------------------------
        # IMPORTANT: table is "room", NOT "rooms"
        # ----------------------------------------------------
        query = "SELECT roomID, roomName, capacity FROM room"

        cursor.execute(query)
        results = cursor.fetchall()

        # ----------------------------------------------------
        # Step 3: Display output
        # ----------------------------------------------------
        print("\n====================")
        print("       ROOMS        ")
        print("====================")

        for row in results:
            print("Room ID   :", row[0])
            print("Room Name :", row[1])
            print("Capacity  :", row[2])
            print("--------------------")

    except Exception as err:
        print("Error retrieving rooms:", err)

    finally:
        # ----------------------------------------------------
        # Step 4: Close connection safely
        # ----------------------------------------------------
        cursor.close()
        conn.close()