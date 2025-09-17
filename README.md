# face662.github.io
Face Attendance System 🏫

The Face Attendance System is a Python-based application that automates student attendance using facial recognition. It eliminates manual attendance, saves time, reduces errors, and ensures accurate records. The system integrates with Firebase Realtime Database for secure, real-time storage of student data.

Features ✅

a) Automatic Attendance Marking: Captures student faces and marks attendance automatically with timestamp if recognized.

b) Database Integration: Each student record has unique ID, name, major, starting year, total attendance, and last attendance timestamp.

c) Secure Credential Handling: Sensitive files (.env, Firebase service keys) are never uploaded to GitHub.

d) Modular & Maintainable: Code split into separate scripts for encoding generation, database operations, and main application logic.

e) Testing Scripts: Includes database_test.py to validate database entries without secrets.
Project Structure 🗂️
face_attendance/
│
├── images/                 # Static images of students
├── encodefile/             # Encodings for faces
├── resource/               # Additional resources
│
├── addDatatodatabase.py    # Firebase database scripts
├── database_test.py        # Testing scripts
├── encodegenerator.py      # Encoding generation
├── main.py                 # Main application logic
├── test_env.py             # Environment variable testing
├── README.md               # Project instructions
├── requirements.txt        # Dependencies
└── .gitignore       
1. Installation & Setup ⚙️
Clone the Repository
git clone https://github.com/yourusername/face662.github.io.git
cd face662.github.io
2. Create Virtual Environment
python -m venv .venv
3 Activate Virtual Environment
# Windows PowerShell
.venv\Scripts\Activate.ps1
4 Install Dependencies
pip install -r requirements.txt
5. Set Up Firebase Credentials
Store your Firebase service key in .env (not uploaded to GitHub)
Example .env:
FIREBASE_KEY=<YOUR_FIREBASE_SERVICE_KEY_JSON>
6. Run the Application
python main.py
Summary 📝
a) This project showcases:
b) Practical Python programming
c) Firebase database integration
d) Real-time data handling
e) Secure management of credentials
f) Modular code structure suitable for maintenance or upgrades






















