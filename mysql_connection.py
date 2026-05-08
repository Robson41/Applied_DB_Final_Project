# Import the mysql connector library
# This library allows Python to communicate with MySQL
import mysql.connector

# Create a connection to the MySQL database
# Replace the values below with your own MySQL details
connection_details = mysql.connector.connect(host= 'localhost', user='root', password='password', database='appdbproj')

# Check if the connection was successful
if connection_details.is_connected:
    print("Successful connection to MySQL database")

else:
    print("Connection Failed")
    