import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the MySQL database
engine = create_engine("mysql+mysqlconnector://TimPC:Badpass123@192.168.86.169/test")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Execute a SELECT query
query = text("SELECT * FROM aqi")
result = session.execute(query)

# Define the path and name of the CSV file
csv_file = "output.csv"

# Write the result to a CSV file
with open(csv_file, "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(result.keys())  # Write the column headers
    csv_writer.writerows(result)  # Write the data rows


# Close the session
session.close()
