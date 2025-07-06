from flask import Flask, render_template, request, redirect, url_for

# Importações dos modelos
from models.aluno import inserir_aluno, deletar_aluno, listar_alunos
from models.professor import inserir_professor, deletar_professor, listar_professores
from models.turma import inserir_turma, deletar_turma, listar_turmas
from models.coreografia import inserir_coreografia, deletar_coreografia, listar_coreografias, atualizar_coreografia
from models.avaliacao import inserir_avaliacao, listar_avaliacoes
from models.participacao import inserir_participacao, deletar_participacao, listar_participacoes
from db.connection import conectar

app = Flask(__name__, template_folder='templates', static_folder='static')

# Rota inicial
@app.route('/')
def index():
    return redirect(url_for('mostrar_alunos'))

# ---------- ALUNOS ----------
@app.route('/alunos')
def mostrar_alunos():
    alunos = listar_alunos()
    turmas = listar_turmas()
    return render_template('alunos.html', alunos=alunos, turmas=turmas)

@app.route('/alunos/deletar/<int:id>')
def remover_aluno(id):
    deletar_aluno(id)
    return redirect(url_for('mostrar_alunos'))

@app.route('/alunos/novo', methods=['POST'])
def adicionar_aluno():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    email = request.form['email']
    turma_id = request.form.get('turma_id') or None
    inserir_aluno(nome, data_nascimento, email, turma_id)
    return redirect(url_for('mostrar_alunos'))

# ---------- PROFESSORES ----------
@app.route('/professores')
def mostrar_professores():
    professores = listar_professores()
    turmas = listar_turmas()
    return render_template('professores.html', professores=professores, turmas=turmas)

@app.route('/professores/deletar/<int:id>')
def remover_professor(id):
    deletar_professor(id)
    return redirect(url_for('mostrar_professores'))

@app.route('/professores/novo', methods=['POST'])
def adicionar_professor():
    nome = request.form['nome']
    especialidade = request.form['especialidade']
    email = request.form['email']
    turma_id = request.form.get('turma_id') or None
    inserir_professor(nome, especialidade, email, turma_id)
    return redirect(url_for('mostrar_professores'))

# ---------- TURMAS ----------
@app.route('/turmas')
def mostrar_turmas():
    turmas = listar_turmas()
    return render_template('turmas.html', turmas=turmas)

@app.route('/turmas/novo', methods=['POST'])
def adicionar_turma():
    nivel = request.form['nivel']
    horario = request.form['horario']
    sala = request.form['sala']
    inserir_turma(nivel, horario, sala)
    return redirect(url_for('mostrar_turmas'))

@app.route('/turmas/deletar/<int:id>')
def remover_turma(id):
    deletar_turma(id)
    return redirect(url_for('mostrar_turmas'))

@app.route('/turmas/<int:id>')
def visualizar_turma(id):
    conn = conectar()
    cursor = conn.cursor()
    
    # Buscar informações da turma
    cursor.execute("SELECT * FROM Turma WHERE id = ?", (id,))
    turma = cursor.fetchone()
    
    # Buscar professor da turma
    cursor.execute("SELECT * FROM Professor WHERE turma_id = ?", (id,))
    professor = cursor.fetchone()
    
    # Buscar alunos da turma
    cursor.execute("SELECT * FROM Aluno WHERE turma_id = ?", (id,))
    alunos = cursor.fetchall()
    
    conn.close()
    return render_template('turma_detalhes.html', turma=turma, professor=professor, alunos=alunos)

# ---------- APRESENTAÇÕES ----------
@app.route('/coreografias')
def mostrar_coreografias():
    coreografias = listar_coreografias()
    turmas = listar_turmas()
    return render_template('coreografias.html', coreografias=coreografias, turmas=turmas)

@app.route('/coreografias/novo', methods=['POST'])
def adicionar_coreografia():
    nome_evento = request.form['nome_evento']
    data = request.form['data']
    local = request.form['local']
    turma_id = request.form.get('turma_id') or None
    tema = request.form.get('tema')
    descricao = request.form.get('descricao')
    inserir_coreografia(nome_evento, data, local, turma_id, tema, descricao)
    return redirect(url_for('mostrar_coreografias'))

@app.route('/coreografias/deletar/<int:id>')
def remover_coreografia(id):
    deletar_coreografia(id)
    return redirect(url_for('mostrar_coreografias'))

@app.route('/coreografias/editar/<int:id>')
def editar_coreografia(id):
    conn = conectar()
    cursor = conn.cursor()

    # Buscar coreografia
    cursor.execute("SELECT * FROM Coreografia WHERE id = ?", (id,))
    coreografia = cursor.fetchone()

    # Buscar turmas disponíveis
    cursor.execute("SELECT id, nivel, horario FROM Turma")
    turmas = cursor.fetchall()

    conn.close()
    return render_template('editar_coreografia.html', coreografia=coreografia, turmas=turmas)

@app.route('/coreografias/editar/<int:id>', methods=['POST'])
def salvar_edicao_coreografia(id):
    nome_evento = request.form['nome_evento']
    data = request.form['data']
    local = request.form['local']
    tema = request.form.get('tema')
    descricao = request.form.get('descricao')
    turma_id = request.form.get('turma_id') or None

    atualizar_coreografia(id, nome_evento, data, local, tema, descricao, turma_id)
    return redirect(url_for('mostrar_coreografias'))

# ---------- AVALIAÇÕES ----------
@app.route('/avaliacoes')
def mostrar_avaliacoes():
    avaliacoes = listar_avaliacoes()
    return render_template('avaliacoes.html', avaliacoes=avaliacoes)

@app.route('/avaliacoes/novo', methods=['POST'])
def adicionar_avaliacao():
    aluno_id = request.form['aluno_id']
    nota = request.form['nota']
    comentario = request.form['comentario']
    data_avaliacao = request.form.get('data_avaliacao')
    inserir_avaliacao(aluno_id, nota, comentario, data_avaliacao)
    return redirect(url_for('mostrar_avaliacoes'))

# ---------- PARTICIPAÇÕES ----------
@app.route('/participacoes')
def mostrar_participacoes():
    participacoes = listar_participacoes()
    return render_template('participacoes.html', participacoes=participacoes)

@app.route('/participacoes/novo', methods=['POST'])
def adicionar_participacao():
    aluno_id = request.form['aluno_id']
    turma_id = request.form['turma_id']
    professor_id = request.form['professor_id']
    data_inicio = request.form['data_inicio']
    inserir_participacao(aluno_id, turma_id, professor_id, data_inicio)
    return redirect(url_for('mostrar_participacoes'))

@app.route('/participacoes/deletar/<int:id>')
def remover_participacao(id):
    deletar_participacao(id)
    return redirect(url_for('mostrar_participacoes'))

# ---------- EXECUTAR ----------
if __name__ == '__main__':
    app.run(debug=True)