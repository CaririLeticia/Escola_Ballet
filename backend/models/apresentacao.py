from db.connection import conectar

def inserir_apresentacao(nome_evento, data, local, tema=None, descricao=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Apresentacao (nome_evento, data, local, tema, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (nome_evento, data, local, tema, descricao))
    conn.commit()
    conn.close()

def listar_apresentacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Apresentacao")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_apresentacao(id, nome_evento, data, local, tema=None, descricao=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Apresentacao
        SET nome_evento = ?, data = ?, local = ?, tema = ?, descricao = ?
        WHERE id = ?
    """, (nome_evento, data, local, tema, descricao, id))
    conn.commit()
    conn.close()

def deletar_apresentacao(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Apresentacao WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def buscar_apresentacao_por_tema(substring):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Apresentacao
        WHERE LOWER(tema) LIKE LOWER(?)
    """, (f"%{substring}%",))
    return cursor.fetchall()