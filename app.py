import tkinter as tk
import sqlite3
import pandas as pd

# ________________________________FUNÇÃO CADASTRAR CLIENTES BANCO DE DADOS________________________________#
def cadastroClientes():
    conexao = sqlite3.connect('medCompany.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO Clientes VALUES (:nome, :nascimento, :idade, :sexo, :estadocivil,:cpf, :rg, :nome_mae, :endereco, :numero, :municipio, :bairro, :cep, :fone, :celular, :email)",
    {
        'nome':entry_nome.get(),
        'nascimento':entry_nascimento.get(),
        'idade':entry_idade.get(),
        'sexo':entry_sexo.get(),
        'estadocivil':entry_estadocivil.get(),
        'cpf': entry_cpf.get(),
        'rg':entry_rg.get(),
        'nome_mae':entry_nome_mae.get(),
        'endereco':entry_endereco.get(),
        'numero':entry_numero.get(),
        'municipio':entry_municipio.get(),
        'bairro':entry_bairro.get(),
        'cep':entry_cep.get(),
        'fone':entry_fone.get(),
        'celular':entry_celular.get(),
        'email':entry_email.get()
    }
    )
    conexao.commit()
    conexao.close()
    
    ## Limpando dados do terminal 

    entry_nome.delete(0,"end")
    entry_nascimento.delete(0,"end")
    entry_idade.delete(0,"end")
    entry_sexo.delete(0,"end")
    entry_estadocivil.delete(0,"end")
    entry_cpf.delete(0,"end")
    entry_rg.delete(0,"end")
    entry_nome_mae.delete(0,"end")
    entry_endereco.delete(0,"end")
    entry_numero.delete (0,"end")
    entry_municipio.delete(0,"end")
    entry_bairro.delete(0,"end")
    entry_cep.delete(0,"end")
    entry_fone.delete(0,"end")
    entry_celular.delete(0,"end")
    entry_email.delete(0,"end")

# ________________________________FUNÇÃO EXPORTAR CLIENTES EXCEL__________________________________________#
def exportarExcel():
    conexao = sqlite3.connect('medCompany.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Clientes")
    clientes_cadastrados = cursor.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns = ['Nome', 'Data Nascimento', 'Idade', 'Sexo','Estado Civil','CPF', 'RG', 'Nome da Mãe', 'Endereço', 'Numero', 'Municipio', 'Bairro', 'CEP', 'Telefone',
    'Celular', 'E-mail'])
    clientes_cadastrados.to_excel('Banco_de_dados.xlsx')

    conexao.commit()
    conexao.close()
## Janela Tkinter


window = tk.Tk()

#### Título da janela 
window.title('Cadastro de Pacientes')
window.wm_resizable(width=False, height=False)
window.iconbitmap(default='med_med.ico')

## Campos
label_titulo = tk.Label(text='DADOS DO PACIENTE')
label_titulo.grid(row=1, column=0, padx=10, pady=10, stick='nswe',columnspan=6)

##

label_nome = tk.Label(text='Nome')
label_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_nome = tk.Entry()
entry_nome.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=5)

## 

label_nascimento = tk.Label(text='Data de Nascimento')
label_nascimento.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_nascimento = tk.Entry()
entry_nascimento.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

##

label_idade = tk.Label(text='Idade')
label_idade.grid(row=3, column=3, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_idade = tk.Entry()
entry_idade.grid(row=3, column=4, padx=10, pady=10, sticky='nswe', columnspan=2)

##

label_sexo = tk.Label(text='Sexo')
label_sexo.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_sexo = tk.Entry()
entry_sexo.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

##

label_estadocivil = tk.Label(text='Estado Civil')
label_estadocivil.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_estadocivil = tk.Entry()
entry_estadocivil.grid(row=4, column=3, padx=10, pady=10, sticky='nswe', columnspan=3)

##

label_cpf = tk.Label(text='CPF')
label_cpf.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_cpf = tk.Entry()
entry_cpf.grid(row=5, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

##

label_rg = tk.Label(text='RG')
label_rg.grid(row=5, column=3, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_rg = tk.Entry()
entry_rg.grid(row=5, column=4, padx=10, pady=10, sticky='nswe', columnspan=2)

##

label_nome_mae = tk.Label(text='Nome da mãe')
label_nome_mae.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_nome_mae = tk.Entry()
entry_nome_mae.grid(row=6, column=1, padx=10, pady=10, sticky='nswe', columnspan=5)

##

label_endereco = tk.Label(text='Endereço')
label_endereco.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_endereco = tk.Entry()
entry_endereco.grid(row=8, column=1, padx=10, pady=10, sticky='nswe', columnspan=3)

##

label_numero = tk.Label(text='Nº')
label_numero.grid(row=8, column=4, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_numero = tk.Entry()
entry_numero.grid(row=8, column=5, padx=10, pady=10, sticky='nswe', columnspan=1)

##

label_municipio = tk.Label(text='Municipio')
label_municipio.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_municipio = tk.Entry()
entry_municipio.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

##

label_bairro = tk.Label(text='Bairro')
label_bairro.grid(row=9, column=2, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_bairro = tk.Entry()
entry_bairro.grid(row=9, column=3, padx=10, pady=10, sticky='nswe', columnspan=1)

##

label_cep = tk.Label(text='CEP')
label_cep.grid(row=9, column=4, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_cep = tk.Entry()
entry_cep.grid(row=9, column=5, padx=10, pady=10, sticky='nswe', columnspan=1)

##

label_fone = tk.Label(text='Tel Contato')
label_fone.grid(row=10, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_fone = tk.Entry()
entry_fone.grid(row=10, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

##

label_celular = tk.Label(text='Tel Celular')
label_celular.grid(row=10, column=3, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_celular = tk.Entry()
entry_celular.grid(row=10, column=4, padx=10, pady=10, sticky='nswe', columnspan=2)

##

label_email = tk.Label(text='E-mail')
label_email.grid(row=11, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_email = tk.Entry()
entry_email.grid(row=11, column=1, padx=10, pady=10, sticky='nswe', columnspan=5)


#### Criar botões

botao_salvar = tk.Button(text='Salvar',command=cadastroClientes)
botao_salvar.grid(row=12, column=0, padx=10, pady=10, sticky='nswe', columnspan=6)

botao_fechar = tk.Button(text='Exportar Clientes',command=exportarExcel)
botao_fechar.grid(row=13, column=0, padx=10, pady=10, sticky='nswe', columnspan=6)

window.mainloop()