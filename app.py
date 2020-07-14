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

class Test(BaseModel):
    kolumna1 = CharField()
    kolumna2 = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField(null=True) 

if __name__ == '__main__':
    with database: database.create_tables([Test])

    teraz = datetime.now()

    ins = Test(kolumna1="k1", kolumna2="k2", created_at=teraz)
    ins.save()

    print(ins.id)
