import os
import sqlite3

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
    <body>""")
print("<h1>Tables Data</h1>")

cur.execute('''SELECT * FROM Human''')
a = cur.fetchall()
print("<table>")
print("<th> id </th>")
print("<th> name </th>")
print("<th> surname </th>")
print("<th> reason </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")

cur.execute('''SELECT * FROM Doctor''')
a = cur.fetchall()
print("<table>")
print("<th> id </th>")
print("<th> name </th>")
print("<th> surname </th>")
print("<th> specialty </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")

cur.execute('''SELECT * FROM Appointment''')
a = cur.fetchall()
print("<table>")
print("<th> id_app </th>")
print("<th> id_doctor </th>")
print("<th> id_human </th>")
print("<th> app_time </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")
print("""</body> </html>""")

cur.close()
con.close()
