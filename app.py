#!/usr/bin/env python
# coding: utf-8

import os
from peewee import *
from datetime import datetime


database = MySQLDatabase(os.environ['MYSQL_DATABASE'], 
                            host=os.environ['MYSQL_HOST'], 
                            port=int(os.environ['MYSQL_PORT']),
                            user=os.environ['MYSQL_USER'], 
                            password=os.environ['MYSQL_PASSWORD'])

class BaseModel(Model):
    class Meta:     
        database = database

class Tabela1(BaseModel):
    kolumna1 = CharField()
    kolumna2 = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField(null=True) 

if __name__ == '__main__':
    # create table
    with database: database.create_tables([Tabela1])

    teraz = datetime.now()
    # insert
    ins = Tabela1(kolumna1="k1", kolumna2="k2", created_at=teraz)
    ins.save()

    # select
    records = Tabela1.select()
    print("W Tabela2 jest w sumie: ", records.count(), " rekordow\n")

    print("\nZapisane rekordy")
    for row in records.dicts():
        print("id = ", row['id'], )
        print("kolumna1 = ", row['kolumna1'])
        print("kolumna2  = ", row['kolumna2'])




    print(ins.id)
