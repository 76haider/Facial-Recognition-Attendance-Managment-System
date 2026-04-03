import streamlit as st
import pandas as pd
from datetime import datetime
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Face Recognition Attendance System", layout="wide")

# Initialize all session state
if 'students' not in st.session_state:
    st.session_state.students = pd.DataFrame([
        ['ST001', 'John Doe', 'Computer Science', 'encoded_1', 'john@example.com', '1234567890'],
        ['ST002', 'Jane Smith', 'Computer Science', 'encoded_2', 'jane@example.com', '1234567891'],
        ['ST003', 'Mike Johnson', 'Electrical Engineering', 'encoded_3', 'mike@example.com', '1234567892'],
    ], columns=['Student ID', 'Name', 'Department', 'Face Encoding', 'Email', 'Phone'])

if 'attendance' not in st.session_state:
    st.session_state.attendance = pd.DataFrame(columns=['Student ID', 'Name', 'Department', 'Date', 'Time'])

if 'departments' not in st.session_state:
    st.session_state.departments = pd.DataFrame([
        ['CS', 'Computer Science', 'Dr. Smith', 'hod.cs@example.com'],
        ['EC', 'Electrical Engineering', 'Dr. Jones', 'hod.ec@example.com'],
    ], columns=['Dept ID', 'Dept Name', 'HOD Name', 'HOD Email'])

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Sidebar Navigation
st.sidebar.title("📋 Menu")
menu = st.sidebar.radio("Navigate", [
    "🏠 Home", 
    "👨‍💼 Admin Login", 
    "📸 Give Attendance", 
    "📊 Attendance List",
    "📝 Student Registration"
])

# Home Page
if menu == "🏠 Home":
    st.title("🎓 Facial Recognition Based Attendance System")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", len(st.session_state.students))
    with col2:
        st.metric("Total Departments", len(st.session_state.departments))
    with col3:
        today = datetime.now().strftime("%Y-%m-%d")
        today_count = len(st.session_state.attendance[st.session_state.attendance['Date'] == today])
        st.metric("Today's Attendance", today_count)
    
    st.info("""
    ### ✨ System Features:
    - **Real-time Face Recognition** - Automatic student identification
    - **Automated Attendance** - Timestamped records
    - **Department Management** - Organize by departments
    - **Student Registration** - Easy enrollment
    - **Report Generation** - Export attendance data
    """)
    
    st.success("✅ System is operational and ready")

