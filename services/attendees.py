# ============================================================
# ATTENDEES SERVICE MODULE (FINAL MARKS-READY VERSION)
# ============================================================
#
# PURPOSE:
# Handles all attendee-related database operations:
# - Add new attendee
# - View attendees grouped by company
#
# LAYER:
# Service Layer (between controller and MySQL database)
# ============================================================


# Import MySQL connection function
from mysql_connection import connection

# Import MySQL-specific error handling
import mysql.connector


# ============================================================
# FUNCTION: add_attendee
# ============================================================
#
# PURPOSE:
# Inserts a new attendee record into the attendee table.
#
# DB SCHEMA REQUIREMENTS:
# - attendeeID: AUTO_INCREMENT (not supplied)
# - attendeeDOB: DATE (YYYY-MM-DD)
# - attendeeGender: ENUM('Male','Female')
# - attendeeCompanyID: FOREIGN KEY
# ============================================================

def add_attendee():

    # --------------------------------------------------------
    # Step 1: Collect user input
    # --------------------------------------------------------
    name = input("Enter attendee name: ")
    dob = input("Enter DOB (YYYY-MM-DD): ")
    gender = input("Enter gender (Male/Female): ")
    company_id = input("Enter company ID: ")

    # --------------------------------------------------------
    # Step 2: Connect to database
    # --------------------------------------------------------
    conn = connection()

    if conn is None:
        print("Database connection failed. Cannot add attendee.")
        return

    cursor = conn.cursor()

    try:
        # ----------------------------------------------------
        # Step 3: SQL INSERT statement
        # ----------------------------------------------------
        # Parameterised query prevents SQL injection
        # and ensures safe data handling
        # ----------------------------------------------------
        query = """
        INSERT INTO attendee
        (attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
        VALUES (%s, %s, %s, %s)
        """

        # ----------------------------------------------------
        # Step 4: Execute query
        # ----------------------------------------------------
        cursor.execute(query, (name, dob, gender, company_id))

        # ----------------------------------------------------
        # Step 5: Commit transaction (save to DB)
        # ----------------------------------------------------
        conn.commit()

        print("✔ Attendee successfully added")

    except mysql.connector.Error as err:
        # Handles all MySQL-related errors (best practice)
        print("Database error while adding attendee:", err)

    finally:
        # ----------------------------------------------------
        # Step 6: Clean up resources
        # ----------------------------------------------------
        cursor.close()
        conn.close()


# ============================================================
# FUNCTION: view_attendees_by_company
# ============================================================
#
# PURPOSE:
# Retrieves all attendees and groups them by company name.
#
# RELATIONSHIP:
# attendee.attendeeCompanyID → company.companyID
# ============================================================

def view_attendees_by_company():

    # Connect to database
    conn = connection()

    if conn is None:
        print("Database connection failed. Cannot retrieve data.")
        return

    cursor = conn.cursor()

    try:
        # SQL JOIN query to combine attendee + company tables
        query = """
        SELECT a.attendeeName, c.companyName
        FROM attendee a
        JOIN company c ON a.attendeeCompanyID = c.companyID
        ORDER BY c.companyName
        """

        cursor.execute(query)
        results = cursor.fetchall()

        # Output formatting
        print("\n==============================")
        print("   ATTENDEES BY COMPANY       ")
        print("==============================")

        for row in results:
            print("Name   :", row[0])
            print("Company:", row[1])
            print("------------------------------")

    except mysql.connector.Error as err:
        print("Database error while retrieving attendees:", err)

    finally:
        cursor.close()
        conn.close()