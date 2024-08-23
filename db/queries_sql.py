sqlite3 vivino.db
sqlite> .headers on
sqlite> .mode csv
sqlite> .output /Users/alexjones/Desktop/Wiwino_project/db/file.csv
sqlite> SELECT * FROM grapes;
sqlite> .output stdout