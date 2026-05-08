# ============================================================
# ATTENDEES SERVICE MODULE
# ============================================================
#
# PURPOSE:
# This module handles all operations related to:
# - Attendees
#
# DATABASE USED:
# MySQL (relational database)
#
# ARCHITECTURE ROLE:
# This file is part of the SERVICE LAYER.
# It contains business logic for attendee-related operations
# and communicates with the database via mysql_connection.py.
#
# RESPONSIBILITIES:
# - Insert new attendee records
# - Retrieve attendee data
# - Group/filter attendee information
# ============================================================


# Import reusable MySQL connection function
from mysql_connection import connection


# ============================================================
# FUNCTION: add_attendee
# ============================================================
#
# PURPOSE:
# Inserts a new attendee record into the database.
#
# USER INPUT:
# - Attendee name
# - Company name
#
# DATABASE OPERATION:
# INSERT INTO attendees table
# ============================================================

def add_attendee():

    # Prompt user for attendee name
    name = input("Enter attendee name: ")

    # Prompt user for company name
    company = input("Enter company name: ")

    # Create connection to MySQL database
    conn = connection()

    # Create cursor object for executing SQL commands
    cursor = conn.cursor()

    # ========================================================
    # SQL INSERT QUERY
    # ========================================================
    # Uses parameterised query (%s placeholders)
    # This helps prevent SQL injection attacks
    # ========================================================

    query = "INSERT INTO attendees (name, company) VALUES (%s, %s)"

    # Execute query with user-provided values
    cursor.execute(query, (name, company))

    # Commit transaction to permanently save changes
    conn.commit()

    # Close database connection
    conn.close()

    # Confirm successful insertion
    print("✔ Attendee successfully added")


# ============================================================
# FUNCTION: view_attendees_by_company
# ============================================================
#
# PURPOSE:
# Retrieves all attendees and groups them by company.
#
# DATABASE OPERATION:
# SELECT query with ORDER BY clause
#
# ============================================================

def view_attendees_by_company():

    # Create connection to database
    conn = connection()

    # Create cursor for SQL execution
    cursor = conn.cursor()

    # ========================================================
    # SQL QUERY EXPLANATION
    # ========================================================
    # Retrieves all attendees from the database
    # Orders results by company name for grouping effect
    # ========================================================

    query = """
    SELECT name, company
    FROM attendees
    ORDER BY company
    """

    # Execute query
    cursor.execute(query)

    # Fetch all results from database
    results = cursor.fetchall()

    # Print section header
    print("\n==============================")
    print("   ATTENDEES BY COMPANY       ")
    print("==============================")

    # Loop through each attendee record
    for row in results:

        # row[0] = attendee name
        # row[1] = company name

        print("Name   :", row[0])
        print("Company:", row[1])
        print("------------------------------")

    # Close database connection
    conn.close()