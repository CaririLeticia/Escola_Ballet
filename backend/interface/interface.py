import tkinter as tk
from models.aluno import inserir_aluno

def cadastrar():
    nome = entry_nome.get()
    data = entry_data.get()
    email = entry_email.get()
    inserir_aluno(nome, data, email)
    label_status.config(text="Aluno cadastrado com sucesso!")

root = tk.Tk()
root.title("Cadastro de Alunos")

tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):").pack()
entry_data = tk.Entry(root)
entry_data.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Cadastrar", command=cadastrar).pack()

label_status = tk.Label(root, text="")
label_status.pack()

root.mainloop()
