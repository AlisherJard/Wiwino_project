# Import the necessary libraries
import csv
import sqlite3

# Connect to the database
connexion = sqlite3.connect("db/vivino.db")
cursor = connexion.cursor()


# A query to get the wine name containing the string 'Cabernet Sauvignon'
cursor.execute("""
    SELECT
        w.name AS wine_name,
        v.year,
        w.ratings_average,
        w.ratings_count,
        (v.price_euros/v.bottle_volume_ml)*1000 AS liter_price_euros,
        c.name AS country
    FROM wines AS w
    INNER JOIN vintages AS v ON w.id = v.wine_id
    LEFT JOIN regions AS r ON w.region_id = r.id
    LEFT JOIN countries AS c ON r.country_code = c.code
    WHERE w.name LIKE '%Cabernet Sauvignon%'
    ORDER BY w.ratings_average DESC, w.ratings_count DESC;
""")

# Create a list of lists, data, where the first list contains the column's names.
data = [[item[0] for item in cursor.description]]

# Add the result of the query to the data list row by row.
for item in cursor.fetchall():
    data.append(list(item))

# Create the csv file.
with open('CSVs/question7.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)