# ============================================================
# MYSQL CONNECTION MODULE
# ============================================================
#
# PURPOSE:
# This module is responsible ONLY for creating a connection
# between Python and the MySQL database.
#
# It is part of the INFRASTRUCTURE / DATA ACCESS LAYER.
#
# It is reused by all service-layer modules such as:
#   - attendees.py
#   - speakers.py
#   - rooms.py
#   - connections.py
#
# BENEFITS:
# - Centralised connection logic (no duplication)
# - Easier debugging and maintenance
# - Cleaner architecture separation
# ============================================================


# Import MySQL connector library
# This allows Python to communicate with MySQL
import mysql.connector


# ============================================================
# FUNCTION: connection()
# ============================================================
#
# PURPOSE:
# Establishes and returns a live connection to the MySQL database.
#
# RETURN VALUE:
# - MySQL connection object if successful
# - None if connection fails
#
# USED BY:
# - All service-layer modules (CRUD operations)
#
# ============================================================

def connection():

    try:
        # --------------------------------------------------------
        # CREATE DATABASE CONNECTION
        # --------------------------------------------------------
        # These credentials define how Python connects to MySQL:
        #
        # host     → where MySQL is running (localhost = your machine)
        # user     → MySQL username (root in this case)
        # password → MySQL password (must match Docker/MySQL setup)
        # database → schema name we want to use (appdbproj)
        # --------------------------------------------------------

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',   # IMPORTANT: update if your password differs
            database='appdbproj'
        )

        # --------------------------------------------------------
        # VERIFY CONNECTION STATUS
        # --------------------------------------------------------
        # is_connected() ensures the connection is valid
        # before returning it to the calling module
        # --------------------------------------------------------

        if conn.is_connected():

            # Confirmation message for debugging / CLI feedback
            print("Successful connection to MySQL database")

            # Return active connection to service layer
            return conn

        else:
            # If connection object is created but not active
            print("Connection failed")
            return None

    except mysql.connector.Error as err:

        # --------------------------------------------------------
        # ERROR HANDLING (MYSQL-SPECIFIC ERRORS)
        # --------------------------------------------------------
        # Catches issues such as:
        # - wrong password
        # - database does not exist
        # - MySQL server not running
        # - Docker container not accessible
        # --------------------------------------------------------

        print("Database connection error:", err)

        return None


# ============================================================
# TESTING BLOCK (OPTIONAL DEVELOPMENT CHECK)
# ============================================================
#
# This runs ONLY when executing this file directly:
#
#   python mysql_connection.py
#
# It will NOT run when imported into other modules.
#
# PURPOSE:
# - Quick sanity check that DB connection works
# - Useful during setup/debugging
# ============================================================

if __name__ == "__main__":

    # Attempt connection test
    connection()