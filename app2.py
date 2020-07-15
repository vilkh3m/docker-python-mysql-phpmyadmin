#!/usr/bin/env python

import os
import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'],
                                    port=int(os.environ['MYSQL_PORT']),
                                    database=os.environ['MYSQL_DATABASE'],
                                    user=os.environ['MYSQL_USER'],
                                    password=os.environ['MYSQL_PASSWORD'])

# create table
sql_create_Query = "CREATE TABLE Tabela2  (`id` int(0) NOT NULL AUTO_INCREMENT,`kolumna1` varchar(255) NULL,`kolumna2` varchar(255) NULL,PRIMARY KEY (`id`));"
cursor = connection.cursor()
cursor.execute(sql_create_Query)

# insert
sql_insert_Query = "INSERT INTO Tabela2 (kolumna1, kolumna2) VALUES('wartosc1','wartosc2');"
cursor1 = connection.cursor()
cursor1.execute(sql_insert_Query)
connection.commit()

# select
sql_select_Query = "select * from Tabela2"
cursor2 = connection.cursor()
cursor2.execute(sql_select_Query)
records = cursor2.fetchall()
print("W Tabela2 jest w sumie: ", cursor2.rowcount, " rekordow\n")

print("\nZapisane rekordy")
for row in records:
    print("id = ", row[0], )
    print("kolumna1 = ", row[1])
    print("kolumna2  = ", row[2])
