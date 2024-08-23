import sqlite3
import csv

conn = sqlite3.connect('vivino.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT
        wineries.name,ratings_average, vintages.ratings_count
    FROM
        vintages
    JOIN
        wineries ON vintages.wine_id = wineries.id
    WHERE
        vintages.ratings_average               
    GROUP BY 
        wineries.name
    
    ORDER BY
        ratings_average DESC, ratings_count DESC
    
;
""")
rows = cursor.fetchall()

column_names = [description[0] for description in cursor.description]

with open('question3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(column_names)
    csvwriter.writerows(rows)

conn.close()
