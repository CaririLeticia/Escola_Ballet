import sqlite3
from db.connection import conectar

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

def deletar_aluno(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Aluno WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def inserir_aluno(nome, data_nascimento, email, turma_id=None, telefone=None, endereco=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Aluno (nome, data_nascimento, email, turma_id, telefone, endereco)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, data_nascimento, email, turma_id, telefone, endereco))
    conn.commit()
    conn.close()

def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, a.nome, a.data_nascimento, a.email, 
               COALESCE(a.turma_id, 'Sem turma') as turma_id
        FROM Aluno a
    """)
    alunos = cursor.fetchall()
    conn.close()
    return alunos