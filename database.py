import sqlite3

def setup_database():
    conn = sqlite3.connect('techcorp.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS employees")
    cursor.execute("""
        CREATE TABLE employees (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   phone TEXT,
                   pin TEXT
        )
    """)
    users = [
        ("Alice", "555-0100", "1234"),
        ("Bob", "555-0101", "5678"),
        ("Charlie", "555-0102", "1212")
    ]
    cursor.executemany("INSERT INTO employees (name,phone,pin) VALUES (?, ?, ?)", users)
    conn.commit()
    conn.close()
    print("Database initialized.")

def get_employee_details(name):
    conn= sqlite3.connect("techcorp.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM employees WHERE name = ?",(name,))
    result = cur.fetchone()
    conn.close()
    return result

if __name__ == "__main__":
    setup_database()
    print("Testing query for Alice:", get_employee_details("Alice"))