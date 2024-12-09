import sqlite3

def inserttodb(query, parameters=()):

    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        print("Data inserted successfully.")

def update(query, parameters=()):

    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        print("Data updated successfully.")

def delete(query, parameters=()):

    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        print("Data deleted successfully.")

def select(query, parameters=()):

    with sqlite3.connect('mydatabase.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        return results
