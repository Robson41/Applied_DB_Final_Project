# Applied Databases Final Project

## Overview

This project is a Python-based menu-driven application that demonstrates the integration of **two different database technologies**:

* **MySQL (Relational Database)**
* **Neo4j (Graph Database)**

It simulates a conference-style system where:

* Structured data (attendees, speakers, sessions, rooms, companies) is stored in MySQL
* Relationships between attendees are stored in Neo4j

This reflects real-world systems where relational and graph databases are used together for different types of data modelling.

---

## Technologies Used

* Python 3.13
* MySQL (running in Docker)
* Neo4j (graph database)
* mysql-connector-python
* neo4j Python driver
* Docker

---

## Project Structure

```
Applied_DB_Final_Project/
│
├── main.py
├── mysql_connection.py
├── neo4j_connection.py
│
├── services/
│   ├── speakers.py
│   ├── attendees.py
│   ├── connections.py
│   └── rooms.py
│
├── utils/
│   └── validation.py
│
├── appdbproj.sql
├── Innovation.pdf
├── GitLink.txt
├── README.md
│
└── venv/   (NOT included in submission)
```

---

## Database Setup

### MySQL (Docker Setup)

MySQL was run using Docker:

```
docker run --name new_mysql \
-e MYSQL_ROOT_PASSWORD=password \
-p 3306:3306 \
-d mysql
```

### Database Import

The database was created using the provided SQL file:

```
docker exec -i new_mysql mysql -u root -ppassword < appdbproj.sql
```

This creates the database:

* `appdbproj`

---

## MySQL Connection (Python)

The application connects to MySQL using the following configuration:

```python
import mysql.connector

def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="appdbproj"
    )
```

---

## Neo4j Connection (Python)

Neo4j is used to manage relationships between attendees.

```python
from neo4j import GraphDatabase

def get_neo4j_driver():
    return GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("neo4j", "password")
    )
```

---

## Application Features

The system is menu-driven and provides the following options:

```
1. View Speakers & Sessions
2. View Attendees by Company
3. Add New Attendee
4. View Connected Attendees
5. Add Attendee Connection
6. View Rooms
x. Exit
```

---

## Core Functionality

### 1. View Speakers & Sessions

* Displays speakers and their associated sessions
* Uses SQL JOIN queries across:

  * speakers
  * sessions
  * rooms

---

### 2. View Attendees by Company

* Input: Company ID
* Displays:

  * Attendee details
  * Session information
  * Speaker details
  * Room allocation

Includes validation for:

* Invalid company IDs
* Non-existent companies
* Companies with no attendees

---

### 3. Add New Attendee

* Inserts a new attendee into the database

Fields include:

* ID
* Name
* Date of Birth
* Gender
* Company ID

Validation includes:

* Duplicate ID checks
* Invalid input types
* Invalid company references
* Gender validation

---

### 4. View Rooms

* Displays room details:

  * Room ID
  * Name
  * Capacity

Optimisation:

* Results are cached after first load during runtime

---

### 5. View Connected Attendees (Neo4j)

* Retrieves relationships between attendees using:

```cypher
MATCH (a:Attendee {id: $id})-[:CONNECTED_TO]-(b)
RETURN b
```

Validation:

* Checks attendee exists in MySQL first
* Handles cases where no connections exist

---

### 6. Add Attendee Connection (Neo4j)

* Creates relationships between attendees:

```cypher
MERGE (a)-[:CONNECTED_TO]-(b)
```

Validation:

* Prevents self-connections
* Prevents duplicate connections
* Ensures both attendees exist in MySQL

---

## Error Handling

The application includes robust validation for:

* Numeric input validation
* Missing database records
* Duplicate entries
* Logical constraints (e.g. self-relationships)
* Database connection errors

---

## Setup Instructions

### 1. Install Dependencies

```
pip install mysql-connector-python neo4j
```

---

### 2. Start MySQL Docker Container

```
docker run --name new_mysql \
-e MYSQL_ROOT_PASSWORD=password \
-p 3306:3306 \
-d mysql
```

---

### 3. Import Database

```
docker exec -i new_mysql mysql -u root -ppassword < appdbproj.sql
```

---

### 4. Run Application

```
python main.py
```

---

## Innovation Highlights

This project includes the following innovation elements:

* Use of **Docker for database deployment**
* Integration of **two database paradigms (Relational + Graph)**
* Structured modular Python design
* Error handling and validation across all inputs
* Separation of concerns (services/utils architecture)

---

## Key Learning Outcomes

This project demonstrates:

* Working with relational databases (MySQL)
* Working with graph databases (Neo4j)
* Python database integration
* SQL query design and joins
* Graph relationship modelling
* Input validation and error handling
* Docker-based database deployment

---

## Author

Mark Hynes

GitHub Repository:
(Add your GitHub link in GitLink.txt)

---

## Notes for Marker

* MySQL runs in Docker container
* Database is provided via `appdbproj.sql`
* Neo4j is used for relationship modelling
* Application is fully menu-driven and interactive

