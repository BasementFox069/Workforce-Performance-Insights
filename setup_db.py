print("🚀 setup_db.py started")

import sqlite3
import pandas as pd

# Load data from CSVs
employee_df = pd.read_csv("employee_data.csv")
attendance_df = pd.read_csv("attendance_data.csv")

# Connect to SQLite database (this will create company.db if it doesn't exist)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Drop tables if they already exist (so you can rerun without errors)
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS attendance")

# Create tables
cursor.execute("""
CREATE TABLE employees (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Designation TEXT,
    BaseSalary REAL
)
""")

cursor.execute("""
CREATE TABLE attendance (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    Date TEXT,
    Status TEXT,
    ClockIn TEXT,
    ClockOut TEXT,
    OvertimeHours REAL,
    FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID)
)
""")

# Insert employee data
employee_df.to_sql("employees", conn, if_exists="append", index=False)
attendance_df.to_sql("attendance", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("✅ Database 'company.db' created successfully with employees and attendance data.")

print("✅ Finished creating DB and inserting data")
