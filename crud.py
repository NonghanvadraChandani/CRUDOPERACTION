#import sqlite3
import sqlite3

#create database
con=sqlite3.connect('crud.db')
print('database created')

#create table movie 
#con.execute('create table movie (leadactor text,actress text,year int,director text,moviename text)')
#print('table created')

#insert record
con.execute('insert into movie values("aurjun","samantha",2021,"rohit","hero")')
con.execute('insert into movie values("aurjun kapur","nathasa",2011,"manish patel","india")')
con.execute('insert into movie values("salaman khan","priynaka chopada",2019,"rohit","superhero")')

con.commit()
print('record inserted')

#display record
data=con.execute('select * from movie')
for row in data:
    print("Lead Actor:",row[0])
    print("Actress:",row[1])
    print("Year",row[2])
    print("Director Name:",row[3])
    print("Movie Name:",row[4])

#select movie based on actross name
print("====================")
data=con.execute('select * from movie where actress="samantha"')
for row in data:
    print("Lead Actor:",row[0])
    print("Actress:",row[1])
    print("Year",row[2])
    print("Director Name:",row[3])
    print("Movie Name:",row[4])
