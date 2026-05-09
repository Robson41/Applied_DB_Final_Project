# ============================================================
# IMPORT SECTION
# ============================================================
#
# "import" in Python is used to bring in external libraries.
# Here we import GraphDatabase from the neo4j driver package.
#
# This gives us access to:
# - Database connections
# - Sessions
# - Cypher query execution
# ============================================================

from neo4j import GraphDatabase


# ============================================================
# FUNCTION: get_driver()
# ============================================================
#
# A function is defined using the "def" keyword.
# Syntax:
#   def function_name(parameters):
#
# This function has NO parameters because all config is hardcoded.
# ============================================================

def get_driver():

    # ========================================================
    # GraphDatabase.driver()
    # ========================================================
    #
    # This is a CLASS METHOD (factory method).
    # It creates a DRIVER object which is the main entry point
    # for connecting to Neo4j.
    #
    # Syntax breakdown:
    #
    #   driver = ClassName.method(arguments)
    #
    # ========================================================

    driver = GraphDatabase.driver(

        # ----------------------------------------------------
        # CONNECTION STRING (URI)
        # ----------------------------------------------------
        # "bolt://" is the protocol used by Neo4j
        # localhost = running on your own machine
        # 7687 = default Neo4j Bolt port
        # ----------------------------------------------------

        "bolt://localhost:7687",

        # ----------------------------------------------------
        # AUTHENTICATION TUPLE
        # ----------------------------------------------------
        # This is a Python tuple:
        #
        # ("username", "password")
        #
        # Neo4j uses this to verify access rights
        # ----------------------------------------------------

        auth=("neo4j", "password")
    )

    # ========================================================
    # return keyword
    # ========================================================
    #
    # "return" sends the driver object back to whoever
    # called this function.
    #
    # Without return, the driver would be lost after function ends
    # ========================================================

    return driver


# ============================================================
# TEST BLOCK (IMPORTANT PYTHON CONCEPT)
# ============================================================
#
# Python sets a special variable called:
#
#   __name__
#
# If this file is RUN directly:
#   __name__ == "__main__"
#
# If this file is IMPORTED:
#   __name__ == "neo4j_connection"
#
# This allows safe testing without affecting imports.
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Create driver using our function
    # --------------------------------------------------------
    driver = get_driver()

    # --------------------------------------------------------
    # "with" statement (context manager)
    # --------------------------------------------------------
    #
    # This automatically closes the session when done
    # even if errors happen.
    #
    # Syntax:
    #   with object as variable:
    #       do something
    # --------------------------------------------------------

    with driver.session() as session:

        # ----------------------------------------------------
        # session.run()
        # ----------------------------------------------------
        #
        # Executes a Cypher query on the database.
        #
        # Cypher is Neo4j's query language (like SQL for graphs)
        #
        # Here we return a simple string to test connection
        # ----------------------------------------------------

        result = session.run(
            "RETURN 'Neo4j is working' AS msg"
        )

        # ----------------------------------------------------
        # result.single()
        # ----------------------------------------------------
        #
        # Extracts a single row from the result set
        # because we only returned one value
        # ----------------------------------------------------

        print(result.single()["msg"])

    # --------------------------------------------------------
    # driver.close()
    # --------------------------------------------------------
    #
    # Frees resources and closes connection properly
    # VERY IMPORTANT in real applications
    # --------------------------------------------------------

    driver.close()