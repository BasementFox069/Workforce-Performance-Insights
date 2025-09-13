import pandas as pd
import numpy as np
from datetime import datetime
import random
import os

# Folder to save CSVs
save_folder = os.path.expanduser('~/PayrollProject')
os.makedirs(save_folder, exist_ok=True)

# Employee data
departments = ['Finance', 'HR', 'Operations', 'Sales', 'IT', 'Marketing', 'Support']
designations = ['Analyst', 'Manager', 'Coordinator', 'Executive', 'Developer', 'Assistant']

employee_list = []
for emp_id in range(1, 51):
    employee_list.append({
        'EmployeeID': emp_id,
        'Name': f'Employee_{emp_id}',
        'Department': random.choice(departments),
        'Designation': random.choice(designations),
        'BaseSalary': random.randint(4000, 8000)
    })
employee_df = pd.DataFrame(employee_list)

# Attendance data
start_date = datetime(2025, 7, 1)
end_date = datetime(2025, 9, 30)
all_dates = pd.date_range(start_date, end_date, freq='D')

attendance_list = []
for _, emp in employee_df.iterrows():
    for date in all_dates:
        status = np.random.choice(['Present', 'Absent', 'Leave'], p=[0.85, 0.10, 0.05])
        clock_in = clock_out = None
        overtime_hours = 0
        if status == 'Present':
            clock_in = f"{random.randint(8,10)}:{random.choice(['00','15','30','45'])}"
            clock_out = f"{random.randint(17,19)}:{random.choice(['00','15','30','45'])}"
            overtime_hours = round(random.uniform(0,2), 2)
        attendance_list.append({
            'EmployeeID': emp['EmployeeID'],
            'Date': date.date(),
            'Status': status,
            'ClockIn': clock_in,
            'ClockOut': clock_out,
            'OvertimeHours': overtime_hours
        })
attendance_df = pd.DataFrame(attendance_list)

# Save CSVs
employee_df.to_csv(os.path.join(save_folder,'employee_data.csv'), index=False)
attendance_df.to_csv(os.path.join(save_folder,'attendance_data.csv'), index=False)

print(f"Generated CSVs in {save_folder}")
