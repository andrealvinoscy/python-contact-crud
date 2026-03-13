# Tentativa crud 01
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="removi",
    database="agenda_contatos"
)

cursor = conexao.cursor()

#------------------------------------------------------------------------------
## ADICIONA CONTATOS (Obriga o usuario a digitar nome e um celular)

def add_contatos():

    print("=== ADICIONAR CONTATOS ===")

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

    print("Contato adicionado com sucesso!")
#------------------------------------------------------------------------------
##BUSCA OS CONTATOS SALVOS NO SQL

def consulta_contatos():
    
    print("=== CONSULTAR CONTATOS ===")

    sql = "SELECT * FROM contatos;"
    cursor.execute(sql)
    lista = cursor.fetchall()
    
    if not lista:
        print("Nenhum contato cadastrado.")
        return
    #FORMATAÇÃO VISUAL
    print("ID | Nome | Celular")
    for contatos in lista:
        print(contatos[0], "|", contatos[1], "|", contatos[3])
#-------------------------------------------------------------------------------

def editar_contatos():

    print("=== EDITAR CONTATOS ===")

    consulta_contatos()
    #ESCOLHER O ID A PARTIR DA LISTA.
    
    try:
        escolha = int(input('Digite o ID do contato a ser editado: '))
    except ValueError:
        print("""ID de contato inválido!
              Deseja ver a lista novamente?
              """)
        
        escolha_invalida = (input('S/N').upper())
        if escolha_invalida == 'S':
            consulta_contatos()
        
        return
    
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

#REMOÇÃO DE CONTATOS DA LISTA
def remover_contato():

    print('=== REMOVER CONTATOS ===')

    consulta_contatos()
    
    try:
        escolha = int(input('Digite o ID do contato a ser removido: '))
    except ValueError:
        print("""ID de contato inválido!
              Deseja ver a lista novamente?
              """)
        
        escolha_invalida = (input('S/N').upper())
        if escolha_invalida == 'S':
            consulta_contatos()
        
        return
            


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

def menu_inicial():
    print("""
    ==== Menu de Contatos ====
    1- Consultar Contatos
    2- Adicionar Contatos
    3- Atualizar Contatos
    4- Remover Contatos
    0- Sair

    """)
#Menu inicial
while True:  
    
    try:
        menu_inicial()
        escolha_menu = int(input(":"))
    except ValueError:
        print("Digite somente números!")
        continue

    if escolha_menu == 1:
        consulta_contatos()

    elif escolha_menu == 2:
        add_contatos()

    elif escolha_menu == 3:
        editar_contatos()

    elif escolha_menu == 4:
        remover_contato()

    elif escolha_menu == 0:
        print("Saindo...")
        cursor.close()
        conexao.close()
        break
    else:
        print("Opção inválida, tente novamente")
    