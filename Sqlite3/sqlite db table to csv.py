import sqlite3
import csv

csv_file = open('Batting Style.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ID', 'Type'])


conn = sqlite3.connect('database.sqlite')
curs = conn.cursor()

curs.execute('''select * from Batting_Style''')

rows = curs.fetchall()
for row in rows:
     csv_writer.writerow(row)


csv_file.close()

conn.commit()
conn.close()