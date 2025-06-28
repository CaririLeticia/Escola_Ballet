from db.connection import conectar

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    with open("db/schema.sql", "r") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Tabelas criadas com sucesso.")

