import os
import random
import csv
from datetime import datetime
from openpyxl import Workbook

# ==============================
# CONFIGURATION
# ==============================
FOLDER_NAME = "Student_Performance_Data"
CSV_FILE = "student_performance_5000.csv"
EXCEL_FILE = "student_performance_5000.xlsx"
NUM_RECORDS = 5000

# ==============================
# DATA SOURCES
# ==============================
FIRST_NAMES = [
    "Alice", "Brian", "Catherine", "David", "Ella", "Frank", "Grace", "Henry",
    "Isabella", "Jack", "Ketro", "Liam", "Mia", "Noah", "Olivia", "Paul",
    "Quinn", "Ryan", "Sophia", "Thomas", "Uma", "Victor", "Willow", "Xavier", "Yara", "Zane"
]

LAST_NAMES = [
    "Johnson", "Smith", "Lee", "Brown", "Garcia", "White", "Kim", "Wilson",
    "Taylor", "Anderson", "Sithole", "Martin", "Thompson", "Rodriguez", "Lewis",
    "Walker", "Adams", "Scott", "Hall", "Young", "Turner", "Hughes", "Perez", "Carter"
]

SUBJECTS = ["Math", "Science", "English", "History", "Computer Science"]

# ==============================
# FUNCTION TO GENERATE DATA
# ==============================
def generate_student_records(num_records=NUM_RECORDS):
    """Generate a list of student performance dictionaries."""
    records = []
    for _ in range(num_records):
        student_name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        subject = random.choice(SUBJECTS)
        score = random.randint(40, 100)
        grade = (
            "A" if score >= 80 else
            "B" if score >= 70 else
            "C" if score >= 60 else
            "D" if score >= 50 else
            "F"
        )
        records.append({
            "Student Name": student_name,
            "Subject": subject,
            "Score": score,
            "Grade": grade,
            "Date Recorded": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return records

# ==============================
# MAIN FUNCTION
# ==============================
def main():
    # Create directory
    os.makedirs(FOLDER_NAME, exist_ok=True)
    csv_path = os.path.join(FOLDER_NAME, CSV_FILE)
    excel_path = os.path.join(FOLDER_NAME, EXCEL_FILE)

    # Generate data
    print(f"🎓 Generating {NUM_RECORDS} student performance records...")
    data = generate_student_records()

    # Write to CSV
    print("📄 Writing CSV file...")
    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Student Name", "Subject", "Score", "Grade", "Date Recorded"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    # Write to Excel
    print("📘 Writing Excel file...")
    wb = Workbook()
    ws = wb.active
    ws.title = "Student Performance"
    ws.append(["Student Name", "Subject", "Score", "Grade", "Date Recorded"])
    for record in data:
        ws.append(list(record.values()))
    wb.save(excel_path)

    print("\n✅ Data generation complete!")
    print(f"📁 Folder: {FOLDER_NAME}")
    print(f"📄 CSV File: {csv_path}")
    print(f"📘 Excel File: {excel_path}")
    print(f"📊 Total Records: {len(data)}")

# ==============================
# RUN SCRIPT
# ==============================
if __name__ == "__main__":
    main()
