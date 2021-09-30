What is PostgreSql
  General purpose and object-relational database management system
  Object classes and inheritance is directly supported in db schemas
  Install PostgreSql using honebrew
      brew install postgresql

      ==> postgresql
To migrate existing data from a previous major version of PostgreSQL run:
  brew postgresql-upgrade-database

    This formula has created a default database cluster with:
      initdb --locale=C -E UTF-8 /usr/local/var/postgres
    For more details, read:
      https://www.postgresql.org/docs/13/app-initdb.html

    To start postgresql:
      brew services start postgresql
    Or, if you don't want/need a background service you can just run:
      /usr/local/opt/postgresql/bin/postgres -D /usr/local/var/postgres


To login to database

brew services start postgresql
brew services list
psql Postgres

#Create database studentdb
create database studentdb;
\c studentdb
create table students(name text,address text,age int ,number int);
\d --> to check table

#Insert data in table
insert into students (name,address,age,number) values('Abhishek Ranjan', 'Ranchi', 34, 99999999);


# Create virtual env for python
python3 -m venv venv
#activate virtual venv
source venv/bin/activate


#Install psycopg2 Its driver to connect python app to database
pip install psycopg2-binary


#Once the new user is created, you can also start using the credentials and log in with the new user’s credentials. You can use the following command to log in with the new user’s credentials. First, we need to quit the current session and then reconnect with the new user’s credentials.

create role testuser with login password 'admin001';
alter role testuser createdb;

psql postgres -U newuser


***************** User Interface to insert data using Tkinter **********************
import tkinter
pip install tk
create  frame
