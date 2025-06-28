
from db.connection import conectar

def inserir_dados_teste():
    conn = conectar()
    cursor = conn.cursor()

    # Alunos
    cursor.execute("INSERT INTO Aluno (nome, data_nascimento, email, telefone, endereco) VALUES (?, ?, ?, ?, ?)", 
                   ('Clara Mendes', '2008-04-10', 'clara@ballet.com', '85999990001', 'Rua das Flores, 123'))
    cursor.execute("INSERT INTO Aluno (nome, data_nascimento, email, telefone, endereco) VALUES (?, ?, ?, ?, ?)", 
                   ('Lívia Rocha', '2006-09-22', 'livia@ballet.com', '85999990002', 'Av. Central, 456'))

    # Professores
    cursor.execute("INSERT INTO Professor (nome, especialidade, email, telefone, certificacoes) VALUES (?, ?, ?, ?, ?)", 
                   ('Juliana Andrade', 'Ballet Clássico', 'juliana@escolaballet.com', '85999991111', 'Royal Academy'))
    cursor.execute("INSERT INTO Professor (nome, especialidade, email, telefone, certificacoes) VALUES (?, ?, ?, ?, ?)", 
                   ('Renato Lima', 'Jazz', 'renato@escolaballet.com', '85999992222', 'Broadway Style'))

    # Turmas
    cursor.execute("INSERT INTO Turma (nivel, horario, sala, quantidade_max_alunos, observacoes) VALUES (?, ?, ?, ?, ?)",
                   ('iniciante', '08:00 - 09:30', 'Sala 01', 15, 'Turma para iniciantes de 7 a 10 anos'))
    cursor.execute("INSERT INTO Turma (nivel, horario, sala, quantidade_max_alunos, observacoes) VALUES (?, ?, ?, ?, ?)",
                   ('intermediário', '10:00 - 11:30', 'Sala 02', 12, 'Turma para quem já tem 1 ano de prática'))

    # Apresentações
    cursor.execute("INSERT INTO Apresentacao (nome_evento, data, local, tema, descricao) VALUES (?, ?, ?, ?, ?)",
                   ('Festival de Dança 2025', '2025-11-20', 'Teatro José de Alencar', 'Clássicos do Ballet', 'Apresentações de todas as turmas'))
    cursor.execute("INSERT INTO Apresentacao (nome_evento, data, local, tema, descricao) VALUES (?, ?, ?, ?, ?)",
                   ('Mostra Interna', '2025-06-30', 'Salão Principal', 'Livre', 'Apresentação para familiares'))

    # Avaliações
    cursor.execute("INSERT INTO Avaliacao (aluno_id, nota, comentario, data_avaliacao, observador_externo) VALUES (?, ?, ?, ?, ?)",
                   (1, 9.0, 'Execução precisa e ótima postura.', '2025-06-15', 'Mônica - Avaliadora externa'))
    cursor.execute("INSERT INTO Avaliacao (aluno_id, nota, comentario, data_avaliacao, observador_externo) VALUES (?, ?, ?, ?, ?)",
                   (2, 7.5, 'Boa desenvoltura, precisa melhorar equilíbrio.', '2025-06-16', None))

    # Participações
    cursor.execute("INSERT INTO Participacao (aluno_id, turma_id, professor_id, data_inicio) VALUES (?, ?, ?, ?)",
                   (1, 1, 1, '2025-02-01'))
    cursor.execute("INSERT INTO Participacao (aluno_id, turma_id, professor_id, data_inicio) VALUES (?, ?, ?, ?)",
                   (2, 2, 2, '2025-02-10'))

    conn.commit()
    conn.close()
    print("Dados de teste inseridos com sucesso!")

inserir_dados_teste()

from db.connection import conectar

def inserir_dados_teste():
    conn = conectar()
    cursor = conn.cursor()

    # Alunos
    cursor.execute("INSERT INTO Aluno (nome, data_nascimento, email, telefone, endereco) VALUES (?, ?, ?, ?, ?)", 
                   ('Clara Mendes', '2008-04-10', 'clara@ballet.com', '85999990001', 'Rua das Flores, 123'))
    cursor.execute("INSERT INTO Aluno (nome, data_nascimento, email, telefone, endereco) VALUES (?, ?, ?, ?, ?)", 
                   ('Lívia Rocha', '2006-09-22', 'livia@ballet.com', '85999990002', 'Av. Central, 456'))

    # Professores
    cursor.execute("INSERT INTO Professor (nome, especialidade, email, telefone, certificacoes) VALUES (?, ?, ?, ?, ?)", 
                   ('Juliana Andrade', 'Ballet Clássico', 'juliana@escolaballet.com', '85999991111', 'Royal Academy'))
    cursor.execute("INSERT INTO Professor (nome, especialidade, email, telefone, certificacoes) VALUES (?, ?, ?, ?, ?)", 
                   ('Renato Lima', 'Jazz', 'renato@escolaballet.com', '85999992222', 'Broadway Style'))

    # Turmas
    cursor.execute("INSERT INTO Turma (nivel, horario, sala, quantidade_max_alunos, observacoes) VALUES (?, ?, ?, ?, ?)",
                   ('iniciante', '08:00 - 09:30', 'Sala 01', 15, 'Turma para iniciantes de 7 a 10 anos'))
    cursor.execute("INSERT INTO Turma (nivel, horario, sala, quantidade_max_alunos, observacoes) VALUES (?, ?, ?, ?, ?)",
                   ('intermediário', '10:00 - 11:30', 'Sala 02', 12, 'Turma para quem já tem 1 ano de prática'))

    # Apresentações
    cursor.execute("INSERT INTO Apresentacao (nome_evento, data, local, tema, descricao) VALUES (?, ?, ?, ?, ?)",
                   ('Festival de Dança 2025', '2025-11-20', 'Teatro José de Alencar', 'Clássicos do Ballet', 'Apresentações de todas as turmas'))
    cursor.execute("INSERT INTO Apresentacao (nome_evento, data, local, tema, descricao) VALUES (?, ?, ?, ?, ?)",
                   ('Mostra Interna', '2025-06-30', 'Salão Principal', 'Livre', 'Apresentação para familiares'))

    # Avaliações
    cursor.execute("INSERT INTO Avaliacao (aluno_id, nota, comentario, data_avaliacao, observador_externo) VALUES (?, ?, ?, ?, ?)",
                   (1, 9.0, 'Execução precisa e ótima postura.', '2025-06-15', 'Mônica - Avaliadora externa'))
    cursor.execute("INSERT INTO Avaliacao (aluno_id, nota, comentario, data_avaliacao, observador_externo) VALUES (?, ?, ?, ?, ?)",
                   (2, 7.5, 'Boa desenvoltura, precisa melhorar equilíbrio.', '2025-06-16', None))

    # Participações
    cursor.execute("INSERT INTO Participacao (aluno_id, turma_id, professor_id, data_inicio) VALUES (?, ?, ?, ?)",
                   (1, 1, 1, '2025-02-01'))
    cursor.execute("INSERT INTO Participacao (aluno_id, turma_id, professor_id, data_inicio) VALUES (?, ?, ?, ?)",
                   (2, 2, 2, '2025-02-10'))

    conn.commit()
    conn.close()
    print("Dados de teste inseridos com sucesso!")

inserir_dados_teste()

