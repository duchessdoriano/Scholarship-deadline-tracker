import streamlit as st
import pandas as pd
from datetime import datetime
import csv

FILENAME = "scholarships.csv"

STATUS_OPTIONS = [
    "Not Started",
    "Researching",
    "Documents Pending",
    "Ready to Apply",
    "Applied",
    "Accepted",
    "Rejected",
]

st.title("Scholarship Deadline Tracker")

# ----- Add a new scholarship -----
st.header("Add a New Scholarship")

with st.form("add_scholarship_form", clear_on_submit=True):
    university = st.text_input("University")
    country = st.text_input("Country")
    scholarship_type = st.text_input("Scholarship type")
    deadline = st.date_input("Deadline")
    application_fee = st.text_input("Application fee")
    required_documents = st.text_input("Required documents")
    status = st.selectbox("Status", STATUS_OPTIONS)

    submitted = st.form_submit_button("Add Scholarship")

    if submitted:
        if not university.strip():
            st.error("University name cannot be empty.")
        elif not country.strip():
            st.error("Country cannot be empty.")
        elif not application_fee.strip().replace(".", "", 1).isdigit() and application_fee.strip().lower() != "free":
            st.error("Application fee must be a number (or 'Free').")
        else:
            new_entry = {
                "university": university,
                "country": country,
                "scholarship_type": scholarship_type,
                "deadline": deadline.strftime("%Y-%m-%d"),
                "application_fee": application_fee,
                "required_documents": required_documents,
                "status": status
            }

            fieldnames = ["university", "country", "scholarship_type", "deadline",
                          "application_fee", "required_documents", "status"]

            with open(FILENAME, mode="a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(new_entry)

            st.success("Scholarship added successfully!")
            st.rerun()

# ----- View scholarships -----
st.header("Your Tracked Scholarships")

df = pd.read_csv(FILENAME)

df["deadline"] = pd.to_datetime(df["deadline"])
df["days_remaining"] = (df["deadline"] - datetime.today()).dt.days

df = df.sort_values("days_remaining").reset_index(drop=True)

st.write("Sorted by urgency:")
st.dataframe(df)