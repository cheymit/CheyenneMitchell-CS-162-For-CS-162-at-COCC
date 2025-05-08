import sqlite3

# Connect to the database
conn = sqlite3.connect('music_library.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Music_Artists (
    artist TEXT,
    genre TEXT,
    number_recordings INTEGER
)
''')

# Insert data
cursor.execute("DELETE FROM Music_Artists")  # Clear old data (optional but helpful during testing)
artists = [
    ('Miley', 'Rock', 14),
    ('Dolly', 'Country', 123),
    ('Eminem', 'HipHop', 98),
    ('Brittany', 'Rock', 37)
]
cursor.executemany("INSERT INTO Music_Artists VALUES (?, ?, ?)", artists)
conn.commit()

# Print the full table
print("All Artists:")
for row in cursor.execute("SELECT * FROM Music_Artists"):
    print(row)

conn.close()

