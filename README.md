# Databases

_Coaching this? Read the coach guidance
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/distributed_applications/databases/HOW_TO_COACH.x.md)_

In this module your objectives are:

* **Design a database schema with at least two tables** from a specification,
    including a one-to-many relationship between two tables, and create the
    schema in a database using SQL.
* **Use SQL to query a database** to read data from one table or resulting of
    a join, create new records, update and delete.
* **Integrate a relational database to a program** by test-driving classes
    which implement CRUD methods to send SQL queries to a database.
* **Explain how your program communicates with the database** by creating a
    sequence diagram.

You will achieve these by working through a sequence of exercises and challenges
over one week.

## Sequence

Work through each of these exercises in sequence.

This module is designed to be worked on during a week. Here's a suggested pace —
you might find you need more (or less) time than this to complete the
challenges, and that's OK.

* Day 1: SQL bites.
* Days 2-5: Rest of the challenges
* Solo challenge at the end of the week.

### Phase Zero: Get started

[Watch this introduction video](https://www.youtube.com/watch?v=5PJQscmAEI4)
before starting the sequence below.

### Phase One: SQL Bites

Go through these exercises and learn how to set up PostgreSQL and use SQL to read
and manipulate data stored in an existing database.

<!-- OMITTED -->

1. [Setting up PostgreSQL](https://github.com/makersacademy/databases-in-python/blob/main/sql_bites/01_setting_up_database.md) ✓
2. [Using `psql` to load data](https://github.com/makersacademy/databases-in-python/blob/main/sql_bites/02_using_psql.md) ✓
3. [Querying data](https://github.com/makersacademy/databases-in-python/blob/main/sql_bites/03_querying_data.md) ✓
4. [Updating or deleting data](https://github.com/makersacademy/databases-in-python/blob/main/sql_bites/04_updating_and_deleting_date.md) ✓
5. [Creating new data](https://github.com/makersacademy/databases-in-python/blob/main/sql_bites/05_creating_new_data.md) ✓
6. [Using TablePlus](https://github.com/makersacademy/databases-in-python/blob/main/sql_bites/06_using_table_plus.md) ✓

### Phase Two: Challenges

Go through these exercises and learn how to set up and gradually build a program
which communicates with a database.

1. [Setting up a project](https://github.com/makersacademy/databases-in-python/blob/main/challenges/01_setting_up_project.md) ✓
2. [Designing a Repository
   class](https://github.com/makersacademy/databases-in-python/blob/main/challenges/02_test_driving_model_repository_classes.md) ✓
3. [Diagramming a database
   application](https://github.com/makersacademy/databases-in-python/blob/main/challenges/03_creating_sequence_diagrams.md)
4. [Designing a schema with one
   table](https://github.com/makersacademy/databases-in-python/blob/main/challenges/04_designing_schema_one_table.md)
5. [Designing a Repository class "find"
   method](https://github.com/makersacademy/databases-in-python/blob/main/challenges/05_test_driving_find_method.md)
6. [Designing a schema with two related
   tables](https://github.com/makersacademy/databases-in-python/blob/main/challenges/06_designing_schema_two_tables.md)
7. [Designing a Repository class "create" and "delete"
   methods](https://github.com/makersacademy/databases-in-python/blob/main/challenges/07_test_driving_write_operations.md)
8. [Wrapping in an Application
   class](https://github.com/makersacademy/databases-in-python/blob/main/challenges/08_wrapping_in_application_class.md)

### Phase Three: Joins and Many-to-Many

This is advanced material. Work on it only if you've completed all the
challenges above.

1. [Using SQL joins](https://github.com/makersacademy/databases-in-python/blob/main/joins/01_using_joins.md)
2. [Designing a Repository class using
   joins](https://github.com/makersacademy/databases-in-python/blob/main/joins/02_test_driving_repository_class_with_join.md)
3. [Using joins with Many-to-many
   relationships](https://github.com/makersacademy/databases-in-python/blob/main/joins/03_using_joins_with_many_to_many.md)
4. [Designing Many-to-many
   relationships](https://github.com/makersacademy/databases-in-python/blob/main/joins/04_designing_many_to_many_relationships.md)
5. [Designing a Repository class with
   Many-to-many](https://github.com/makersacademy/databases-in-python/blob/main/joins/05_repository_classes_many_to_many.md)

### Phase Four: Solo Project

Do this project solo. It is designed to help you test all of your skills for
this module.

[Shop Manager](https://github.com/makersacademy/databases-in-python/blob/main/projects/shop_manager_project.md)
