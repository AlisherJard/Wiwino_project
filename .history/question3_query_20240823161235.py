import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('vivino.db')
cursor = conn.cursor()

# Execute the SQL query
query = """
    SELECT
        wineries.name,
        wines(wines.ratings_average) AS avg_ratings_average,
        SUM(wines.ratings_count) AS total_ratings_count
    FROM
        wines
    JOIN
        wineries ON wines.wine_id = wineries.name
    GROUP BY
        wineries.name
    ORDER BY
        avg_ratings_average DESC, total_ratings_count DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

# Specify the CSV file path
csv_file_path = 'question3.csv'

# Write the results to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['name', 'avg_ratings_average', 'total_ratings_count'])
    
    # Write the data rows
    writer.writerows(results)

print(f"Data has been written to {csv_file_path}")