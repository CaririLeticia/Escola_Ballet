
from db.connection import conectar

def inserir_avaliacao(aluno_id, nota, comentario, data_avaliacao=None, observador_externo=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Avaliacao (aluno_id, nota, comentario, data_avaliacao, observador_externo)
        VALUES (?, ?, ?, ?, ?)
    """, (aluno_id, nota, comentario, data_avaliacao, observador_externo))
    conn.commit()
    conn.close()

def listar_avaliacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Avaliacao")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_avaliacao(id, aluno_id, nota, comentario, data_avaliacao=None, observador_externo=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Avaliacao
        SET aluno_id = ?, nota = ?, comentario = ?, data_avaliacao = ?, observador_externo = ?
        WHERE id = ?
    """, (aluno_id, nota, comentario, data_avaliacao, observador_externo, id))
    conn.commit()
    conn.close()

def deletar_avaliacao(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Avaliacao WHERE id = ?", (id,))
    conn.commit()
    conn.close()

#Consulta com ANY
def alunos_acima_da_media():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.nome, av.nota 
        FROM Aluno a
        JOIN Avaliacao av ON a.id = av.aluno_id
        WHERE av.nota > ANY (
            SELECT AVG(nota) FROM Avaliacao GROUP BY aluno_id
        )
    """)

from db.connection import conectar

def inserir_avaliacao(aluno_id, nota, comentario, data_avaliacao=None, observador_externo=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Avaliacao (aluno_id, nota, comentario, data_avaliacao, observador_externo)
        VALUES (?, ?, ?, ?, ?)
    """, (aluno_id, nota, comentario, data_avaliacao, observador_externo))
    conn.commit()
    conn.close()

def listar_avaliacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Avaliacao")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_avaliacao(id, aluno_id, nota, comentario, data_avaliacao=None, observador_externo=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Avaliacao
        SET aluno_id = ?, nota = ?, comentario = ?, data_avaliacao = ?, observador_externo = ?
        WHERE id = ?
    """, (aluno_id, nota, comentario, data_avaliacao, observador_externo, id))
    conn.commit()
    conn.close()

def deletar_avaliacao(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Avaliacao WHERE id = ?", (id,))
    conn.commit()
    conn.close()

#Consulta com ANY
def alunos_acima_da_media():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.nome, av.nota 
        FROM Aluno a
        JOIN Avaliacao av ON a.id = av.aluno_id
        WHERE av.nota > ANY (
            SELECT AVG(nota) FROM Avaliacao GROUP BY aluno_id
        )
    """)

    return cursor.fetchall()