# Admin Login
elif menu == "👨‍💼 Admin Login":
    st.title("Admin Login")
    
    if not st.session_state.logged_in:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login", use_container_width=True):
            if username == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.success("✅ Login Successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
    else:
        st.success(f"✅ Logged in as Admin")
        
        # Admin Panel
        st.subheader("🔧 Admin Control Panel")
        
        admin_tab1, admin_tab2, admin_tab3 = st.tabs(["🏛️ Department Management", "👨‍🎓 Student Management", "📧 Generate Reports"])
        
        # Department Management Tab
        with admin_tab1:
            st.write("### Add New Department")
            col1, col2 = st.columns(2)
            with col1:
                dept_id = st.text_input("Department ID (e.g., CS)")
                dept_name = st.text_input("Department Name")
            with col2:
                hod_name = st.text_input("HOD Name")
                hod_email = st.text_input("HOD Email")
            
            if st.button("➕ Add Department"):
                if dept_id and dept_name:
                    new_dept = pd.DataFrame([[dept_id, dept_name, hod_name, hod_email]], 
                                           columns=['Dept ID', 'Dept Name', 'HOD Name', 'HOD Email'])
                    st.session_state.departments = pd.concat([st.session_state.departments, new_dept], ignore_index=True)
                    st.success(f"✅ Department {dept_name} added!")
                    st.rerun()
            
            st.write("### Existing Departments")
            st.dataframe(st.session_state.departments, use_container_width=True)
        
        # Student Management Tab
        with admin_tab2:
            st.write("### Register New Student")
            col1, col2 = st.columns(2)
            with col1:
                new_student_id = st.text_input("Student ID")
                new_name = st.text_input("Full Name")
                new_email = st.text_input("Email")
            with col2:
                new_department = st.selectbox("Department", st.session_state.departments['Dept Name'].tolist())
                new_phone = st.text_input("Phone Number")
                admission_year = st.number_input("Admission Year", min_value=2000, max_value=2030, value=2024)
            
            if st.button("📝 Register Student"):
                if new_student_id and new_name:
                    new_student = pd.DataFrame([[new_student_id, new_name, new_department, f"encoded_{new_student_id}", new_email, new_phone]],
                                              columns=['Student ID', 'Name', 'Department', 'Face Encoding', 'Email', 'Phone'])
                    st.session_state.students = pd.concat([st.session_state.students, new_student], ignore_index=True)
                    st.success(f"✅ Student {new_name} registered! ID: {new_student_id}")
                    st.balloons()
                    st.rerun()
            
            st.write("### All Students")
            st.dataframe(st.session_state.students[['Student ID', 'Name', 'Department', 'Email']], use_container_width=True)
            
            # Remove student
            st.write("### Remove Student")
            student_to_remove = st.selectbox("Select Student to Remove", st.session_state.students['Name'].tolist())
            if st.button("🗑️ Remove Student", type="secondary"):
                st.session_state.students = st.session_state.students[st.session_state.students['Name'] != student_to_remove]
                st.success(f"✅ Student {student_to_remove} removed!")
                st.rerun()
        
        # Reports Tab
        with admin_tab3:
            st.write("### Generate Attendance Report")
            
            if len(st.session_state.attendance) > 0:
                # Date range filter
                col1, col2 = st.columns(2)
                with col1:
                    start_date = st.date_input("Start Date")
                with col2:
                    end_date = st.date_input("End Date")
                
                # Filter attendance
                mask = (pd.to_datetime(st.session_state.attendance['Date']) >= pd.to_datetime(start_date)) & \
                       (pd.to_datetime(st.session_state.attendance['Date']) <= pd.to_datetime(end_date))
                filtered = st.session_state.attendance[mask]
                
                st.write(f"### Report for {start_date} to {end_date}")
                st.dataframe(filtered, use_container_width=True)
                
                # Download button
                csv = filtered.to_csv(index=False)
                st.download_button("📥 Download Report (CSV)", csv, f"attendance_{start_date}_to_{end_date}.csv", "text/csv")
                
                # Summary stats
                st.write("### Summary Statistics")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Records", len(filtered))
                with col2:
                    st.metric("Unique Students", filtered['Student ID'].nunique() if len(filtered) > 0 else 0)
                with col3:
                    st.metric("Departments", filtered['Department'].nunique() if len(filtered) > 0 else 0)
            else:
                st.info("No attendance records yet")
        
        # Logout button
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

# Give Attendance
elif menu == "📸 Give Attendance":
    st.title("Mark Attendance")
    st.markdown("Position your face clearly in front of the camera")
    
    camera_image = st.camera_input("📷 Capture Face", key="attendance_camera")
    
    if camera_image is not None:
        # Display captured image
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(camera_image, caption="Captured Face", width=300)
        
        # Simulate face recognition
        with col2:
            st.write("### Recognition Result")
            
            # Get list of students for selection (simulating recognition)
            student_names = st.session_state.students['Name'].tolist()
            
            # In real system, this would be automatic. For demo, admin confirms.
            matched_student = st.selectbox("Matched Student (simulated recognition)", student_names)
            
            if st.button("✅ Confirm & Mark Attendance", use_container_width=True):
                student_data = st.session_state.students[st.session_state.students['Name'] == matched_student].iloc[0]
                now = datetime.now()
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%H:%M:%S")
                
                # Check if already marked today
                already_marked = st.session_state.attendance[
                    (st.session_state.attendance['Student ID'] == student_data['Student ID']) & 
                    (st.session_state.attendance['Date'] == date_str)
                ]
                
                if len(already_marked) == 0:
                    new_entry = pd.DataFrame([[
                        student_data['Student ID'],
                        student_data['Name'],
                        student_data['Department'],
                        date_str,
                        time_str
                    ]], columns=['Student ID', 'Name', 'Department', 'Date', 'Time'])
                    
                    st.session_state.attendance = pd.concat([st.session_state.attendance, new_entry], ignore_index=True)
                    st.success(f"✅ Attendance marked for {matched_student} at {time_str}")
                    st.balloons()
                else:
                    st.warning(f"⚠️ {matched_student} already marked attendance today")

# Attendance List
elif menu == "📊 Attendance List":
    st.title("Attendance Records")
    
    if len(st.session_state.attendance) > 0:
        # Filters
        col1, col2 = st.columns(2)
        with col1:
            unique_dates = st.session_state.attendance['Date'].unique()
            selected_date = st.selectbox("Filter by Date", ["All"] + list(unique_dates))
        with col2:
            unique_depts = st.session_state.attendance['Department'].unique()
            selected_dept = st.selectbox("Filter by Department", ["All"] + list(unique_depts))
        
        # Apply filters
        filtered_df = st.session_state.attendance.copy()
        if selected_date != "All":
            filtered_df = filtered_df[filtered_df['Date'] == selected_date]
        if selected_dept != "All":
            filtered_df = filtered_df[filtered_df['Department'] == selected_dept]
        
        st.dataframe(filtered_df, use_container_width=True)
        
        # Download
        csv = filtered_df.to_csv(index=False)
        st.download_button("📥 Download Full Report", csv, "attendance_report.csv", "text/csv")
        
        # Summary
        st.subheader("📊 Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Records", len(st.session_state.attendance))
        with col2:
            st.metric("Today's Records", len(st.session_state.attendance[st.session_state.attendance['Date'] == datetime.now().strftime("%Y-%m-%d")]))
        with col3:
            st.metric("Unique Students", st.session_state.attendance['Student ID'].nunique())
    else:
        st.info("📭 No attendance records found")

# Student Registration
elif menu == "📝 Student Registration":
    st.title("Student Self Registration")
    
    with st.form("self_registration"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name *")
            email = st.text_input("Email *")
            phone = st.text_input("Phone Number")
        with col2:
            student_id = st.text_input("Student ID *")
            department = st.selectbox("Department", st.session_state.departments['Dept Name'].tolist())
            admission_year = st.number_input("Admission Year", min_value=2000, max_value=2030, value=2024)
        
        st.write("### Capture Your Face for Registration")
        face_image = st.camera_input("Look straight into camera", key="registration_camera")
        
        submitted = st.form_submit_button("Submit Registration", use_container_width=True)
        
        if submitted:
            if name and student_id and email:
                # Check if student ID already exists
                if student_id in st.session_state.students['Student ID'].values:
                    st.error("❌ Student ID already exists!")
                else:
                    new_student = pd.DataFrame([[student_id, name, department, f"encoded_{student_id}", email, phone]],
                                              columns=['Student ID', 'Name', 'Department', 'Face Encoding', 'Email', 'Phone'])
                    st.session_state.students = pd.concat([st.session_state.students, new_student], ignore_index=True)
                    st.success(f"✅ Registration successful! Your ID is {student_id}")
                    st.info("📧 A confirmation email would be sent to your registered email (simulated)")
                    st.balloons()
            else:
                st.error("❌ Please fill all required fields (*)")