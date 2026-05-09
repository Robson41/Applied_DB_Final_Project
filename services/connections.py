# ============================================================
# CONNECTIONS SERVICE MODULE (NEO4J - FINAL VERSION)
# ============================================================
#
# PURPOSE:
# This module handles all Neo4j graph database operations:
# - Viewing attendee-to-attendee relationships
# - Creating connections between attendees
#
# DATABASE:
# Neo4j (Graph Database)
#
# GRAPH MODEL:
# (Attendee)-[:CONNECTED_TO]-(Attendee)
#
# ARCHITECTURE ROLE:
# Service Layer
# (Called by main.py, interacts with Neo4j only)
#
# ============================================================


# Import Neo4j driver factory function from connection module
from neo4j_connection import get_driver


# ============================================================
# FUNCTION: view_connections
# ============================================================
#
# PURPOSE:
# Retrieves and displays all attendee relationships stored in Neo4j.
#
# WHAT IT DOES:
# - Connects to Neo4j
# - Runs a Cypher MATCH query
# - Fetches all CONNECTED_TO relationships
# - Prints them in a readable format
#
# ============================================================

def view_connections():

    # Get Neo4j driver instance (connection to database)
    driver = get_driver()

    try:
        # Open a session (required to run Cypher queries)
        with driver.session() as session:

            # ----------------------------------------------------
            # CYPHER QUERY
            # ----------------------------------------------------
            # MATCH: finds relationships between Attendee nodes
            # RETURN: retrieves attendee names for display
            # ----------------------------------------------------

            result = session.run("""
            MATCH (a1:Attendee)-[:CONNECTED_TO]-(a2:Attendee)
            RETURN a1.attendeeName AS from_attendee,
                   a2.attendeeName AS to_attendee
            """)

            # Print formatted header
            print("\n===================================")
            print("      ATTENDEE CONNECTIONS         ")
            print("===================================")

            # Track whether any results exist
            found = False

            # Loop through query results
            for record in result:
                found = True
                print(f"{record['from_attendee']} → {record['to_attendee']}")

            # If no relationships exist
            if not found:
                print("No connections found.")

    except Exception as e:
        # Handle errors safely (prevents program crash)
        print("Error retrieving connections:", e)

    finally:
        # Always close Neo4j driver connection
        driver.close()


# ============================================================
# FUNCTION: add_connection
# ============================================================
#
# PURPOSE:
# Creates a relationship between two attendees in Neo4j.
#
# USER INPUT:
# - First attendee name
# - Second attendee name
#
# IMPORTANT:
# Both attendees must already exist as nodes in Neo4j.
#
# ============================================================

def add_connection():

    # Collect input from user
    name1 = input("Enter first attendee name: ")
    name2 = input("Enter second attendee name: ")

    # Get Neo4j driver instance
    driver = get_driver()

    try:
        with driver.session() as session:

            # ----------------------------------------------------
            # CYPHER QUERY EXPLANATION
            # ----------------------------------------------------
            # MATCH: finds both attendee nodes by name
            # MERGE: creates relationship if it does not exist
            #         (prevents duplicate relationships)
            # RETURN: confirms nodes used in relationship
            # ----------------------------------------------------

            result = session.run("""
            MATCH (a1:Attendee {attendeeName: $name1})
            MATCH (a2:Attendee {attendeeName: $name2})
            MERGE (a1)-[:CONNECTED_TO]-(a2)
            RETURN a1, a2
            """,
            name1=name1,
            name2=name2
            )

            # Convert result to list to check if operation succeeded
            records = list(result)

            # If no records returned, nodes likely do not exist
            if len(records) == 0:
                print("⚠ Could not create connection (attendees may not exist)")
            else:
                print("✔ Connection successfully created")

    except Exception as e:
        # Catch and display any Neo4j errors
        print("Error creating connection:", e)

    finally:
        # Always close connection to free resources
        driver.close()