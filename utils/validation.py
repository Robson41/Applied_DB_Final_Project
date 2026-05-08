# ============================================================
# VALIDATION UTILITY MODULE
# ============================================================
#
# PURPOSE:
# This module contains reusable validation functions.
#
# ARCHITECTURE ROLE:
# This file belongs to the UTILITIES LAYER.
#
# WHY VALIDATION IS IMPORTANT:
# - Prevents invalid user input
# - Improves data integrity
# - Reduces database errors
# - Improves user experience
#
# DESIGN PRINCIPLE:
# Validation logic is separated from business logic
# to improve maintainability and code reuse.
#
# ============================================================


# ============================================================
# FUNCTION: validate_menu_option
# ============================================================
#
# PURPOSE:
# Validates menu selections entered by the user.
#
# PARAMETERS:
# option = user input from main menu
#
# RETURNS:
# True  = valid option
# False = invalid option
#
# ============================================================

def validate_menu_option(option):

    # Create list of valid menu options
    valid_options = ["1", "2", "3", "4", "5", "6", "x", "X"]

    # Check if user input exists in valid options list
    if option in valid_options:
        return True

    # Otherwise input is invalid
    return False


# ============================================================
# FUNCTION: validate_text_input
# ============================================================
#
# PURPOSE:
# Ensures text input is not empty.
#
# PARAMETERS:
# text = user-provided input
#
# RETURNS:
# True  = valid text
# False = invalid text
#
# ============================================================

def validate_text_input(text):

    # Remove leading/trailing spaces
    cleaned_text = text.strip()

    # Check if text is empty after trimming spaces
    if cleaned_text == "":
        return False

    # Otherwise input is valid
    return True