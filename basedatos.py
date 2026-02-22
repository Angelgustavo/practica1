import sqlite3

def crear_base():
    conn = sqlite3.connect("tarjeta.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cedula INTEGER NOT NULL,
        saldo REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Base de datos creada correctamente")

if __name__ == "__main__":
    crear_base()