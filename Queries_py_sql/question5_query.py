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
""")

# Create a list of lists, data_01, where the first list contains the column's names.
data_01 = [[item[0] for item in cursor.description]]

# Add the result of the query to the data_01 list row by row.
for item in cursor.fetchall():
    data_01.append(list(item))

# Create the csv file.
with open('CSVs/top_grapes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data_01)


# Query the wine name containing one of the following string:
# 'Cabernet Sauvignon', 'Merlot', and 'Chardonnay'
# whose are the top three grapes used in the most countries
cursor.execute("""
    SELECT
        w.name AS wine_name,
        v.year,
        CASE WHEN w.name LIKE '%Cabernet Sauvignon%' THEN 'Cabernet Sauvignon'
             WHEN w.name LIKE '%Merlot%' THEN 'Merlot'
             WHEN w.name LIKE '%Chardonnay%' THEN 'Chardonnay'
             END AS grape_name,
        w.ratings_average,
        w.ratings_count,
        r.name AS region,
        c.name AS country
    FROM wines AS w
    INNER JOIN vintages AS v ON w.id = v.wine_id
    LEFT JOIN regions AS r ON w.region_id = r.id
    LEFT JOIN countries AS c ON r.country_code = c.code
    WHERE w.name LIKE '%Cabernet Sauvignon%'
        OR w.name LIKE '%Merlot%'
        OR w.name LIKE '%Chardonnay%'
    ORDER BY w.ratings_average DESC, w.ratings_count DESC;
""")

# Create a list of lists, data_02, where the first list contains the column's names.
data_02 = [[item[0] for item in cursor.description]]

# Add the result of the query to the data_02 list row by row.
for item in cursor.fetchall():
    data_02.append(list(item))

# Create the csv file.
with open('CSVs/question5.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data_02)