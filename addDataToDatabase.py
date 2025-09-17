import os
import json
import firebase_admin

from firebase_admin import credentials, db
from dotenv import load_dotenv   

# Load env variables
load_dotenv()

firebase_key = os.getenv("FIREBASE_KEY")
cred_dict = json.loads(firebase_key)

# private_key ke \n ko actual new line banate hai
cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")


cred = credentials.Certificate(cred_dict)

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face2-62a3a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "10622319": {
        "name": "TUSHAR SHARMA",
        "major": "diploma",
        "starting": "2022",
        "total_attendance": 1,
        "last_attendance_time": "2025-03-16 09:00:00"
    },
    "852741": {
        "name": "Emly",
        "major": "diploma",
        "starting_year": "2022",
        "total_attendance": 6,
        "last_attendance_time": "2025-03-16 09:00:00"
    },
    "963852": {
        "name": "Elon",
        "major": "diploma",
        "starting": "2022",
        "total_attendance": 9,
        "last_attendance_time": "2025-03-16 09:00:00"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
