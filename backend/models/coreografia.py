
from db.connection import conectar

def inserir_coreografia(nome_evento, data, local, turma_id, tema=None, descricao=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Coreografia (nome_evento, data, local, tema, descricao, turma_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome_evento, data, local, tema, descricao, turma_id))
    conn.commit()
    conn.close()

def listar_coreografias():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.id, c.nome_evento, c.data, c.local, c.tema, c.descricao,
               c.turma_id, t.nivel, t.horario
        FROM Coreografia c
        LEFT JOIN Turma t ON c.turma_id = t.id
        ORDER BY c.data DESC
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def deletar_coreografia(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Coreografia WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def atualizar_coreografia(id, nome_evento, data, local, tema=None, descricao=None, turma_id=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Coreografia
        SET nome_evento = ?, data = ?, local = ?, tema = ?, descricao = ?, turma_id = ?
        WHERE id = ?
    """, (nome_evento, data, local, tema, descricao, turma_id, id))
    conn.commit()
    conn.close()

def buscar_coreografia_por_tema(substring):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Coreografia
        WHERE LOWER(tema) LIKE LOWER(?)
    """, (f"%{substring}%",))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

