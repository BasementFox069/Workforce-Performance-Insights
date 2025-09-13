# Workforce Performance Insights (Python + SQL)

A mini HR analytics project that simulates payroll and attendance data, loads it into a relational database (SQLite), and extracts **business insights** using SQL + Python.

---

## 🚀 Features
- **Data generation**:HR datasets (employees, attendance logs).
- **Database setup**: Load CSVs into SQLite (`company.db`).
- **Analysis queries** (SQL + Pandas):
  - Attendance summaries
  - Top 5 most absent employees
  - Average overtime by department
  - Payroll cost estimation (base + overtime)
  - Punctuality analysis (late arrivals)
  - Overtime champions
- **Charts** auto-saved in `/charts`.

---

## 📂 Project Structure
```text
PayrollProject/
├── generate_data.py      # Creates sample CSVs
├── setup_db.py           # Loads CSVs into SQLite
├── analysis.py           # Runs SQL queries + charts
├── company.db            # Database 
├── employee_data.csv     # Generated data
├── attendance_data.csv   # Generated data
└── charts/               # Auto-generated PNGs
```


---

## 🖥️ Outputs

**Average Overtime by Department**  
<p align="center">
  <img src="charts/Average_Overtime_by_Department.png" alt="Average Overtime by Department" width="500">
</p>

**Top 5 Most Absent Employees**  
<p align="center">
  <img src="charts/Top_5_Most_Absent_Employees.png" alt="Top 5 Most Absent Employees" width="500">
</p>

**Payroll Cost Estimation by Department**  
<p align="center">
  <img src="charts/Payroll_Cost_Estimation_by_Department.png" alt="Payroll Cost Estimation by Department" width="500">
</p>


---

## ⚙️ How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/BasementFox069/Workforce-Performance-Insights.git
   cd Workforce-Performance-Insights
