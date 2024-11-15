import streamlit as st
import pandas as pd
from datetime import datetime

# CSV file where the data will be stored
csv_file = "leave_applications.csv"

# Streamlit Leave Application Form
st.title("Leave Application Form")

# Form fields for the leave application
with st.form("leave_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    department = st.selectbox("Department", ["HR", "Supervising", "Engineering", "Duty - type 1", "Canteen", "Other"])
    
    leave_type = st.selectbox("Type of Leave", ["Sick Leave", "Casual Leave", "Vacation", "Maternity Leave", "Other"])
    leave_start = st.date_input("Leave Start Date", datetime.today())
    leave_end = st.date_input("Leave End Date", datetime.today())
    
    reason = st.text_area("Reason for Leave")

    # Submit button
    submitted = st.form_submit_button("Submit Application")
    
    # Processing the submitted form
    if submitted:
        if not name or not email:
            st.error("Please fill out all required fields (Name, Email).")
        else:
            # Display the submitted data
            st.success(f"Leave Application Submitted Successfully by {name}")
            st.write(f"**Email**: {email}")
            st.write(f"**Department**: {department}")
            st.write(f"**Leave Type**: {leave_type}")
            st.write(f"**Leave Period**: From {leave_start} to {leave_end}")
            st.write(f"**Reason for Leave**: {reason}")
            
            # Create a dictionary for the form data
            form_data = {
                "Name": [name],
                "Email": [email],
                "Department": [department],
                "Leave Type": [leave_type],
                "Leave Start": [leave_start],
                "Leave End": [leave_end],
                "Reason for Leave": [reason]
            }
            
            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame(form_data)
            
            # Append the new data to the CSV file (create if it doesn't exist)
            try:
                df.to_csv(csv_file, mode='a', header=not pd.read_csv(csv_file).empty, index=False)
            except FileNotFoundError:
                df.to_csv(csv_file, mode='a', header=True, index=False)

            st.write("Data saved to CSV file successfully.")
            st.table(df)