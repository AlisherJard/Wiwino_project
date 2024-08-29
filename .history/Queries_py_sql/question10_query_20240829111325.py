# Import the necessary libraries
import csv
import sqlite3

# Connect to the database
connexion = sqlite3.connect("db/vivino.db")
cursor = connexion.cursor()


# A query to get all the vintages ranked in the Vivino's Wine Style Awards
cursor.execute("""
    SELECT
        v.name AS vintage,
        v.year AS vintage_year,
        vtr.rank,
        vtr.previous_rank,
        CAST(SUBSTR(t.name, 10, 4) AS int) AS award_year,
        SUBSTR(t.name, INSTR(t.name, ':')+2) AS style_name,
        price_euros,
        bottle_volume_ml
    FROM vintages AS v
    LEFT JOIN vintage_toplists_rankings AS vtr ON v.id = vtr.vintage_id
    LEFT JOIN toplists AS t ON vtr.top_list_id = t.id
    WHERE t.name LIKE 'Vivino%';
""")

# Create a list of lists, data, where the first list contains the column's names.
data = [[item[0] for item in cursor.description]]

# Add the result of the query to the data list row by row.
for item in cursor.fetchall():
    data.append(list(item))

# Create the csv file.
with open('CSVs/question10.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)