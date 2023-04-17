import os
import sqlite3
import xml.dom.minidom

db_path = 'C:/Users/kras2/PycharmProjects/5Individual'
db_file = 'db01.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

cur.execute('SELECT * FROM Human')
humans = cur.fetchall()
cur.execute('SELECT * FROM Doctor')
doctors = cur.fetchall()
cur.execute('SELECT * FROM Appointment')
apps = cur.fetchall()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Data</title>
        </head>
        <h1> Data export successful </h1>""")

doc = xml.dom.minidom.Document()

root = doc.createElement('medicine')
doc.appendChild(root)

humans_list = doc.createElement('humans')
root.appendChild(humans_list)
for human in humans:
    human_elem = doc.createElement('humans')
    human_elem.setAttribute('id', str(human[0]))
    human_elem.setAttribute('name', human[1])
    human_elem.setAttribute('surname', human[2])
    human_elem.setAttribute('reason', human[3])
    humans_list.appendChild(human_elem)

doctors_list = doc.createElement('doctors')
root.appendChild(doctors_list)
for doctor in doctors:
    doctor_elem = doc.createElement('humans')
    doctor_elem.setAttribute('id', str(doctor[0]))
    doctor_elem.setAttribute('name', doctor[1])
    doctor_elem.setAttribute('surname', doctor[2])
    doctor_elem.setAttribute('specialty', doctor[3])
    doctors_list.appendChild(doctor_elem)

apps_list = doc.createElement('appointments')
root.appendChild(apps_list)
for app in apps:
    app_elem = doc.createElement('humans')
    app_elem.setAttribute('id_app', str(app[0]))
    app_elem.setAttribute('id_doctor', str(app[1]))
    app_elem.setAttribute('id_human', str(app[2]))
    app_elem.setAttribute('app_time', str(app[3]))
    apps_list.appendChild(app_elem)

with open('C:\\Users\\kras2\\PycharmProjects\\5Individual\\book.xml', 'w') as f:
    f.write(doc.toprettyxml())

cur.close()
con.close()
