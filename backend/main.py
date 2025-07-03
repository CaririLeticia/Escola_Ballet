from db.connection import conectar
import os

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    caminho_schema = os.path.join(os.path.dirname(__file__), "db", "schema.sql")
    with open(caminho_schema, "r", encoding="utf-8") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Tabelas criadas com sucesso.")

