# ============================================================
# MAIN ENTRY POINT - APPLIED DATABASES FINAL PROJECT
# ============================================================
# This file acts as the CONTROLLER layer of the application.
#
# In software architecture terms:
# - main.py = Controller (handles user interaction + routing)
# - services/* = Business logic (database operations)
# - mysql_connection.py / neo4j_connection.py = Data layer
#
# Its responsibility is NOT to interact with databases directly,
# but to coordinate user input and delegate tasks to service modules.
# ============================================================


# Import service-layer functions
# Each imported function represents a specific feature of the system
# These functions encapsulate database logic (MySQL or Neo4j)

# ============================================================
# SERVICE LAYER IMPORTS (APPLICATION ARCHITECTURE)
# ============================================================
#
# These imports connect the MAIN CONTROLLER (main.py)
# to the SERVICE LAYER of the application.
#
# In this project design, we follow a modular architecture:
#
#   main.py
#     ↓ (delegates tasks)
#   services/  → contains business logic
#     ↓
#   database layer (MySQL / Neo4j)
#
# This separation is important because it:
# - Improves code maintainability
# - Allows reuse of database functions
# - Keeps UI logic separate from data logic
# - Reflects real-world enterprise application structure
#
# ============================================================

# ============================================================
# SERVICE LAYER IMPORTS (APPLICATION ARCHITECTURE)
# ============================================================
#
# These imports connect the MAIN CONTROLLER (main.py)
# to the SERVICE LAYER of the application.
#
# In this project design, we follow a modular architecture:
#
#   main.py
#     ↓ (delegates tasks)
#   services/  → contains business logic
#     ↓
#   database layer (MySQL / Neo4j)
#
# This separation is important because it:
# - Improves code maintainability
# - Allows reuse of database functions
# - Keeps UI logic separate from data logic
# - Reflects real-world enterprise application structure
#
# ============================================================


from services.speakers import view_speakers_sessions
from services.attendees import add_attendee, view_attendees_by_company
from services.rooms import view_rooms
from services.connections import view_connections, add_connection

