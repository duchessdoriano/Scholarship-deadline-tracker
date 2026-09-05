import csv

FILENAME = "scholarships.csv"


def view_scholarships():
    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        if not rows:
            print("No scholarships tracked yet.")
            return

        for row in rows:
            print("-" * 40)
            print(f"University: {row['university']}")
            print(f"Status: {row['status']}")


view_scholarships()