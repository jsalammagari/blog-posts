import sqlite3

connection = sqlite3.connect('database.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())
connection.execute(
    '''
    DROP TABLE IF EXISTS posts;
    '''
)
connection.execute(
    '''
    CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);'''
)


cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )
connection.commit()
connection.close()
