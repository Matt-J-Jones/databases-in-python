

# Setting up PostgreSQL

Learn to set up PostgreSQL.

## Introduction

<!-- OMITTED -->

Up until now, you've been storing your program's data in memory — as attributes, lists, objects, etc. If we exit the program, all the data is lost, which is not great if we need to store data for the long term (think bank accounts, user accounts, order history...).

This week, you'll learn how to use a database to store data used by programs.

There are many types of databases, but this week you'll learn how to use **PostgreSQL**, which is a **relational database** software.

PostgreSQL is free and open-source, and is also widely used in a lot of large-scale, professional applications, which makes it the perfect choice for a first database to learn with.

## About relational databases

A **database** is a collection of **tables**. Each table stores a list of "things". For example, if our application is a blogging system, we could have a table 'posts' and a table 'comments'.

```
+----------------------------------------------------------+
|                                                          |
|   Database 'blog'                                        |
|                                                          |
|   +--------------------+       +--------------------+    |
|   |                    |       |                    |    |
|   |  Table 'posts'     |       |  Table 'comments'  |    |
|   |                    |       |                    |    |
|   +--------------------+       +--------------------+    |
+----------------------------------------------------------+
```

A table has **columns** for the attributes of the records, which are fixed and the same for each record (unless we're changing the schema of this table later). Each record is a **row** in the table.

For example, a table "students" could have columns "name" and "cohort_name".

Here's an example of how such a table would look like:

```
Table: students

 id |     name     | cohort_name
----+--------------+------------
  1 | Sarah        | April 2022
  2 | Georgia      | April 2022
  3 | David        | May 2022
  4 | Ali          | April 2022
```

*(By convention, table names and column names are **always lowercase**, using underscores to separate words). Table names are always plural.*

## Setup

```PS
# Run this after the installation
# to start the postgresql software
# in the background.
cd "C:\Program Files\PostgreSQL\16\bin"
.\pg_ctl.exe start -D "C:\Program Files\PostgreSQL\16\data"

# To start PSQL
# Enter username and password

psql -U postgres

# You should get the following output:
==> psql (16.1)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.
```

If you have a different system, [follow the relevant instructions](https://www.postgresql.org/download/), and if you're not sure, ask your coach. If you have any trouble with the installation process, it's probably better to ask your coach for help, rather than spending too much time figuring it out.

## Demonstration

[Here's a video introduction and demonstration.](https://www.youtube.com/watch?v=9wT1FVQbPZw)