import csv
import MySQLdb
import time

# Open the CSV file and read the data
with open('WELL.csv', newline='') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    
    # Skip the header row
    next(csvfile)
    
    all_values = []
    for row in csvfile:
        # Ensure the row has the expected number of columns and is not empty
        if len(row) == 11 and all(row):
            value = tuple(row)  # Convert row to a tuple directly
            all_values.append(value)

# Function to insert a row into the database and print the execution time
def insert_row_to_db(row):
    start_time = time.time()
    mydb = MySQLdb.connect(host="localhost", user="root", passwd="", db="well")
    query = """INSERT INTO well1 (Date_Time, X1, X2, X3, X4, X5, Y1, Y2, Y3, Y4, Y5) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    mycursor = mydb.cursor()
    mycursor.execute(query, row)
    mydb.commit()
    mycursor.close()
    mydb.close()
    end_time = time.time()
    print(f"Execution time for inserting a row: {end_time - start_time} seconds")


