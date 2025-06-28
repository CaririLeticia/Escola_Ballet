import sqlite3
from db.connection import conectar

def inserir_aluno(nome, data_nascimento, email, telefone=None, endereco=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Aluno (nome, data_nascimento, email, telefone, endereco)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, data_nascimento, email, telefone, endereco))
    conn.commit()
    conn.close()


#manipulacao em massa
def inserir_alunos_em_lote(alunos):
    """
    alunos: Lista de tuplas no formato (nome, data_nascimento, email, telefone, endereco)
    """
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.executemany("""
            INSERT INTO Aluno (nome, data_nascimento, email, telefone, endereco)
            VALUES (?, ?, ?, ?, ?)
        """, alunos)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False
    finally:
        conn.close()



def buscar_aluno_por_nome(substring):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Aluno 
        WHERE LOWER(nome) LIKE LOWER(?)
    """, (f"%{substring}%",))
    return cursor.fetchall()

def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, data_nascimento, email FROM Aluno")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def deletar_aluno(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Aluno WHERE id = ?", (id,))
    conn.commit()
    conn.close()