# 🎓 Facial Recognition Based Attendance System

A simplified attendance management system deployed on Streamlit Cloud that allows admins to manage students and mark attendance efficiently. The system currently uses manual selection instead of real-time facial recognition for cloud compatibility.

---

## 🎯 Overview

The **Facial Recognition Based Attendance System** is a streamlined solution designed to manage attendance in educational institutions. This deployed version focuses on simplicity and accessibility by replacing complex ML-based recognition with a manual selection system while still maintaining structured attendance tracking and reporting.

### Key Highlights

* ✅ **Admin Login System** for secure access
* ✅ **Department-wise Student Management**
* ✅ **Manual Attendance Marking** via dropdown selection
* ✅ **Automatic Timestamp Logging**
* ✅ **Duplicate Attendance Prevention (Same Day)**
* ✅ **Attendance Filtering & Reports**
* ✅ **CSV Export सुविधा** for attendance data

---

## ✨ Features

### 👨‍💼 Admin Features

* **Secure Admin Authentication**: Simple login using username and password
* **Department Management**: Add and manage departments
* **Student Management**:

  * Add new students with details (name, ID, email, phone, department)
  * View all registered students
  * Remove students from the system
* **Attendance Reports**: Filter attendance by date and department and download as CSV

### 📸 Attendance Features

* **Manual Attendance Selection**: Select student from dropdown
* **Automatic Attendance Logging**: Records attendance with timestamp
* **Duplicate Prevention**: Prevents multiple attendance entries on the same day
* **Attendance List View**: View and filter attendance records

### 📧 Notification System

* ❌ Email notifications removed in deployed version
* ❌ No automated communication features

---

## 🛠 Technology Stack

### Frontend

* **Streamlit**: Web application framework for UI and deployment

### Backend

* **Python 3.8+**

### Data Handling

* **Pandas**: Data manipulation and reporting
* **NumPy**: Numerical operations

### Deployment

* **Streamlit Cloud**: Hosting platform

---

## 🏗 System Architecture

| **1. Student Registration**                                                   |
| ----------------------------------------------------------------------------- |
| <img src="IMAGES\01.png" width="1200" height="600" style="object-fit:cover;"> |

| **2. Give Attendance**                                                        |
| ----------------------------------------------------------------------------- |
| <img src="IMAGES\02.png" width="1200" height="600" style="object-fit:cover;"> |

| **3. Generate Attendance Report**                                             |
| ----------------------------------------------------------------------------- |
| <img src="IMAGES\03.png" width="1200" height="600" style="object-fit:cover;"> |

---

## 🏗 Database Architecture

| **1. In-Memory Storage (Session State)**                                      |
| ----------------------------------------------------------------------------- |
| <img src="IMAGES\04.png" width="1200" height="600" style="object-fit:cover;"> |

| **2. No Vector Database (Removed)**                                           |
| ----------------------------------------------------------------------------- |
| <img src="IMAGES\06.png" width="1200" height="600" style="object-fit:cover;"> |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* **pip**
* **Git**
* **Virtual Environment (venv or conda)**

### Required Accounts

* **Streamlit Cloud Account** (for deployment)

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/76haider/Facial-Recognition-Attendance-Managment-System
cd Facial-Recognition-Attendance-Managment-System
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

venv\Scripts\activate       # On Windows

source venv/bin/activate    # On macOS/Linux:
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Requirements include:**

* streamlit
* pandas
* numpy

---

## ⚙️ Configuration

### 1. Application Setup

No external database or API setup required.

* The system uses **Streamlit session state** for storing:

  * Students
  * Departments
  * Attendance records

### 2. Admin Credentials

```text
Username: admin
Password: admin
```

---

## 📁 Project Structure

```
Facial-Recognition-Attendance-Managment-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── UI/
│   ├── Admin_login.py
│   ├── Admin_dashboard.py
│   ├── Add_student.py
│   ├── Manage_students.py
│   ├── Attendance.py
│   └── Reports.py
│
├── IMAGES/
└── LICENSE
```

---

## 🎮 Usage

### Starting the Application

```bash
streamlit run app.py
```

Or access the live app:

👉 [https://76haiderkhan-facial-recognition-attendance-managment-system.streamlit.app/](https://76haiderkhan-facial-recognition-attendance-managment-system.streamlit.app/)

---

### Admin Workflow

1. **Login** using admin credentials
2. **Manage Departments**
3. **Add Students** with required details
4. **Mark Attendance** using dropdown selection
5. **View Attendance Records**
6. **Download Reports** as CSV

---

### Student Attendance Workflow

1. Navigate to **Attendance Page**
2. Select student from dropdown
3. Click **Mark Attendance**
4. Attendance is logged with timestamp
5. Duplicate entries are prevented

---

## 🔑 Key Modules

### Student Management

* Add, view, and delete students
* Assign students to departments

### Attendance System

* Manual selection-based attendance
* Timestamp logging
* Duplicate prevention

### Reporting

* Filter attendance by date and department
* Export attendance as CSV

---

## 💾 Database Schema

### Students (Session State)

* Student ID
* Name
* Email
* Phone
* Department

### Departments

* Department ID
* Department Name

### Attendance Log

* Date
* Student ID
* Department
* Timestamp

---

## 🔗 API Integration

❌ No external APIs used in deployed version

---

## 🔒 Security

* Basic authentication system
* Session-based data handling
* No external API keys required

---

## 🐛 Troubleshooting

### Common Issues

**1. App Not Loading**

* Check Streamlit Cloud status
* Restart app

**2. Data Reset Issue**

* Session state resets on refresh
* This is expected behavior

**3. Import Errors**

* Ensure dependencies are installed
* Use Python 3.8+

---

## 🖼️ Screenshots

*(All screenshots remain same as UI reference)*

[Keep all existing image sections unchanged]

---

## 📊 Project Status

✅ **Deployed & Functional (Simplified Version)**

### Roadmap

* [ ] Reintroduce facial recognition
* [ ] Database integration (Supabase/Firebase)
* [ ] Email notifications
* [ ] Persistent storage
* [ ] Mobile optimization

---

## 🙏 Acknowledgments

* **Streamlit**: For the web framework
* **Python Community**: For open-source libraries

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Project Maintainer**: [Haider Khan]

* 📧 Email: [haiderkhaan0800@gmail.com](mailto:haiderkhaan0800@gmail.com)
* 🐙 GitHub: [https://github.com/76haider](https://github.com/76haider)
* 💼 LinkedIn: [https://linkedin.com/in/76haiderkhan](https://linkedin.com/in/76haiderkhan)

**Project Link**:
[https://github.com/76haider/Facial-Recognition-Attendance-Managment-System](https://github.com/76haider/Facial-Recognition-Attendance-Managment-System)

---

**⭐ If you find this project helpful, please consider giving it a star ⭐**

---

*Last Updated: April 2026*
