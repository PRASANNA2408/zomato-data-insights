🍽️ Zomato Data Insights – CRUD Application
An interactive Streamlit application for performing CRUD (Create, Read, Update, Delete) operations on a MySQL database containing Zomato-like data.
This project offers a simple yet powerful platform for database manipulation, enabling users to query, update, and explore data effortlessly.


📌 Features
Create – Add new records to the database

Read – Retrieve and filter records from tables

Update – Modify records with conditional filters

Delete – Remove records based on criteria

Alter Tables – Add, modify, or drop table columns

Predefined Queries – Execute 20+ SQL queries for insights

Interactive UI – Explore customers, restaurants, orders, and deliveries in scrollable tables



🗂 Project Structure
pgsql
Copy
Edit
Zomato-Data-Insights/
│
├── Pages/
│   ├── CRUD.py          # Perform CRUD operations via Streamlit UI
│   ├── Query.py         # Execute predefined SQL queries
│   ├── Table.py         # View datasets interactively
│
├── Scripts/
│   ├── Data Sets.py     # Generate synthetic datasets (using Faker)
│   ├── SQLconnection.py # Connect to MySQL & create tables
│   ├── class_CRUD.py    # CRUDOperations class for handling SQL logic
│   ├── class_DataManager.py # Database connection management
│
├── main.py              # Streamlit front page
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
