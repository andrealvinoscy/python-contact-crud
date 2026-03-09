# Tentativa crud 01
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="(removi)",
    database="agenda_contatos"
)

cursor = conexao.cursor()

#------------------------------------------------------------------------------
## ADICIONA CONTATOS (Obriga o usuario a digitar nome e um celular)

def add_contatos():
    nome_contato = input('Nome: ')
    while nome_contato == "":
        nome_contato = input('Nome é obrigatório. Digite novamente: ')

    email_contato = input('E-mail: ')

    celular_contato = input('Celular: ')
    while celular_contato == "":
        celular_contato = input('Celular é obrigatório. Digite novamente: ')
    
    telefone_contato = input('Telefone: ')

    sql = "INSERT INTO contatos (nome, email, celular, telefone) VALUES (%s, %s, %s, %s)"
    valores = (nome_contato, email_contato, celular_contato, telefone_contato)

    cursor.execute(sql, valores)
    conexao.commit()
#------------------------------------------------------------------------------
##BUSCA OS CONTATOS SALVOS NO SQL

def consulta_contatos():

    sql = "SELECT * FROM contatos;"
    cursor.execute(sql)
    lista = cursor.fetchall()
    
    #FORMATAÇÃO VISUAL
    print("ID | Nome | Celular")
    for contatos in lista:
        print(contatos[0], "|", contatos[1], "|", contatos[3])
    print("Contato adicionado com sucesso!")
#-------------------------------------------------------------------------------

def editar_contatos():
    consulta_contatos()
    #ESCOLHER O ID A PARTIR DA LISTA.
    
    escolha = int(input('Digite o ID do contato a ser editado ou digite 0 para sair: '))
    
    #SE A ESCOLHA FOR 0, A APLICAÇÃO DEVE ENCERRAR.
    
    if escolha == 0:
        return
    
    #NOVOS PARÂMETROS "N = NOVOS"
    
    n_nome = input('Digite o nome do contato: ')
    n_email = input('Digite o novo email do contato: ')
    n_celular = input('Digite o novo celular do contato: ')
    n_telefone = input('Digite o novo telefone do contato: ')

    #UPDATE NO SQL COM OS NOVOS PARÂMETROS
    
    sql = "UPDATE contatos SET nome = %s, email = %s, celular = %s, telefone = %s WHERE id = %s"
    n_value = (n_nome, n_email, n_celular, n_telefone, escolha)
    cursor.execute(sql, n_value)
    conexao.commit()
    print("Contato atualizado com sucesso!")

def remover_contato():
    consulta_contatos()
    
    escolha = int(input('Digite o ID do contato a ser removido: '))
    

    if escolha == 0:
        return
    
    confirmação = input('Tem certeza que deseja remover este contato? (s/n)').lower()
    if confirmação == 's':
        sql = "DELETE FROM contatos WHERE id = %s"
        valor = (escolha,)
        cursor.execute(sql, valor)
        conexao.commit()
       
        if cursor.rowcount > 0:
            print("Contato removido com sucesso!")
        else:
            print('ID não encontrado!')
    else:
        return
    

<<<<<<< HEAD
=======
add_contatos()
>>>>>>> b9eced97825a52f1b2c6426c5e9f68d5fdd0b400
