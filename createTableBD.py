##### Importar bibliotecas.
import sqlite3
from sqlite3 import Error

##### Criar função de CONEXÃO com o database.
def ConexaoBanco():
    caminho = "C:\\Users\\joaod\\projetos\\cadastroMedCompany\\medCompany.db"
    conex = None
    try:
        conex = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conex

##### Variável para inicializar a função. 
conect_db = ConexaoBanco()

##### Criar TABELA 
newTabSql = """CREATE TABLE IF NOT EXISTS Clientes( 
                NOME VARCHAR (100),
                DATA NASCIMENTO DATE,  
                IDADE INTEGER,
                SEXO VARCHAR (20),
                ESTADO CIVIL VARCHAR (20),
                CPF INTEGER,
                RG INTEGER,
                MAE VARCHAR (100),
                ENDERECO VARCHAR (150),
                NUMERO INTEGER,
                MUNICIPIO VARCHAR (100),
                BAIRRO VARCHAR (100),
                CEP NUMBER,
                FONE NUMBER,
                CELULAR NUMBER,
                EMAIL VARCHAR (100)        
                )"""

##### Criar função CURSOR 
def createTab (conexao, sql):
    try:
        cursor=conexao.cursor()
        cursor.execute(sql)
        print('Tabela Criada')     
    except Error as ex:
        print(ex)

##### Chamando as funções e criando tabela no database.
createTab(conect_db, newTabSql)   


