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
        <h1> Data import successful </h1>""")

doc = xml.dom.minidom.parse('C:\\Users\\kras2\\PycharmProjects\\5Individual\\book.xml')
humans = doc.getElementsByTagName('human')
doctors = doc.getElementsByTagName('doctor')
appointments = doc.getElementsByTagName('appointment')

for human in humans:
    id_human = human.getAttribute('id')
    name = human.getAttribute('name')
    surname = human.getAttribute('surname')
    reason = human.getAttribute('reason')
    sql_app = '''INSERT or REPLACE INTO Human(id, name, surname, reason) VALUES (?,?,?,?)'''
    cur.execute(sql_app, (id_human, name, surname, reason))
    con.commit()

for doctor in doctors:
    id_doctor = doctor.getAttribute('id')
    name = doctor.getAttribute('name')
    surname = doctor.getAttribute('surname')
    specialty = doctor.getAttribute('specialty')
    sql_app = '''INSERT or REPLACE INTO Doctor(id, name, surname, specialty) VALUES (?,?,?,?)'''
    cur.execute(sql_app, (id_doctor, name, surname, specialty))
    con.commit()

for appointment in appointments:
    id_app = appointment.getAttribute('id_app')
    id_doctor = appointment.getAttribute('id_doctor')
    id_human = appointment.getAttribute('id_human')
    app_time = appointment.getAttribute('app_time')
    sql_app = '''INSERT or REPLACE INTO Appointment(id_app, id_doctor, id_human, app_time) VALUES (?,?,?,?)'''
    cur.execute(sql_app, (id_app, id_doctor, id_human, app_time))
    con.commit()

cur.close()
con.close()
