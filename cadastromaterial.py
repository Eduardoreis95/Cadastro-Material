# 1) Importar as bibliotecas
# 2) criar interface gráfica:
    # - Descrição
    # Tipo da Unidade
    # - Quantidade do tipo da Unidade
# 3) Inteligencia da interface gráfica
    # - Função

# Importação das bibliotecas
import tkinter as tk
from tkinter import ttk
import datetime as dt

# Declarando variaveis
lista_tipos = ['Galão', 'Caixa', 'Saco', 'Unidade']
lista_codigos = []

janela = tk.Tk()

# Criação da função

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quantidade = entry_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao =  data_criacao.strftime('%d/%m/%Y %H:%M')
    codigo = len(lista_codigos)+1
    codigo_str = 'COD-{}'.format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quantidade, data_criacao))

# Titulo da Janela

janela.title('Ferramenta de cadastro de materiais')

# Label, Entry e Combobox

label_descricao = tk.Label(text='Descrição do Material')
label_descricao.grid(row=1, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

label_tipo_unidade = tk.Label(text='Tipo da unidade do Material')
label_tipo_unidade.grid(row=3, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx = 10, pady = 10, sticky='nswe', columnspan = 2)

label_quantidade = tk.Label(text='Quantidade na unidade de material')
label_quantidade.grid(row=4, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

botao_criar_codigo = tk.Button(text='Criar código', command=inserir_codigo())
botao_criar_codigo.grid(row=5, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 2)

janela.mainloop()

print(lista_codigos)
