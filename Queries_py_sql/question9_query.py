import sqlite3
import csv

connection = sqlite3.connect('/home/siegfried2021/Bureau/BeCode_AI/Projets/Wiwino_project/vivino.db')
cursor = connection.cursor()

query_10 = """
    SELECT vintages.name AS group_name, wines.name AS wine_name, wines.acidity, wines.intensity, wines.sweetness, wines.tannin, (price_euros / bottle_volume_ml * 1000) AS price_euros_liter
    FROM vintages
    JOIN wines ON vintages.wine_id = wines.id
"""

cursor.execute(query_10)
results = cursor.fetchall()

csv_file_path = 'CSV files/question9.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['group_name', 'wine_name', 'acidity', 'intensity', 'sweetness', 'tannin', 'price_euros_liter'])
    
    writer.writerows(results)