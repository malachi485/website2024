import sqlite3
import hashlib

# Connect to SQLite database
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

# Create table if it does not exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(225) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

# User credentials and hashed passwords
username1, password1 = "ManMan", hashlib.sha256("ManManDIDit".encode()).hexdigest()
username2, password2 = "MotherChild", hashlib.sha256("JohnCarter".encode()).hexdigest()
username3, password3 = "LucySmith", hashlib.sha256("Johndoe".encode()).hexdigest()
username4, password4 = "PerryTim", hashlib.sha256("TheU".encode()).hexdigest()
username5, password5 = "ZombieCraft", hashlib.sha256("Minecraftlover".encode()).hexdigest()

# Insert user data into the table
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
