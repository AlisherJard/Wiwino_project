# Import the necessary libraries
import csv
import sqlite3

# Connect to the database
connexion = sqlite3.connect("db/vivino.db")
cursor = connexion.cursor()

cursor.execute("""
        SELECT
               w.name AS wine_name,
               s.grape_name AS grape_name,
               w.ratings_average AS wine_ratings_average,
               w.ratings_count AS wine_ratings_count
        FROM wines AS w
        LEFT JOIN regions AS r ON w.region_id = r.id
        LEFT JOIN countries AS c ON r.country_code = c.code
        INNER JOIN
            -- A subquery to get the three most used grapes in the world
            (SELECT
                g.name AS grape_name,
                COUNT(DISTINCT c.name) AS countries_count,
                c.code AS country_code
            FROM most_used_grapes_per_country AS m
            LEFT JOIN grapes AS g
                ON m.grape_id = g.id
            LEFT JOIN countries AS c
                ON m.country_code = c.code
            GROUP BY g.name
            ORDER BY countries_count DESC
            LIMIT 3) AS s
                ON c.code = s.country_code
        ORDER BY wine_ratings_average DESC, wine_ratings_count DESC;
""")

# Create a list of lists, data, where the first list contains the column's names.
data = [[item[0] for item in cursor.description]]

# Add the result of the query to the data list row by row.
for item in cursor.fetchall():
    data.append(list(item))

# Create the csv file.
with open('CSVs/query_05.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)