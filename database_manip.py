import _sqlite3

# Create a table called 'python_programming'
# with columns 'id', 'name', and 'grade'
connection = _sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        grade INTEGER NOT NULL
    )
''')
# Insert new records into the 'python_programming' table
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]
cursor.executemany('''
    INSERT INTO python_programming (id, name, grade)
    VALUES (?, ?, ?)
''', students)

# Select all records with grades between 60 and 80
cursor.execute('''
    SELECT * FROM python_programming
    WHERE grade BETWEEN ? AND ?
''', (60, 80))
results = cursor.fetchall()
for row in results:
    print(row)

# Change Carl Davis's grade to 65
cursor.execute('''
    UPDATE python_programming
    SET grade = ?
    WHERE name = ?
''', (65, 'Carl Davis'))

# Delete Dennis Fredrickson's row
cursor.execute('''
    DELETE FROM python_programming
    WHERE name = ?
''', ('Dennis Fredrickson',))

# Change the grade of all students with an id greater than 55 to 80
cursor.execute('''
    UPDATE python_programming
    SET grade = ?
    WHERE id > ?
''', (80, 55))
# Commit the changes and close the connection
connection.commit()
connection.close()
