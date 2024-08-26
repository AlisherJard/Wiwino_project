# Import the necessary libraries
import csv
import sqlite3

# Connect to the database
connexion = sqlite3.connect("db/vivino.db")
cursor = connexion.cursor()

cursor.execute("""
        SELECT 
               w.name AS wine_name, 
               v.name AS vintage_name,
               v.year AS vintage_year,
               w.ratings_average AS wine_ratings_average,
               w.ratings_count AS wine_ratings_count,
               v.ratings_average AS vintage_ratings_average,
               v.ratings_count AS vintage_rating_count,
               (v.price_euros/v.bottle_volume_ml)*1000 AS liter_price_euros,
               -- A case statement to see if a vintage wine is in a top list ranking
               CASE WHEN vtr.vintage_id IS NOT NULL THEN TRUE
                    ELSE FALSE 
               END AS in_top_list,
               c.name AS country
        FROM wines AS w
        INNER JOIN vintages AS v ON w.id = v.wine_id
        LEFT JOIN regions AS r ON w.region_id = r.id
        LEFT JOIN countries AS c ON r.country_code = c.code
        LEFT JOIN vintage_toplists_rankings AS vtr ON v.id = vtr.vintage_id;
""")

# Create a list of lists, data, where the first list contains the column's names.
data = [[item[0] for item in cursor.description]]

# Add the result of the query to the data list row by row.
for item in cursor.fetchall():
    data.append(list(item))

# Create the csv file.
with open('CSVs/query_01.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)