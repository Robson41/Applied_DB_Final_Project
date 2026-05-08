# ============================================================
# NEO4J CONNECTION MODULE
# ============================================================
#
# PURPOSE:
# This module creates and returns a reusable Neo4j driver.
#
# DATABASE USED:
# Neo4j Graph Database
#
# DESIGN PRINCIPLES:
# - Separation of concerns
# - Reusable database connection
# - Centralised configuration
#
# WHY THIS IS IMPORTANT:
# Service modules can reuse this connection function
# without duplicating connection logic.
# ============================================================


# Import GraphDatabase class from neo4j package
from neo4j import GraphDatabase


# ============================================================
# FUNCTION: get_driver
# ============================================================
#
# PURPOSE:
# Creates and returns a Neo4j driver object.
#
# This driver is reused by service modules whenever
# Neo4j access is required.
#
# ============================================================

def get_driver():

    # Create Neo4j driver connection
    driver = GraphDatabase.driver(

        # Bolt protocol connection string
        "bolt://localhost:7687",

        # Authentication credentials
        auth=("neo4j", "password")
    )

    # Return reusable driver object
    return driver


# ============================================================
# OPTIONAL TEST BLOCK
# ============================================================
#
# This block only runs if this file is executed directly.
# It does NOT run when imported into service modules.
#
# ============================================================

if __name__ == "__main__":

    # Create Neo4j driver
    driver = get_driver()

    # Open Neo4j session
    with driver.session() as session:

        # Execute simple test query
        result = session.run(
            "RETURN 'Neo4j is working' AS msg"
        )

        # Print query result
        print(result.single()["msg"])

    # Close driver connection
    driver.close()