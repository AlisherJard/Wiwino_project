import sqlite3
import csv

conn = sqlite3.connect('vivino.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT
        wineries.name,
        AVG(vintages.ratings_average) AS avg_ratings_average,
        SUM(vintages.ratings_count) AS total_ratings_count
    FROM
        vintages
    JOIN
        wineries ON vintages.wine_id = wineries.id
    GROUP BY
        wineries.name
    ORDER BY
        avg_ratings_average DESC, total_ratings_count DESC;
""")
rows = cursor.fetchall()

column_names = [description[0] for description in cursor.description]

with open('CSVs/question3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(column_names)
    csvwriter.writerows(rows)

conn.close()
