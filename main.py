import sqlite3
import xml.dom.minidom

con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.executescript('''DROP TABLE IF EXISTS Human; DROP TABLE IF EXISTS Doctor; DROP TABLE IF EXISTS Appointment''')
sql = '''
CREATE TABLE Human (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    reason TEXT
);
CREATE TABLE Doctor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    specialty TEXT
);
CREATE TABLE Appointment (
    id_app INTEGER PRIMARY KEY AUTOINCREMENT,
    id_doctor INTEGER,
    id_human INTEGER,
    app_time TEXT,
    CONSTRAINT doctor_app_fk
    FOREIGN KEY (id_doctor) REFERENCES Doctor (id),
    CONSTRAINT human_app_fk
    FOREIGN KEY (id_human) REFERENCES Human (id)
);'''

cur.executescript(sql)
cur.executescript('''INSERT INTO Human(name, surname, reason) VALUES ('John', 'Wick', 'Bullet injury');''')
con.commit()

var_list_Human = [
    ('Ivan', 'Ivanov', 'Headache'),
    ('Danil', 'Liadrin', 'Toothache'),
    ('German', 'Hooch', 'Eye problems'),
    ('Magni', 'Bronzebeard', 'Too short')
]
sql_human = '''
    INSERT INTO Human(name, surname, reason) VALUES (?,?,?)
'''
cur.executemany(sql_human, var_list_Human)
con.commit()

var_list_Doctor = [
    ('Ilya', 'Cave', 'Cardiologist'),
    ('Petr', 'Sergeevich', 'Therapist'),
    ('Dmitriy', 'Gop', 'Dentist'),
    ('Mark', 'Korben', 'Eye doctor'),
    ('Kirill', 'Maslov', 'Extension doctor')
]
sql_doctor = '''
    INSERT INTO Doctor(name, surname, specialty) VALUES (?,?,?)
'''
cur.executemany(sql_doctor, var_list_Doctor)
con.commit()

var_list_App = [
    (1, 2, '17.04.2021'),
    (3, 3, '08.08.2023'),
    (4, 4, '01.10.2024'),
    (5, 5, '23.07.2023'),
    (2, 6, '30.01.2023')
]
sql_app = '''INSERT INTO Appointment(id_doctor, id_human, app_time) VALUES (?,?,?)'''
cur.executemany(sql_app, var_list_App)
con.commit()

cur.execute('SELECT * from Human')
print(cur.fetchall())
cur.execute('''SELECT name, surname from Doctor WHERE specialty = 'Therapist' ''')
print(cur.fetchall())
cur.execute('''SELECT name, surname from Doctor WHERE specialty = 'Therapist' ''')
print(cur.fetchall())

cur.close()
con.close()
