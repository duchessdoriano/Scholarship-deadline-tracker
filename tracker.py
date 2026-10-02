import csv
from datetime import datetime

FILENAME = "scholarships.csv"


def view_scholarships():
    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        if not rows:
            print("No scholarships tracked yet.")
            return

        for row in rows:
            deadline_date = datetime.strptime(row['deadline'], "%Y-%m-%d")
            days_left = (deadline_date - datetime.today()).days           
            print("-" * 40)
            print(f"University: {row['university']}")
            print(f"Days remaining: {days_left}")
            print(f"Status: {row['status']}")
                  



def add_scholarship():
    print("Enter the scholarship details below:")
    new_entry = {
        "university": input("University: "),
        "country": input("Country: "),
        "scholarship_type": input("Scholarship type: "),
        "deadline": input("Deadline (YYYY-MM-DD): "),
        "application_fee": input("Application fee: "),
        "required_documents": input("Required documents: "),
        "status": "Not Started"
    }

    with open(FILENAME, mode="a", newline="") as file:
        fieldnames = ["university", "country", "scholarship_type", "deadline",
                      "application_fee", "required_documents", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_entry)

    print("Scholarship added successfully!")

def update_status():
    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No scholarships tracked yet.")
        return

    for i, row in enumerate(rows):
        print(f"{i + 1}. {row['university']} - Current status: {row['status']}")

    choice = int(input("Enter the number of the scholarship to update: ")) - 1

    if choice < 0 or choice >= len(rows):
        print("Invalid selection.")
        return

    new_status = input("Enter new status (Not Started / In Progress / Submitted): ")
    rows[choice]['status'] = new_status

    fieldnames = ["university", "country", "scholarship_type", "deadline",
                  "application_fee", "required_documents", "status"]

    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Status updated successfully!")

#add_scholarship()
#view_scholarships()
def main_menu():
    while True:
        print("1. View scholarships")
        print("2. Add a new scholarship")
        print("3. Update scholarship status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_scholarships()
        elif choice == "2":
            add_scholarship()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


main_menu()