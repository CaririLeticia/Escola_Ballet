from db.connection import conectar

def inserir_professor(nome, especialidade, email, telefone=None, certificacoes=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Professor (nome, especialidade, email, telefone, certificacoes)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, especialidade, email, telefone, certificacoes))
    conn.commit()
    conn.close()

def listar_professores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Professor")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_professor(id, nome, especialidade, email, telefone=None, certificacoes=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Professor
        SET nome = ?, especialidade = ?, email = ?, telefone = ?, certificacoes = ?
        WHERE id = ?
    """, (nome, especialidade, email, telefone, certificacoes, id))
    conn.commit()
    conn.close()

def deletar_professor(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Professor WHERE id = ?", (id,))
    conn.commit()
    conn.close()