# Dictionary Application

This project is a dictionary application that allows users to register, log in, add words, and search for their definitions. It provides both console-based and GUI interfaces to interact with the system. The project is designed to showcase core concepts in data engineering, including database management, data persistence, and user interaction.

## Features

- **User Management:**
  - Register and log in users securely.
- **Word Management:**
  - Add and search for words with definitions stored in a relational database.
- **GUI Interface:**
  - User-friendly graphical interface built with Tkinter.
- **Data Engineering Showcase:**
  - Efficient database design for word and user management.
  - Structured query operations for CRUD functionalities.
  - Data persistence through relational database tables.

## Requirements

- **Python 3.x**
- Required packages (install using pip):
  ```bash
  pip install pyodbc
  ```

## Database Setup

Ensure that your database is properly configured and that the required tables (`Users`, `Words`, and `UserDictionary`) are created.

### Database ERD (Entity-Relationship Diagram)

Below is the ERD showcasing the structure and relationships between the tables:

![image](https://github.com/user-attachments/assets/c421da56-dc75-4cdb-b6e2-6f8a7e7f16f2)


- **Users Table:** Stores user information such as username and password.
- **Words Table:** Stores dictionary words and their definitions.
- **UserDictionary Table:** Associates users with their added words.

## Running the Project

### Console Application

Run the following command to use the console version:

```bash
python app.py
```

### GUI Application

To launch the GUI version:

```bash
python app_gui.py
```

## Project Structure

```plaintext
DictionaryProject/
├── app.py               # Console-based application entry point
├── app_gui.py            # GUI-based application entry point
├── database.py           # Database connection and setup
├── user_management.py    # User registration and login logic
├── word_management.py    # Word addition and search logic
├── README.md             # Project documentation
└── venv/                 # Virtual environment (optional)
```

## Demo

Below are sample screenshots of the application's functionality:

### **User Registration**
*(Screenshot here)*

### **Word Addition**
*(Screenshot here)*

### **Search Functionality**
*(Screenshot here)*

Ensure that the application connects to the database and performs operations as expected.

## Data Engineering Showcase

- **Database Schema Design:** Optimized for efficient lookups and user-specific word storage.
- **Data Persistence:** Ensures consistent and reliable storage through transactional commits.
- **Structured Queries:** Efficient and secure SQL queries for word and user operations.
- **Scalability Considerations:** Well-structured schema to handle additional features or user loads.

This project serves as a practical demonstration of core data engineering and application development principles.

