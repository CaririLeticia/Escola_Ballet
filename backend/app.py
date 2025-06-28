from flask import Flask, render_template, request, redirect, url_for

# Importações dos modelos
from models.aluno import inserir_aluno, deletar_aluno, listar_alunos
from models.professor import inserir_professor, deletar_professor, listar_professores
from models.turma import inserir_turma, deletar_turma, listar_turmas
from models.apresentacao import inserir_apresentacao, deletar_apresentacao, listar_apresentacoes
from models.avaliacao import inserir_avaliacao, listar_avaliacoes
from models.participacao import inserir_participacao, deletar_participacao, listar_participacoes

app = Flask(__name__, template_folder='templates', static_folder='static')

# Rota inicial
@app.route('/')
def index():
    return redirect(url_for('mostrar_alunos'))

# ---------- ALUNOS ----------
@app.route('/alunos')
def mostrar_alunos():
    alunos = listar_alunos()
    return render_template('alunos.html', alunos=alunos)

@app.route('/alunos/novo', methods=['POST'])
def adicionar_aluno():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    email = request.form['email']
    inserir_aluno(nome, data_nascimento, email)
    return redirect(url_for('mostrar_alunos'))

@app.route('/alunos/deletar/<int:id>')
def remover_aluno(id):
    deletar_aluno(id)
    return redirect(url_for('mostrar_alunos'))

# ---------- PROFESSORES ----------
@app.route('/professores')
def mostrar_professores():
    professores = listar_professores()
    return render_template('professores.html', professores=professores)

@app.route('/professores/novo', methods=['POST'])
def adicionar_professor():
    nome = request.form['nome']
    especialidade = request.form['especialidade']
    email = request.form['email']
    inserir_professor(nome, especialidade, email)
    return redirect(url_for('mostrar_professores'))

@app.route('/professores/deletar/<int:id>')
def remover_professor(id):
    deletar_professor(id)
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

# ---------- APRESENTAÇÕES ----------
@app.route('/apresentacoes')
def mostrar_apresentacoes():
    apresentacoes = listar_apresentacoes()
    return render_template('apresentacoes.html', apresentacoes=apresentacoes)

@app.route('/apresentacoes/novo', methods=['POST'])
def adicionar_apresentacao():
    nome_evento = request.form['nome_evento']
    data = request.form['data']
    local = request.form['local']
    tema = request.form.get('tema')
    inserir_apresentacao(nome_evento, data, local, tema)
    return redirect(url_for('mostrar_apresentacoes'))

@app.route('/apresentacoes/deletar/<int:id>')
def remover_apresentacao(id):
    deletar_apresentacao(id)
    return redirect(url_for('mostrar_apresentacoes'))

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
