import sqlite3
import csv

connection = sqlite3.connect('/home/siegfried2021/Bureau/BeCode_AI/Projets/Wiwino_project/WiwinoDB.session.sql')
cursor = connection.cursor()

query_4 = """
    WITH selection AS (
        SELECT wines.name AS wine_name,
        'Subtly aphrodisiac flavour' AS group_name, wines.region_id AS region
        FROM wines
        JOIN keywords_wine ON wines.id = keywords_wine.wine_id   
        RIGHT JOIN keywords ON keywords_wine.keyword_id = keywords.id
        WHERE keywords.name IN ('coffee', 'toast', 'green apple', 'cream', 'citrus')
        AND keywords_wine.count >= 10
        GROUP BY wines.name
        HAVING COUNT(DISTINCT keywords.name) = 5
        ORDER BY wine_name
        )
        SELECT selection.wine_name, selection.group_name, countries.name
        FROM selection
        INNER JOIN regions ON selection.region = regions.id
        INNER JOIN countries ON regions.country_code = countries.code
        ORDER BY countries.name;
"""

cursor.execute(query_5)
results = cursor.fetchall()

csv_file_path = 'question4.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['wine_name', 'group_name', 'country'])
    
    # Write the data rows
    writer.writerows(results)
