import os
import sqlite3
from xml.dom import minidom

db_path = 'C:/Users/kras2/PycharmProjects/5Individual'
db_file = 'db01.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Data</title>
        </head>
        <h1> Data export successful</h1>""")

xmldoc = minidom.parse('book.xml')
a_list = xmldoc.getElementsByTagName()

cur.close()
con.close()
