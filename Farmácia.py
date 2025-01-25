import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta


# Conexão com o banco de dados
def conectar_banco():
    conexao = sqlite3.connect("estoque_medicamentos.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            vezes_dia INTEGER NOT NULL,
            data_reposicao TEXT
        )
    """)
    conexao.commit()
    conexao.close()


# Função para calcular a data de reposição
def calcular_data_reposicao(quantidade, vezes_dia):
    dias = quantidade // vezes_dia
    data_reposicao = datetime.now() + timedelta(days=dias)
    return data_reposicao.strftime("%d/%m/%Y")


# Salvar medicamento no banco
def salvar_medicamento():
    nome = entrada_nome.get()
    quantidade = entrada_quantidade.get()
    vezes_dia = entrada_vezes_dia.get()

    if not nome or not quantidade.isdigit() or not vezes_dia.isdigit():
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return

    quantidade = int(quantidade)
    vezes_dia = int(vezes_dia)
    data_reposicao = calcular_data_reposicao(quantidade, vezes_dia)

    conexao = sqlite3.connect("estoque_medicamentos.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO medicamentos (nome, quantidade, vezes_dia, data_reposicao)
        VALUES (?, ?, ?, ?)
    """, (nome, quantidade, vezes_dia, data_reposicao))
    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", "Medicamento salvo com sucesso!")
    limpar_campos()
    atualizar_lista()


# Atualizar lista de medicamentos
def atualizar_lista():
    conexao = sqlite3.connect("estoque_medicamentos.db")
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome, quantidade, vezes_dia, data_reposicao FROM medicamentos")
    registros = cursor.fetchall()
    conexao.close()

    lista_medicamentos.delete(0, tk.END)
    for registro in registros:
        lista_medicamentos.insert(tk.END, f"{registro[0]} - {registro[1]} - {
                                  registro[2]} comprimidos - {registro[3]}x/dia - Reposição: {registro[4]}")


# Limpar campos de entrada
def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_vezes_dia.delete(0, tk.END)


# Carregar medicamento para edição
def carregar_medicamento():
    try:
        selecionado = lista_medicamentos.get(lista_medicamentos.curselection())
        id_medicamento = selecionado.split(" - ")[0]

        conexao = sqlite3.connect("estoque_medicamentos.db")
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT nome, quantidade, vezes_dia FROM medicamentos WHERE id = ?", (id_medicamento,))
        medicamento = cursor.fetchone()
        conexao.close()

        limpar_campos()
        entrada_nome.insert(0, medicamento[0])
        entrada_quantidade.insert(0, medicamento[1])
        entrada_vezes_dia.insert(0, medicamento[2])

        # Guardar ID do medicamento para atualização
        global id_selecionado
        id_selecionado = id_medicamento
    except:
        messagebox.showerror("Erro", "Selecione um medicamento para editar.")


# Atualizar medicamento no banco
def atualizar_medicamento():
    nome = entrada_nome.get()
    quantidade = entrada_quantidade.get()
    vezes_dia = entrada_vezes_dia.get()

    if not nome or not quantidade.isdigit() or not vezes_dia.isdigit():
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return

    quantidade = int(quantidade)
    vezes_dia = int(vezes_dia)
    data_reposicao = calcular_data_reposicao(quantidade, vezes_dia)

    conexao = sqlite3.connect("estoque_medicamentos.db")
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE medicamentos
        SET nome = ?, quantidade = ?, vezes_dia = ?, data_reposicao = ?
        WHERE id = ?
    """, (nome, quantidade, vezes_dia, data_reposicao, id_selecionado))
    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", "Medicamento atualizado com sucesso!")
    limpar_campos()
    atualizar_lista()


# Excluir medicamento do banco
def excluir_medicamento():
    try:
        selecionado = lista_medicamentos.get(lista_medicamentos.curselection())
        id_medicamento = selecionado.split(" - ")[0]

        conexao = sqlite3.connect("estoque_medicamentos.db")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM medicamentos WHERE id = ?",
                       (id_medicamento,))
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Medicamento excluído com sucesso!")
        atualizar_lista()
    except:
        messagebox.showerror("Erro", "Selecione um medicamento para excluir.")


# Configuração da interface
conectar_banco()
janela = tk.Tk()
janela.title("Controle de Estoque de Medicamentos")

# Labels e campos de entrada
tk.Label(janela, text="Nome do Medicamento:").grid(
    row=0, column=0, pady=5, padx=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, pady=5, padx=5)

tk.Label(janela, text="Quantidade de Comprimidos:").grid(
    row=1, column=0, pady=5, padx=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.grid(row=1, column=1, pady=5, padx=5)

tk.Label(janela, text="Vezes ao Dia:").grid(row=2, column=0, pady=5, padx=5)
entrada_vezes_dia = tk.Entry(janela)
entrada_vezes_dia.grid(row=2, column=1, pady=5, padx=5)

# Botões
tk.Button(janela, text="Salvar Medicamento",
          command=salvar_medicamento).grid(row=3, column=0, pady=10)
tk.Button(janela, text="Carregar para Editar",
          command=carregar_medicamento).grid(row=3, column=1, pady=10)
tk.Button(janela, text="Atualizar Medicamento",
          command=atualizar_medicamento).grid(row=4, column=0, pady=10)
tk.Button(janela, text="Excluir Medicamento",
          command=excluir_medicamento).grid(row=4, column=1, pady=10)

# Lista de medicamentos
lista_medicamentos = tk.Listbox(janela, width=80)
lista_medicamentos.grid(row=5, column=0, columnspan=2, pady=10)

# Atualizar lista ao iniciar
atualizar_lista()

janela.mainloop()
