
from db.connection import conectar

def inserir_turma(nivel, horario, sala, quantidade_max_alunos=None, observacoes=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Turma (nivel, horario, sala, quantidade_max_alunos, observacoes)
        VALUES (?, ?, ?, ?, ?)
    """, (nivel, horario, sala, quantidade_max_alunos, observacoes))
    conn.commit()
    conn.close()

def listar_turmas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Turma")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_turma(id, nivel, horario, sala, quantidade_max_alunos=None, observacoes=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Turma
        SET nivel = ?, horario = ?, sala = ?, quantidade_max_alunos = ?, observacoes = ?
        WHERE id = ?
    """, (nivel, horario, sala, quantidade_max_alunos, observacoes, id))
    conn.commit()
    conn.close()

def deletar_turma(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Turma WHERE id = ?", (id,))
    conn.commit()
    conn.close()

#JOIN + GROUP BY + HAVING
def turmas_com_vagas_disponiveis():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, t.nivel, t.quantidade_max_alunos - COUNT(p.aluno_id) AS vagas
        FROM Turma t
        LEFT JOIN Participacao p ON t.id = p.turma_id
        GROUP BY t.id
        HAVING vagas > 0
    """)
    return cursor.fetchall()

#atualizacao em lotes
def atualizar_niveis_em_lote(turmas_nivel):
    """
    turmas_nivel: Lista de tuplas (novo_nivel, id_turma)
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.executemany("""
        UPDATE Turma SET nivel = ? WHERE id = ?
    """, turmas_nivel)
    conn.commit()