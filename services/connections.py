# ============================================================
# CONNECTIONS SERVICE MODULE (NEO4J)
# ============================================================
#
# PURPOSE:
# This module handles all graph database operations related to:
# - Viewing attendee connections
# - Creating attendee relationships
#
# DATABASE USED:
# Neo4j (graph database)
#
# ARCHITECTURE ROLE:
# This file belongs to the SERVICE LAYER.
# It contains business logic related to graph relationships
# and communicates with Neo4j through neo4j_connection.py.
#
# GRAPH MODEL:
# (Attendee)-[:CONNECTED_TO]->(Attendee)
#
# RESPONSIBILITIES:
# - Execute Cypher queries
# - Retrieve graph relationships
# - Create new graph relationships
# ============================================================


# Import reusable Neo4j driver function
from neo4j_connection import get_driver


# ============================================================
# FUNCTION: view_connections
# ============================================================
#
# PURPOSE:
# Retrieves and displays all attendee connections
# stored in the Neo4j graph database.
#
# DATABASE OPERATION:
# Uses a Cypher MATCH query to retrieve relationships
# between attendee nodes.
#
# ============================================================

def view_connections():

    # Create Neo4j driver connection
    # Uses reusable function from neo4j_connection.py
    driver = get_driver()

    # Open a Neo4j session
    # Sessions are used to execute Cypher queries
    with driver.session() as session:

        # ====================================================
        # CYPHER QUERY EXPLANATION
        # ====================================================
        #
        # MATCH:
        # Searches the graph database for a relationship pattern
        #
        # GRAPH PATTERN:
        # (a1:Attendee)-[:CONNECTED_TO]->(a2:Attendee)
        #
        # This means:
        # - Find an Attendee node called a1
        # - Find another Attendee node called a2
        # - Find a CONNECTED_TO relationship between them
        #
        # RETURN:
        # Returns attendee names for display
        # ====================================================

        result = session.run("""
        MATCH (a1:Attendee)-[:CONNECTED_TO]->(a2:Attendee)
        RETURN a1.name AS from_attendee,
               a2.name AS to_attendee
        """)

        # Print section header
        print("\n===================================")
        print("      ATTENDEE CONNECTIONS         ")
        print("===================================")

        # Loop through each relationship returned
        for record in result:

            # record["from_attendee"] = starting node
            # record["to_attendee"] = connected node

            print(
                f"{record['from_attendee']} "
                f"→ "
                f"{record['to_attendee']}"
            )

    # Close Neo4j driver connection
    driver.close()


# ============================================================
# FUNCTION: add_connection
# ============================================================
#
# PURPOSE:
# Creates a new relationship between two attendees
# in the Neo4j graph database.
#
# USER INPUT:
# - First attendee name
# - Second attendee name
#
# DATABASE OPERATION:
# Uses Cypher CREATE statement
#
# ============================================================

def add_connection():

    # Prompt user for first attendee name
    name1 = input("Enter first attendee name: ")

    # Prompt user for second attendee name
    name2 = input("Enter second attendee name: ")

    # Create Neo4j driver connection
    driver = get_driver()

    # Open Neo4j session
    with driver.session() as session:

        # ====================================================
        # CYPHER QUERY EXPLANATION
        # ====================================================
        #
        # MATCH:
        # Finds existing attendee nodes in the graph
        #
        # CREATE:
        # Creates a CONNECTED_TO relationship
        #
        # PARAMETERS:
        # $name1 and $name2 are parameterised values
        # passed safely into the query
        #
        # ====================================================

        session.run("""
        MATCH (a1:Attendee {name: $name1})
        MATCH (a2:Attendee {name: $name2})
        CREATE (a1)-[:CONNECTED_TO]->(a2)
        """,
        name1=name1,
        name2=name2
        )

    # Display confirmation message
    print("✔ Connection successfully created")

    # Close Neo4j driver connection
    driver.close()