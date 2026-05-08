# ============================================================
# MAIN CONTROLLER - APPLIED DATABASES FINAL PROJECT
# ============================================================
#
# PURPOSE:
# This file acts as the CONTROLLER layer of the application.
#
# RESPONSIBILITIES:
# - Display the command-line menu to the user
# - Capture user input
# - Route requests to the correct service-layer functions
# - Control overall application flow
# - Handle safe application exit
#
# IMPORTANT DESIGN PRINCIPLE:
# This file does NOT directly communicate with databases.
#
# Instead:
# - Business logic is handled in services/
# - Database connections are handled in:
#       mysql_connection.py
#       neo4j_connection.py
#
# ARCHITECTURE FLOW:
#
# User
#   ↓
# main.py (Controller Layer)
#   ↓
# services/ (Business Logic Layer)
#   ↓
# MySQL / Neo4j (Data Layer)
#
# ============================================================


# ============================================================
# IMPORT SPEAKERS SERVICE FUNCTIONS
# ============================================================
#
# Imports function responsible for retrieving:
# - Speakers
# - Sessions
#
# ============================================================

from services.speakers import view_speakers_sessions


# ============================================================
# IMPORT ATTENDEES SERVICE FUNCTIONS
# ============================================================
#
# Imports functions responsible for:
# - Adding attendees
# - Viewing attendees by company
#
# ============================================================

from services.attendees import (
    add_attendee,
    view_attendees_by_company
)


# ============================================================
# IMPORT ROOMS SERVICE FUNCTION
# ============================================================
#
# Imports function responsible for retrieving room data.
#
# ============================================================

from services.rooms import view_rooms


# ============================================================
# IMPORT NEO4J CONNECTION SERVICE FUNCTIONS
# ============================================================
#
# Imports functions responsible for:
# - Viewing attendee graph connections
# - Creating attendee relationships
#
# ============================================================

from services.connections import (
    view_connections,
    add_connection
)


# ============================================================
# FUNCTION: show_menu
# ============================================================
#
# PURPOSE:
# Displays the command-line interface (CLI) menu.
#
# This function only handles menu display.
# It does NOT process business logic or database queries.
#
# ============================================================

def show_menu():

    # Print menu header
    print("\n======================================")
    print("     APPLIED DATABASES PROJECT        ")
    print("======================================")

    # Display menu options to user
    print("1. View Speakers & Sessions")
    print("2. View Attendees by Company")
    print("3. Add New Attendee")
    print("4. View Connected Attendees")
    print("5. Add Attendee Connection")
    print("6. View Rooms")
    print("x. Exit")

    # Print footer line
    print("======================================")


# ============================================================
# FUNCTION: main
# ============================================================
#
# PURPOSE:
# Main controller loop for the application.
#
# RESPONSIBILITIES:
# - Keep application running
# - Capture user menu selections
# - Route requests to service-layer functions
# - Handle invalid input safely
#
# ============================================================

def main():

    # Infinite loop keeps application running
    # until user explicitly exits
    while True:

        # Display menu to user
        show_menu()

        # Capture user input from keyboard
        # .strip() removes accidental spaces
        choice = input("Select an option: ").strip()

        # ====================================================
        # ROUTING LOGIC
        # ====================================================
        #
        # Each menu option routes execution
        # to a specific service-layer function.
        #
        # ====================================================

        # ----------------------------------------------------
        # OPTION 1
        # View speakers and sessions
        # ----------------------------------------------------

        if choice == "1":

            # Call function from speakers service module
            view_speakers_sessions()

        # ----------------------------------------------------
        # OPTION 2
        # View attendees grouped by company
        # ----------------------------------------------------

        elif choice == "2":

            # Call function from attendees service module
            view_attendees_by_company()

        # ----------------------------------------------------
        # OPTION 3
        # Add new attendee
        # ----------------------------------------------------

        elif choice == "3":

            # Call attendee insertion function
            add_attendee()

        # ----------------------------------------------------
        # OPTION 4
        # View attendee graph connections
        # ----------------------------------------------------

        elif choice == "4":

            # Call Neo4j graph retrieval function
            view_connections()

        # ----------------------------------------------------
        # OPTION 5
        # Create attendee graph connection
        # ----------------------------------------------------

        elif choice == "5":

            # Call Neo4j relationship creation function
            add_connection()

        # ----------------------------------------------------
        # OPTION 6
        # View rooms
        # ----------------------------------------------------

        elif choice == "6":

            # Call room retrieval function
            view_rooms()

        # ====================================================
        # EXIT CONDITION
        # ====================================================
        #
        # Allows user to safely terminate application.
        #
        # .lower() allows both:
        # - x
        # - X
        #
        # ====================================================

        elif choice.lower() == "x":

            # Display exit message
            print("\nExiting application... Goodbye!")

            # Break exits infinite loop
            break

        # ====================================================
        # INVALID INPUT HANDLING
        # ====================================================
        #
        # Prevents application crash if user enters
        # invalid menu option.
        #
        # ====================================================

        else:

            # Display validation error message
            print("\nInvalid option. Please try again.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
#
# PURPOSE:
# Ensures the main() function only runs when this
# file is executed directly.
#
# Prevents automatic execution if imported elsewhere.
#
# ============================================================

if __name__ == "__main__":

    # Start main application loop
    main()