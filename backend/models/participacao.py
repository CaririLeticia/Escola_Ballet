from db.connection import conectar

def inserir_participacao(aluno_id, turma_id, professor_id, data_inicio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Participacao (aluno_id, turma_id, professor_id, data_inicio)
        VALUES (?, ?, ?, ?)
    """, (aluno_id, turma_id, professor_id, data_inicio))
    conn.commit()
    conn.close()

def listar_participacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Participacao")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_participacao(id, aluno_id, turma_id, professor_id, data_inicio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Participacao
        SET aluno_id = ?, turma_id = ?, professor_id = ?, data_inicio = ?
        WHERE id = ?
    """, (aluno_id, turma_id, professor_id, data_inicio, id))
    conn.commit()
    conn.close()

def deletar_participacao(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Participacao WHERE id = ?", (id,))
    conn.commit()
    conn.close()