import sqlite3

DB_NAME = "sensor_data.db"

def create_table():
    """Creates a table for storing sensor data if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        pressure REAL,
        temperature REAL,
        flow_rate REAL
    )
    """)
    
    conn.commit()
    conn.close()

def insert_sensor_data(pressure, temperature, flow_rate):
    """Inserts sensor data into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO sensors (pressure, temperature, flow_rate) VALUES (?, ?, ?)",
                   (pressure, temperature, flow_rate))
    
    conn.commit()
    conn.close()
    print("Sensor data saved to database.")

def get_recent_data(limit=5):
    """Fetches the most recent sensor readings."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM sensors ORDER BY timestamp DESC LIMIT ?", (limit,))
    data = cursor.fetchall()
    
    conn.close()
    return data

# Run the table creation when the script is executed
if __name__ == "__main__":
    create_table()
    print("Database and table are set up!")