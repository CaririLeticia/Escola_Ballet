-- Tabela Aluno
CREATE TABLE IF NOT EXISTS Aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    endereco TEXT,
    turma_id INTEGER REFERENCES Turma(id)
);

-- Tabela Professor
CREATE TABLE IF NOT EXISTS Professor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    certificacoes TEXT,
    turma_id INTEGER REFERENCES Turma(id)
);

-- Tabela Turma
CREATE TABLE IF NOT EXISTS Turma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nivel TEXT NOT NULL DEFAULT 'iniciante',
    horario TEXT NOT NULL,
    sala TEXT NOT NULL,
    quantidade_max_alunos INTEGER,
    observacoes TEXT
);

-- Tabela Apresentacao
CREATE TABLE IF NOT EXISTS Coreografia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_evento TEXT NOT NULL,
    data TEXT NOT NULL,
    local TEXT NOT NULL,
    tema TEXT,
    descricao TEXT,
    turma_id INTEGER,
    FOREIGN KEY (turma_id) REFERENCES Turma(id)
);

-- Tabela Avaliacao
CREATE TABLE IF NOT EXISTS Avaliacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    nota REAL NOT NULL,
    comentario TEXT NOT NULL,
    data_avaliacao DATE,
    observador_externo TEXT,
    FOREIGN KEY(aluno_id) REFERENCES Aluno(id)
);

-- Tabela Participacao (relacionamento ternário)
CREATE TABLE IF NOT EXISTS Participacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    turma_id INTEGER,
    professor_id INTEGER,
    data_inicio DATE,
    FOREIGN KEY(aluno_id) REFERENCES Aluno(id),
    FOREIGN KEY(turma_id) REFERENCES Turma(id),
    FOREIGN KEY(professor_id) REFERENCES Professor(id)
);

-- Tabela de logs
CREATE TABLE IF NOT EXISTS Log_Alteracoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tabela_afetada TEXT NOT NULL,
    id_registro INTEGER NOT NULL,
    acao TEXT NOT NULL,  -- 'INSERT', 'UPDATE', 'DELETE'
    data_hora DATETIME NOT NULL
);

-- Gatilho para registrar alterações em Professores
CREATE TRIGGER IF NOT EXISTS log_professor_update
AFTER UPDATE ON Professor
BEGIN
    INSERT INTO Log_Alteracoes (
        tabela_afetada, 
        id_registro, 
        acao, 
        data_hora
    ) VALUES (
        'Professor', 
        OLD.id, 
        'UPDATE', 
        datetime('now')
    );
END;