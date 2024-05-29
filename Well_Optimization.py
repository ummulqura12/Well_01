import threading

# Function to insert rows with a delay of 10 seconds
def insert_rows_with_delay(rows, delay=10):
    for row in rows:
        threading.Thread(target=insert_row_to_db, args=(row,)).start()
        time.sleep(delay)

# Start the insertion process
insert_rows_with_delay(all_values)
