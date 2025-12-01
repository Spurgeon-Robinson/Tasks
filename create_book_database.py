# This creates the book database
""""This module provides a function to connect to a SQLite database,"""
import sqlite3


def get_sql_cursor():
    """
    Establishes a connection to "ebookstore.db", sets up the database
    schema by dropping any existing "Books" table, and "Authors" table
    creating a new one, and inserting initial data.
    Returns a cursor for further database
    operations.

    Returns:
        sqlite3.Cursor: Cursor for database interaction
    """
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Books;')
    cursor.execute('DROP TABLE IF EXISTS Authors;')

    with open("SQLFiles/create_book_table.sql",
              encoding='utf-8') as create_book_file:
        cursor.execute(create_book_file.read())

    with open("SQLFiles/insert_book_values.sql",
              encoding='utf-8') as insert_book_file:
        cursor.execute(insert_book_file.read())

    with open("SQLFiles/create_author_table.sql",
              encoding='utf-8') as create_author_file:
        cursor.execute(create_author_file.read())

    with open("SQLFiles/insert_author_values.sql",
              encoding='utf-8') as insert_author_file:
        cursor.execute(insert_author_file.read())

    return cursor
