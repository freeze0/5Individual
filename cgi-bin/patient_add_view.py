import cgi
import sqlite3
import os

db_path = 'C:/Users/kras2/PycharmProjects/5Individual'
db_file = 'db01.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

form = cgi.FieldStorage()
text1 = form.getfirst("Name", "Не задано")
text2 = form.getfirst("Surname", "Не задано")
text3 = form.getfirst("Reason", "Не задано")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Patient handling</title>
        </head>
    <body>""")
print("<h1>Patient handling</h1>")
print("<p>Name: %s</p>"%text1)
print("<p>Surname: %s</p>"%text2)
print("<p>Reason: %s</p>"%text3)

if text1 == "Не задано" or text2 == "Не задано" or text3 == "Не задано":
    print("<p> Неправильные данные</p>")
else:
    a = (text1, text2, text3)
    sql_insert = '''INSERT INTO Human(name, surname, reason) VALUES(?,?,?);'''
    cur.execute(sql_insert, a)
    con.commit()

print("""</body> </html>""")

cur.close()
con.close()
