# readStudentsFromFirebase.py

import os
import json
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
from tabulate import tabulate  # Optional, for pretty table output

# Load environment variables
load_dotenv()

# Get Firebase key and fix newlines in private key
firebase_key = os.getenv("FIREBASE_KEY")
cred_dict = json.loads(firebase_key)
cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")

# Initialize Firebase app
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face2-62a3a-default-rtdb.firebaseio.com/"
})

# Reference to Students node
ref = db.reference('Students')

# Read data from Firebase
students_data = ref.get()

# Check if there is any data
if not students_data:
    print("No student data found in Firebase.")
else:
    # Prepare data for table printing
    table = []
    headers = ["ID", "Name", "Major", "Starting Year", "Total Attendance", "Last Attendance Time"]

    for student_id, info in students_data.items():
        row = [
            student_id,
            info.get("name", ""),
            info.get("major", ""),
            info.get("starting", info.get("starting_year", "")),
            info.get("total_attendance", ""),
            info.get("last_attendance_time", "")
        ]
        table.append(row)

    # Print table
    print(tabulate(table, headers=headers, tablefmt="grid"))
