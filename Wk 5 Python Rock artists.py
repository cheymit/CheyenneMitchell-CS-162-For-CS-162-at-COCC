import sqlite3

# Connect to the database
conn = sqlite3.connect('music_library.db')
cursor = conn.cursor()

# Print only rock genre artists
print("Rock Artists:")
for row in cursor.execute("SELECT * FROM Music_Artists WHERE genre='Rock'"):
    print(row)

conn.close()
