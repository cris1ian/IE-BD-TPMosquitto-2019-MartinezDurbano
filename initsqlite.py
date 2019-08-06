import sqlite3

db_name =  "iot-sqlite.db"

# Cristian: borrar todas las tablas que puedan existir, luego creo las necesarias
#           creadas una para cada magnitud de cada sensor de forma independiente
# SQLite DB Table Schema
table_schema="""
drop table if exists dummyroom_dummysensor ;
drop table if exists bedroom_temperature    ;
drop table if exists bedroom_humidity       ;
drop table if exists bedroom_noisemeter     ;
drop table if exists kitchen_temperature    ;
drop table if exists kitchen_humidity       ;
drop table if exists livingroom_temperature ;
drop table if exists livingroom_humidity    ;

create table bedroom_temperature    (
  value real,
  unit text,
  timestamp real primary key
);
create table bedroom_humidity       (
  value real,
  unit text,
  timestamp real primary key
);
create table bedroom_noisemeter     (
  value real,
  unit text,
  timestamp real primary key
);
create table kitchen_temperature    (
  value real,
  unit text,
  timestamp real primary key
);
create table kitchen_humidity       (
  value real,
  unit text,
  timestamp real primary key
);
create table livingroom_temperature (
  value real,
  unit text,
  timestamp real primary key
);
create table livingroom_humidity    (
  value real,
  unit text,
  timestamp real primary key
);"""

#Connect or Create DB File
conn = sqlite3.connect(db_name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(table_schema)
curs.executescript(table_schema)

#Close DB
curs.close()
conn.close()
