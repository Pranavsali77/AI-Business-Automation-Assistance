import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("leads.db", check_same_thread=False)

# Create cursor
cursor = conn.cursor()

# Create leads table
cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    message TEXT
)
""")

# Save changes
conn.commit()


# Function to save lead data
def save_lead(name, email, phone, message):

    cursor.execute("""
    INSERT INTO leads (name, email, phone, message)
    VALUES (?, ?, ?, ?)
    """, (name, email, phone, message))

    conn.commit()


# Function to fetch all leads
def get_all_leads():

    cursor.execute("SELECT * FROM leads")

    return cursor.fetchall()

#Function to delete lead by ID
def delete_lead(lead_id):

    cursor.execute(
        "DELETE FROM leads WHERE id = ?",
        (lead_id,)
    )

    conn.commit()
    
 # Delete all leads and reset ID
def delete_all_leads():

    # Delete all records
    cursor.execute("DELETE FROM leads")

    # Reset auto increment counter
    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name='leads'"
    )

    conn.commit()