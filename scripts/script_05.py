# Import the necessary libraries
import csv
import sqlite3

# Connect to the database
connexion = sqlite3.connect("db/vivino.db")
cursor = connexion.cursor()


# A query to get the three most used grapes in the world
cursor.execute("""
    SELECT
        g.name AS grape_name,
        COUNT(DISTINCT m.country_code) AS countries_count
    FROM most_used_grapes_per_country AS m
    LEFT JOIN grapes AS g
        ON m.grape_id = g.id
    GROUP BY g.name
    ORDER BY countries_count DESC
    LIMIT 3
""")

# Create a list of lists, data, where the first list contains the column's names.
data_01 = [[item[0] for item in cursor.description]]

# Add the result of the query to the data list row by row.
for item in cursor.fetchall():
    data_01.append(list(item))

# Create the csv file.
with open('CSVs/top3_grapes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data_01)


# Query the wine name containing one of the following string:
# 'Cabernet Sauvignon', 'Merlot', and 'Chardonnay'
# whose are the top three grapes used in the most countries
cursor.execute("""
    SELECT
        name AS wine_name,
        CASE WHEN name LIKE '%Cabernet Sauvignon%' THEN 'Cabernet Sauvignon'
             WHEN name LIKE '%Merlot%' THEN 'Merlot'
             WHEN name LIKE '%Chardonnay%' THEN 'Chardonnay'
             END AS grape_name,
             ratings_average,
             ratings_count
    FROM wines
    WHERE name LIKE '%Cabernet Sauvignon%'
        OR name LIKE '%Merlot%'
        OR name LIKE '%Chardonnay%'
    ORDER BY ratings_average DESC, ratings_count DESC;
""")

# Create a list of lists, data, where the first list contains the column's names.
data_02 = [[item[0] for item in cursor.description]]

# Add the result of the query to the data list row by row.
for item in cursor.fetchall():
    data_02.append(list(item))

# Create the csv file.
with open('CSVs/query_05.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data_02)