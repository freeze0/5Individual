import os
import sqlite3
import xml.dom.minidom

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
        <h1> Data import successful</h1>""")

xmldoc = xml.dom.minidom.parse('C:\\Users\\kras2\\PycharmProjects\\5Individual\\book.xml')
humans = xmldoc.getElementsByTagName('humans')

for human in humans:
    id_human = int(human.getAttribute('id'))
    name = human.getAttribute('name')
    surname = human.getAttribute('surname')
    reason = human.getAttribute('reason')
    a = [id_human, name, surname, reason]
    sql_app = '''INSERT INTO Human(id, name, surname, reason) VALUES (?,?,?,?)'''
    cur.execute(sql_app, a)
    con.commit()

cur.close()
con.close()
