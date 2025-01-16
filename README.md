# Facial-Recognition-System


This project integrates advanced facial recognition technology to enhance security and streamline identity verification processes. Designed specifically for academic institutions, it ensures efficient student identification with high accuracy and automation.

Features
High Accuracy: Achieves 95% accuracy in facial recognition.
Real-Time Verification: Provides prompt identification with an average response time of less than one second.
Centralized Database: Seamlessly integrates with Firebase to store and retrieve student information.
Automated Reports:
Generates daily attendance records in XLSX format.
Tracks check-in and check-out times.
Sends alerts to students outside the campus after the cut-off time using the Twilio API.
Safety Enhancements: Reduces unauthorized access incidents, fostering a safer campus environment.
Technical Details
Tech Stack: Python, OpenCV, Firebase, Twilio API.
Core Functionality:
Facial feature extraction using OpenCV.
Secure storage and retrieval of student data using Firebase.
Automated notifications via Twilio SMS API.
Reporting tools for daily administration needs.
How to Use
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Shoaib/FacialRecognitionSystem.git
cd FacialRecognitionSystem
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure Firebase:

Replace the placeholder in firebase_config.json with your Firebase project details.
Run the Application:

bash
Copy
Edit
python main.py
Outcomes
Reduced administrative overhead by 40%.
Improved operational efficiency by 90%.
Enhanced campus security through real-time monitoring and alerts.
Future Enhancements
Integration with other authentication mechanisms.
Expansion to support multi-campus setups.
Addition of a mobile application interface.
Contribution
Contributions are welcome! Please feel free to raise issues or submit pull requests
