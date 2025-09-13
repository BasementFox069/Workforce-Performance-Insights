import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create a folder for charts
os.makedirs("charts", exist_ok=True)

# Helper function for queries + optional plots
def run_query(query: str, conn: sqlite3.Connection, title: str, plot_type=None, x_col=None, y_col=None):
    print(f"\n--- {title} ---")
    df = pd.read_sql_query(query, conn)
    print(f"[{len(df)} rows returned]")
    print(df.head(20))  # tables still visible in console

    # Optional visualization
    if plot_type and not df.empty:
        plt.figure(figsize=(8, 5))
        if plot_type == "bar":
            plt.bar(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(title)
        elif plot_type == "barh":
            plt.barh(df[x_col], df[y_col])
            plt.xlabel(y_col)
            plt.ylabel(x_col)
            plt.title(title)
        elif plot_type == "line":
            plt.plot(df[x_col], df[y_col], marker="o")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(title)

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        # Save chart
        filename = f"charts/{title.replace(' ', '_')}.png"
        plt.savefig(filename, dpi=300)
        print(f"📊 Chart saved as: {filename}")

        plt.show()

    return df


def main():
    conn = sqlite3.connect("company.db")

    # 1. Sample employees
    run_query("SELECT * FROM employees LIMIT 5;", conn, "Sample Employees")

    # 2. Attendance summary
    run_query("""
    SELECT e.Name, e.Department,
           SUM(CASE WHEN a.Status='Present' THEN 1 ELSE 0 END) AS DaysPresent,
           SUM(CASE WHEN a.Status='Absent' THEN 1 ELSE 0 END) AS DaysAbsent,
           SUM(CASE WHEN a.Status='Leave' THEN 1 ELSE 0 END) AS DaysOnLeave
    FROM employees e
    JOIN attendance a ON e.EmployeeID = a.EmployeeID
    GROUP BY e.EmployeeID
    LIMIT 10;
    """, conn, "Attendance Summary (10 employees)")

    # 3. Average overtime by department
    run_query("""
    SELECT e.Department,
           ROUND(AVG(a.OvertimeHours),2) AS AvgOvertime
    FROM employees e
    JOIN attendance a ON e.EmployeeID = a.EmployeeID
    GROUP BY e.Department;
    """, conn, "Average Overtime by Department", plot_type="bar", x_col="Department", y_col="AvgOvertime")

    # 4. Top 5 most absent employees
    run_query("""
    SELECT e.Name, e.Department, COUNT(*) AS Absences
    FROM employees e
    JOIN attendance a ON e.EmployeeID = a.EmployeeID
    WHERE a.Status = 'Absent'
    GROUP BY e.EmployeeID
    ORDER BY Absences DESC
    LIMIT 5;
    """, conn, "Top 5 Most Absent Employees", plot_type="barh", x_col="Name", y_col="Absences")

    # 5. Payroll cost estimation
    run_query("""
    SELECT e.Department,
           ROUND(SUM(e.BaseSalary),2) AS TotalBaseSalaries,
           ROUND(SUM(a.OvertimeHours * 20),2) AS TotalOvertimeCost,
           ROUND(SUM(e.BaseSalary) + SUM(a.OvertimeHours * 20),2) AS TotalPayrollCost
    FROM employees e
    JOIN attendance a ON e.EmployeeID = a.EmployeeID
    GROUP BY e.Department
    ORDER BY TotalPayrollCost DESC;
    """, conn, "Payroll Cost Estimation by Department", plot_type="bar", x_col="Department", y_col="TotalPayrollCost")

    conn.close()


if __name__ == "__main__":
    main()
