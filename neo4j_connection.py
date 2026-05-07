
# Import the GraphDatabase class from the neo4j module
# "from ... import ..." is Python syntax used to import specific functionality
from neo4j import GraphDatabase

# Create a driver object that manages the connection to Neo4j
# Variable assignment uses "=" in Python
driver = GraphDatabase.driver(
    
    # Connection string (Bolt protocol)
    # "bolt://" is the protocol used by Neo4j
    "bolt://localhost:7687",


    # Connection string (Bolt protocol)
    # "bolt://" is the protocol used by Neo4j
    auth=("neo4j", "password")  # change if needed
)

def test():
    with driver.session() as session:
        result = session.run("RETURN 'Neo4j is working' AS msg")
        print(result.single()["msg"])

test()
driver.close()



