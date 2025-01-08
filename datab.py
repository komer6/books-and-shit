# import sqlite3
# import pandas as pd
# import os

# # Path to your SQLite database
# db_path = r'C:\Users\komer\Desktop\projectlibary\instance\books.db'
# json_path = 'book.json'

# # Check if the database file exists
# if not os.path.exists(db_path):
#     print(f"The database file does not exist: {db_path}")
# else:
#     conn = None
#     try:
#         # Connect to the database
#         conn = sqlite3.connect(db_path)
        
#         # Query the 'book' table into a pandas DataFrame
#         query = "SELECT * FROM book"
#         df = pd.read_sql_query(query, conn)
        
#         # Export the DataFrame to a JSON file
#         df.to_json(json_path, orient='records', indent=4, force_ascii=False)
        
#         print(f"Data from table 'book' has been exported to '{json_path}' successfully.")

#     except sqlite3.Error as e:
#         print(f"Error: {e}")

#     finally:
#         if conn:
#             conn.close()
from app import db
with app.app_context():
    db.create_all()  # Create tables
