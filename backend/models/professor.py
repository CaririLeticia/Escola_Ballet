from db.connection import conectar

def inserir_professor(nome, especialidade, email, turma_id=None, telefone=None, certificacoes=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Professor (nome, especialidade, email, turma_id, telefone, certificacoes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, especialidade, email, turma_id, telefone, certificacoes))
    conn.commit()
    conn.close()

def listar_professores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id, p.nome, p.especialidade, p.email, 
               COALESCE(p.turma_id, 'Sem turma') as turma_id,
               p.telefone, p.certificacoes
        FROM Professor p
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_professor(id, nome, especialidade, email, turma_id=None, telefone=None, certificacoes=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Professor
        SET nome = ?, especialidade = ?, email = ?, turma_id = ?, telefone = ?, certificacoes = ?
        WHERE id = ?
    """, (nome, especialidade, email, turma_id, telefone, certificacoes, id))
    conn.commit()
    conn.close()

def deletar_professor(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Professor WHERE id = ?", (id,))
    conn.commit()
    conn.close()
