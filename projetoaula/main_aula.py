# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================
from Validacao import Validacao
import os
import getpass
from login import *
#===============================================================================
from edicao_usuario import *        #SO PARA ADM FAZER AMANHA
#_______________________________________________________________________________________________________________
#____________________________________________________________________________________FUNCAO PRINT NA TELA COMECO

def print_reservas_prof(cpf_prof): 
    cursor.execute("select * from reservas where professor_reserva='%s'" %(cpf_prof))
    global lista_reserva_ID
    lista_reserva_ID =[]
    lista_predioID = []
    lista_localID = []
    lista_data = []
    lista_disciplinaID = []
    lista_hora = []
    
    for row in cursor.fetchall(): #pega ID
        lista_reserva_ID.append(row[0])
        lista_predioID.append(row[1])
        lista_localID.append(row[2])
        lista_data.append(row[3])
        lista_disciplinaID.append(row[4])
        lista_hora.append(row[6])
        
    
    lista_predioNOME = []
    lista_localNOME = []
    lista_disciplinaNOME = []
    lista_cursoNOME = []

    for j in range (len(lista_predioID)): #pega nome do predio
        cursor.execute("select * from predios where id_predio='%s'" %(lista_predioID[j]))
        
        for row in cursor.fetchall():
            lista_predioNOME.append(row[1])
            
            
    for j in range (len(lista_localID)): #pega nome do local
        cursor.execute("select * from locais where id_local='%s'" %(lista_localID[j]))
        
        for row in cursor.fetchall():
            lista_localNOME.append(row[1])
            
    for j in range (len(lista_disciplinaID)): #pega nome da disciplina
        cursor.execute("select * from disciplinas where id_disciplina='%s'" %(lista_disciplinaID[j]))
        
        for row in cursor.fetchall():
            lista_disciplinaNOME.append(row[1])
            lista_cursoNOME.append(row[2])

    print "                      RESERVAS.\n"
    print "item   ano-mes-dia    hora     predio local    Disciplina\n"  
    for i in range (len(lista_reserva_ID)):
        print "[%.2d]   %s  as  %.2d h    %s  %s    %s - %s  " %(i+1,lista_data[i],lista_hora[i],lista_predioNOME[i],lista_localNOME[i],lista_disciplinaNOME[i],lista_cursoNOME[i])
    
    danone = input("\nDigite o item a ser excluido: ")
    return lista_reserva_ID[danone-1]

def print_disciplinas(CURSO):
    cursor.execute("select * from disciplinas where curso_disciplina='%s'" %(CURSO))
    lista_disciplinas_ID=[]
    lista_disciplinas_Nome=[]
    for row in cursor.fetchall():
            lista_disciplinas_ID.append(row[0])
            lista_disciplinas_Nome.append(row[1])
    print "  ID      NOME"
    for i in range (len(lista_disciplinas_ID)):
        print "["+lista_disciplinas_ID[i]+"] - "+lista_disciplinas_Nome[i]
    
def print_predios():
    cursor.execute("select * from predios")
    lista_predios_ID=[]
    lista_predios_Nome=[]
    for row in cursor.fetchall():
        lista_predios_ID.append(row[0])
        lista_predios_Nome.append(row[1])
    print "  ID      NOME"
    for i in range (len(lista_predios_ID)):
        print "["+lista_predios_ID[i]+"] - "+lista_predios_Nome[i]
        
def print_cursos():                                                    #Novo print 12/06
    cursor.execute("select * from cursos")
    lista_cursos_ID=[]
    lista_cursos_Nome=[]
    for row in cursor.fetchall():
        lista_cursos_ID.append(row[0])
        lista_cursos_Nome.append(row[1])
    print "  ID      NOME"
    for i in range (len(lista_cursos_ID)):
        print "["+lista_cursos_ID[i]+"] - "+lista_cursos_Nome[i]
        
def print_departamentos():                                             #Novo print 12/06
    cursor.execute("select * from departamentos")
    lista_departamentos_ID=[]
    lista_departamentos_Nome=[]
    for row in cursor.fetchall():
        lista_departamentos_ID.append(row[0])
        lista_departamentos_Nome.append(row[1])
    print "  ID      NOME"
    for i in range (len(lista_departamentos_ID)):
        print "["+lista_departamentos_ID[i]+"] - "+lista_departamentos_Nome[i]
        
def print_local(predio_reserva):
    cursor.execute("select * from locais where predio_local='%s'" %(predio_reserva))
    lista_locais_ID=[]
    lista_locais_Nome=[]
    lista_locais_Tipo=[]
    for row in cursor.fetchall():
        lista_locais_ID.append(row[0])
        lista_locais_Nome.append(row[1])
        lista_locais_Tipo.append(row[2])
    print " ID     NOME     TIPO"
    for i in range (len(lista_locais_ID)):
        print "["+lista_locais_ID[i]+"] - "+lista_locais_Nome[i]+" - "+lista_locais_Tipo[i]

#__________________________________________________FUNCAO PRINT NA TELA FIM

inicio=0
while inicio == 0:
    print "\n                         AULA.\n"
    choice=input("[1] Pesquisa  [2] Login  [3] Sair\nDigite: ")
    if choice > 3 or choice <1:
        os.system("cls")
        print "[ERRO 000] Op��o inv�lida. Tente novamente\n"
    else:
#____________________________________________________________________SEARCH
        if choice == 1:
            os.system("cls")
            print "\n                     PESQUISA.\n"
#____________________________________________________________________SEARCH

                        #INICIO DO LOGIN--------->>>>>> main_PROF and main_ADM
        if choice == 2:
            os.system("cls")
            print "\n                         LOGIN.\n"
            
            Login = Login_professor()
            end=0
            while end == 0:
                cpf = raw_input("Digite o login (CPF): ")
                verificar_CPF = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(cpf)
                existe = cursor.execute(verificar_CPF)
                if existe < 1:
                    print "Usuario n�o existente."
                    continue
                else:
                    Login.prof_CPF(cpf)
                    acesso = False
                    while acesso == False:
                        senha = getpass.getpass(prompt="Digite sua senha: ")
                        verificar_senha = "select usuario_cpf='%s' from usuarios where senha='%s'" %(cpf,senha)
                        executar = cursor.execute(verificar_senha)
                        if executar < 1:
                            print "Senha incorreta."
                        else:
                            acesso = True
                            Login.userSenha(senha)
                    if acesso == True:
                        cursor.execute("SELECT * FROM usuarios where usuario_cpf='%s'" %(cpf))
                        for row in cursor.fetchall():
                            classe_user = row[2]
            
                        if classe_user == 1:
                            os.system("cls")
                            print "Bem vindo, ADMINISTRADOR" #PAINEL DO ADMIN
    
############################# MAIN_ADM ################################

                            inicio_ADM = 0
                            while inicio_ADM == 0:
                                print "\n                     PAINEL DO ADMINISTRADOR.\n"    
                                
                                choice=input("Gerenciar:\n1 - Predios\n2 - Departamentos\n3 - Cursos\n4 - Disciplinas\n5 - Professores\n6 - Sair\n->")
                               
                                if choice > 6 or choice <1:
                                    print "[ERRO 001] Op��o inv�lida. Tente novamente\n"
                                else:
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                                    if choice == 1:
                                        os.system("cls")
                                        print "\n                   GERENCIAR PREDIOS.\n"
                                        
                                        choice2=input("Digite:\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice2 > 4 or choice <1:
                                            print "[ERRO 001] Op��o inv�lida. Tente novamente\n"
                                        else:
                                            saida = None
                                            while saida <> "s":
                                                if choice2 == 1:
                                                    os.system("cls")
                                                    print "\n                   ADICIONAR PREDIO.\n"
                                                    
                                                    id_predio = raw_input('Digite o ID do predio: ')
                                                    nome_predio = raw_input("Digite o nome do predio: ")
                                                    sql = "insert into predios values('%s','%s')" %(id_predio, nome_predio)
                                                    try:
                                                        cursor.execute(sql)
                                                        db.commit()
                                                        print "Novo predio cadastrado com sucesso."
                                                    except:
                                                        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
                                                        db.rollback()
                                                        
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")                   
#ADD PREDIO 100% PERFEITO by Gustavo_____________________________________________________________________
                                                if choice2 == 2:
                                                    os.system("cls")
                                                    print "\n                   EDITAR PREDIO.\n"
                                                    
                                                    print_predios()
                                                    
                                                    id_predio = raw_input('\nDigite o ID do predio que deseja editar: ')
                                                    verificar_predio = "select id_predio from predios where id_predio='%s'" %(id_predio)
                                                    existe = cursor.execute(verificar_predio)
                                                    if existe < 1:
                                                        print "[ERRO 005] ID n�o existente."
                                                        continue
                                                    else:
                                                        opcao = input("\nDigite: [1] Editar o ID    [2] Editar o nome\n->")
                                                        if opcao > 2 or opcao < 1:
                                                            print "[ERRO 004] Op��o incorreta."
                                                            continue
                                                        else:
                                                            if opcao == 1:
                                                                id_novo = raw_input("Digite o novo ID do predio: ")
                                                                
                                                                sql = "update predios set id_predio='%s' where id_predio='%s'" %(id_novo, id_predio)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "ID do predio editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()
        
                                                            if opcao == 2:
                                                                nome_predio = raw_input("Digite o novo nome do predio: ")
                                                                
                                                                sql = "update predios set nome_predio='%s' where id_predio='%s'" %(nome_predio, id_predio)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "Nome do predio editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()
                                    
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")                                                    
#EDITAR PREDIO 100% PERFEITO by Gustavo____________________________________________________________________
                                                if choice2 == 3:
                                                    os.system("cls")
                                                    print "\n                   EXCLUIR PREDIO.\n"
                                                    
                                                    print_predios()

                                                    deletado = raw_input('\nDigite o ID do predio que deseja excluir: ')
                                                    verificar_predio = "select id_predio from predios where id_predio='%s'" %(deletado)
                                                    existe = cursor.execute(verificar_predio)
                                                    if existe < 1:
                                                        print "Predio n�o existente."
                                                        continue
                                                    else:                                            
                                                        sql = "delete from predios where id_predio='%s'" %(deletado)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Predio excluido com sucesso."
                                                        except:
                                                            print "Erro na exclus�o."
                                                            db.rollback()
                                                        
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#EXCLUIR PREDIO 100% PERFEITO by Gustavo____________________________________________________________________

                                                if choice2 == 4:
                                                    os.system("cls")
                                                    print "\n                   EXIT.\n"
                                                    saida = "s"
                                                    
                                                os.system("cls")
                                        
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#

                                    if choice == 2:
                                        os.system("cls")
                                        print "\n                   GERENCIAR DEPARTAMENTOS.\n"
                                        
                                        choice3=input("Digite:\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice3 > 4 or choice <1:
                                            print "[ERRO 001] Op��o inv�lida. Tente novamente\n"
                                        else:
                                            saida = None
                                            while saida <> "s":
                                                if choice3 == 1:
                                                    os.system("cls")
                                                    print "\n                   ADICIONAR DEPARTAMENTO.\n"

                                                    id_departamento = raw_input('Digite o ID do departamento: ')
                                                    nome = raw_input("Digite o nome do departamento: ")
                                                    coordenador = raw_input("Digite o nome do coordenador: ")
                                                    
                                                    sql = "insert into departamentos values('%s','%s','%s')" %(id_departamento, nome, coordenador)
                                                    try:
                                                        cursor.execute(sql)
                                                        db.commit()
                                                        print "Departamento cadastrado com sucesso."
                                                    except:
                                                        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
                                                        db.rollback()
                                                    
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#ADD DEPARTAMENTO 100% PERFEITO by Gustavo____________________________________________________________________                                               
                                                    
                                                if choice3 == 2:
                                                    os.system("cls")
                                                    print "\n                   EDITAR DEPARTAMENTO.\n"
                                                    
                                                    print_departamentos()
                                                    
                                                    id_dep = raw_input('\nDigite o ID do departamento que deseja editar: \n')
                                                    verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(id_dep)
                                                    existe = cursor.execute(verificar_dep)
                                                    if existe < 1:
                                                        print "[ERRO 005] ID n�o existente."
                                                        continue
                                                    else:
                                                        opcao = input("Digite:\n1 (editar id)     2 (editar nome)     3 (editar coordenador)\n-> ")
                                                        if opcao > 3 or opcao < 1:
                                                            print "[ERRO 004] Op��o incorreta."
                                                            continue
                                                        else:
                                                            if opcao == 1:
                                                                id_novo = raw_input("Digite o novo ID do departamento: ")
                                                                sql = "update departamentos set id_departamento='%s' where id_departamento='%s'" %(id_novo, id_dep)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "ID editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()
                                                                
                                                            if opcao == 2:
                                                                nome = raw_input("Digite o novo nome do departamento: ")
                                                                sql = "update departamentos set nome_departamento='%s' where id_departamento='%s'" %(nome, id_dep)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "Nome editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()
                                                                
                                                            if opcao == 3:
                                                                coordenador = raw_input("Digite o nome do novo coordenador: ")
                                                                sql = "update departamentos set coordenador='%s' where id_departamento='%s'" %(coordenador, id_dep)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "Coordenador editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()

                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#EDITAR DEPARTAMENTO 100% PERFEITO by Gustavo____________________________________________________________________                                                      
                                                    
                                                if choice3 == 3:
                                                    os.system("cls")
                                                    print "\n                   EXCLUIR DEPARTAMENTO.\n"
                                                    print_departamentos()
                                                    deletado = raw_input('\nDigite o ID do departamento que deseja excluir: ')
                                                    verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(deletado)
                                                    existe = cursor.execute(verificar_dep)
                                                    if existe < 1:
                                                        print "Departamento n�o existente."
                                                        continue
                                                    else:
                                                        sql = "delete from departamentos where id_departamento='%s'" %(deletado)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Departamento excluido com sucesso."
                                                        except:
                                                            print "Erro na exclus�o, h� professores ou cursos atrelados ao departamento."
                                                            db.rollback()
                                                        
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#EXCLUIR DEPARTAMENTO 100% PERFEITO by Gustavo____________________________________________________________________ 
                                                if choice3 == 4:
                                                    os.system("cls")
                                                    print "\n                   EXIT.\n"
                                                    saida = "s"
                                            
                                                os.system("cls")
                                        
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#

                                    if choice == 3:
                                        os.system("cls")
                                        print "\n                   GERENCIAR CURSOS.\n"
                                        
                                        choice4=input("Digite:\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice4 > 4 or choice <1:
                                            print "[ERRO 001] Op��o inv�lida. Tente novamente\n"
                                        else:
                                            saida = None
                                            while saida <> "s":

                                                if choice4 == 1:
                                                    os.system("cls")
                                                    print "\n                   ADICIONAR CURSO.\n"
                                                    
                                                    id_curso = raw_input("\nDigite o ID do curso: ")
                                                    verificar_curso = "select id_curso from cursos where id_curso='%s'" %(id_curso)
                                                    existe = cursor.execute(verificar_curso)
                                                    if existe > 0:
                                                        print "Curso j� existe."
                                                        continue
                                                    else:
                                                        nome_curso = raw_input("Digite o nome do curso: ")
                                                        os.system("cls")
                                                        print_departamentos()
                                                        departamento_curso = raw_input("\nDigite o ID do departamento do curso: ")

                                                        sql = "insert into cursos values('%s','%s','%s')"%(id_curso, nome_curso, departamento_curso)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Curso cadastrado com sucesso."
                                                        except:
                                                            print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
                                                            db.rollback()
                                                                                                            
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#ADICIONAR CURSO 100% PERFEITO by Gustavo____________________________________________________________________

                                                if choice4 == 2:
                                                    os.system("cls")
                                                    print "\n                   EDITAR CURSO.\n"
                                                    print_cursos()
                                                    
                                                    id_curso = raw_input('\nDigite o ID do curso que deseja editar: ')
                                                    verificar_curso = "select id_curso from cursos where id_curso='%s'" %(id_curso)
                                                    existe = cursor.execute(verificar_curso)
                                                    if existe < 1:
                                                        print "ID n�o existente."
                                                        continue
                                                    else:
                                                        opcao = input("\nEDITAR:\n1 (ID)     2 (NOME)     3 (DEPARTAMENTO)\n-> ")
                                                        if opcao > 3 or opcao < 1:
                                                            print "Op��o incorreta."
                                                            continue
                                                        else:
                                                            if opcao == 1:
                                                                id_novo = raw_input("\nDigite o novo ID do curso: ")
                                                                
                                                                sql = "update cursos set id_curso='%s' where id_curso='%s'" %(id_novo, id_curso)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "ID editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente ou existe disciplinas e aulas relacionadas com esse curso."
                                                                    db.rollback()
                                                                
                                                            if opcao == 2:
                                                                nome = raw_input("\nDigite o novo nome do curso: ")
                                                                
                                                                sql = "update cursos set nome_curso='%s' where id_curso='%s'" %(nome, id_curso)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "Nome do curso editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()
                                                                
                                                            if opcao == 3:
                                                                os.system("cls")
                                                                print_departamentos()
                                                                departamento = raw_input("\nDigite o ID do novo departamento: ")
                                                                os.system("cls")
                                                                verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(departamento)
                                                                existe = cursor.execute(verificar_dep)
                                                                if existe < 1:
                                                                    print "Departamento n�o existente."
                                                                else:
                                                                    sql = "update cursos set departamento_curso='%s' where id_curso='%s'" %(departamento, id_curso)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Departamento do curso editado com sucesso."
                                                                    except:
                                                                        print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                        db.rollback()

                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#EDITAR CURSO 100% PERFEITO by Gustavo____________________________________________________________________
                                            
                                                if choice4 == 3:
                                                    os.system("cls")
                                                    print "\n                   EXCLUIR CURSO.\n"
                                                    print_cursos()
                                                    
                                                    deletado = raw_input('\nDigite o ID do curso que deseja excluir: ')
                                                    verificar_curso = "select id_curso from cursos where id_curso='%s'" %(deletado)
                                                    existe = cursor.execute(verificar_curso)
                                                    if existe < 1:
                                                        print "Curso n�o existente." #Mudar esse erro e definir um padrao TESTERS
                                                        continue
                                                    else:
                                                        sql = "delete from cursos where id_curso='%s'" %(deletado)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Curso excluido com sucesso."
                                                        except:
                                                            print "Erro na exclus�o. Verifique se existe disciplinas e aulas relacionadas com esse curso"
                                                            db.rollback()

                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#EXCLUIR CURSO 100% PERFEITO by Gustavo____________________________________________________________________
                                     
                                                if choice4 == 4:
                                                    os.system("cls")
                                                    print "\n                   EXIT.\n"
                                                    saida = "s"
                                            
                                                os.system("cls")                                                           
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                
                                    if choice == 4:
                                        os.system("cls")
                                        print "\n                   GERENCIAR DISCIPLINAS.\n"
                                        
                                        choice5=input("Digite:\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice5 > 4 or choice <1:
                                            print "[ERRO 001] Op��o inv�lida. Tente novamente\n"
                                        else:
                                            saida = None
                                            while saida <> "s":
                                                if choice5 == 1:
                                                    os.system("cls")
                                                    print "\n                   ADICIONAR DISCIPLINA.\n"
                                                    
                                                    id_disciplina = raw_input("Digite o ID da disciplina: ")
                                                    verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(id_disciplina)
                                                    existe = cursor.execute(verificar_dis)
                                                    if existe > 0:
                                                        print "Disciplina j� existente."
                                                        continue
                                                    else:
                                                        nome_disciplina = raw_input("Digite o nome da disciplina: ")
                                                        os.system("cls")
                                                        print_cursos()                                          
                                                        curso_disciplina = raw_input("Digite o curso da disciplina: ")
                                                        os.system("cls")
                                                        sql = "insert into disciplinas values('%s','%s','%s')"%(id_disciplina, nome_disciplina, curso_disciplina)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Disciplina cadastrada com sucesso."
                                                        except:
                                                            print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
                                                            db.rollback()
                                                                                                            
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#ADICIONAR DISCIPLINA 100% PERFEITO by Gustavo____________________________________________________________________
                                                 
                                                if choice5 == 2:
                                                    os.system("cls")
                                                    print "\n                   EDITAR DISCIPLINA.\n"
                                                    
                                                    print_cursos()
                                                    CURSO = raw_input("\nDigite o ID do curso da disciplina: ")
                                                    os.system("cls")
                                                    print_disciplinas(CURSO)
                                                    
                                                    id_disciplina = raw_input('\nDigite o ID da disciplina que deseja editar: ')
                                                    verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(id_disciplina)
                                                    existe = cursor.execute(verificar_dis)
                                                    if existe < 1:
                                                        print "ID n�o existente."
                                                        continue
                                                    else:
                                                        opcao = input("Digite:\n 1 (ID), 2 (NOME) ou 3 (CURSO): ")
                                                        if opcao > 3 or opcao < 1:
                                                            print "Op��o incorreta."
                                                            continue
                                                        else:
                                                            if opcao == 1:
                                                                id_novo = raw_input("Digite o novo ID da disciplina: ")

                                                                sql = "update disciplinas set id_disciplina='%s' where id_disciplina='%s'" %(id_novo, id_disciplina)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "ID editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()
  
                                                            if opcao == 2:
                                                                nome = raw_input("Digite o novo nome da disciplina: ")
                                                                sql = "update disciplinas set nome_disciplina='%s' where id_disciplina='%s'" %(nome, id_disciplina)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "Nome da disciplina editado com sucesso."
                                                                except:
                                                                    print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                    db.rollback()
                                                                
                                                            if opcao == 3:
                                                                os.system("cls")
                                                                print_cursos()   
                                                                curso = raw_input("Digite o id do novo curso: ")
                                                                os.system("cls")
                                                                verificar_curso = "select id_curso from cursos where id_curso='%s'" %(curso)
                                                                existe = cursor.execute(verificar_curso)
                                                                if existe < 1:
                                                                    print "Curso n�o existente."
                                                                else:
                                                                    sql = "update disciplinas set curso_disciplina='%s' where id_disciplina='%s'" %(curso, id_disciplina)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Curso da disciplina editado com sucesso."
                                                                    except:
                                                                        print "Erro na edi��o. Por favor verifique se os campos foram inseridos corretamente."
                                                                        db.rollback()
                                    
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#EDITAR DISCIPLINA 100% PERFEITO by Gustavo____________________________________________________________________                                               
                                                
                                                if choice5 == 3:
                                                    os.system("cls")
                                                    print "\n                   EXCLUIR DISCIPLINA.\n"
                                                    
                                                    print_cursos()
                                                    CURSO = raw_input("\nDigite o ID do curso da disciplina: ")
                                                    os.system("cls")
                                                    print_disciplinas(CURSO)
                                                    
                                                    deletado = raw_input('\nDigite o ID da disciplina que deseja excluir: ')
                                                    verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(deletado)
                                                    existe = cursor.execute(verificar_dis)
                                                    if existe < 1:
                                                        print "Disciplina n�o existente."
                                                        continue
                                                    else:
                                                        sql = "delete from disciplinas where id_disciplina='%s'" %(deletado)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Disciplina excluida com sucesso."
                                                        except:
                                                            print "Erro na exclus�o."
                                                            db.rollback()
                                                                                                            
                                                    saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
#EXCLUIR DISCIPLINA 100% PERFEITO by Gustavo____________________________________________________________________                                                                                              

                                                if choice5 == 4:
                                                    os.system("cls")
                                                    print "\n                   EXIT.\n"
                                                    saida = "s"
                                                os.system("cls")  
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                                    if choice == 5:
                                        os.system("cls")
                                        print "\n                   GERENCIAR PROFESSORES.\n"
                                        
                                        choice6=input("Digite:\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice6 > 4 or choice <1:
                                            print "[ERRO 001] Op��o inv�lida. Tente novamente\n"
                                        else:
                                            saida = None
                                            while saida <> "s":

#ESSE E DIFICIL VOU DEIXAR PRA DEPOIS
#
#
#
#
#
#
#
#
#
#
#
#
#ESSE E DIFICIL VOU DEIXAR PRA DEPOIS

                                                saida = raw_input('\nDigite s para sair ou ENTER para continuar excluindo: ')
                                                saida = saida.lower()
                                                os.system("cls")
                                        
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                             
                                    if choice == 6:
                                        os.system("cls")
                                        print "\n                   LOG OFF.\n"
                                        inicio_ADM = 1

                                os.system("cls")                          
                                        
                                        
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                         
                            
############################# MAIN_ADM FIM ################################                            
                            
                            
############################# MAIN_PROF ################################
                        else:
                            os.system("cls")
                            cursor.execute("select * from professores where id_professor='%s'" %(cpf))
                            nome_usuario = ""
                            for row in cursor.fetchall():
                                nome_usuario = row[1]
                            print "Bem vindo, Professor %s" %(nome_usuario)
                            inicio_prof=0
                            while inicio_prof == 0:
                                print "\n                     PAINEL DO PROFESSOR.\n"
                                choice=input("Digite:\n1 - Fazer Reserva\n2 - Deletar Reserva\n3 - Alterar senha\n4 - Sair\n->")
                                if choice > 4 or choice <1:
                                    print "[ERRO 001] Op��o inv�lida. Tente novamente\n"
                                else:
                            
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#

                                    if choice == 1:
                                        os.system("cls")
                                        print "\n                   FAZER RESERVA.\n"
                                        
                                        saida = None
                                        while saida <> "s":
                                            Test = Validacao()
                                            
                                            print_predios()
                                            predio_reserva = raw_input("\n\nDigite o ID do pr�dio da reserva ")
                                            os.system("cls")
                                            
                                            print_local(predio_reserva)
                                            local_reserva = raw_input("\n\nDigite o ID do local da reserva: ")
                                            os.system("cls")
                                            
                                            data = raw_input("Digite a data da reserva ano-mes-dia (0000-00-00) ")
                                            os.system("cls")
                                            
                                            professor_reserva = cpf
                                            
#############################################print_disciplinas(professor_reserva)
                                            #Fazer disciplinas apenas do professor
                                            disciplina_reserva = raw_input("\n\nDigite o ID da disciplina da reserva: ")
                                
                                            os.system("cls")
                                            print "Digite a hora da reserva (funcionamento das 7 as 22 horas)\n"
                                            hora1 = input("Inicio: ")
                                            hora2 = input("Fim: ")
                                            
#############################################Fazer verificacao de horario negativo ou fora do funcionamento
                                            
                                            count_erros = 0
                                            nova_reserva = 0
                                            
                                            for horario in range (hora1,hora2,1):
                                                hora = str(horario)
                                                id_reserva = hora+"_"+data+"_"+predio_reserva+"_"+local_reserva
                                                
                                                verificar_reserva = "select id_reserva from reservas where id_reserva='%s'" %(id_reserva)
                                                existe = cursor.execute(verificar_reserva)
                                                if existe < 1:
                                                    print "[LIVRE]      %s horas" %(hora)
                                                    continue
                                                else:
                                                    print "[RESERVADO]  %s horas"%(hora)
                                                    count_erros = count_erros + 1
                                                    
                                            while count_erros != 0:
                                                Resposta = input("\n1 - Continuar\n2 - Alterar reserva\n3 - Sair\n->")
                                                os.system("cls")
                                                if Resposta == 1:
                                                    count_erros = 0
                                                elif Resposta == 2:
                                                    nova_reserva = 1
                                                    count_erros = 0
                                                elif Resposta == 3:
                                                    nova_reserva = 3
                                                    count_erros = 0
                                                    saida = "s"
                                                else:
                                                    print "[ERRO 004] Opcao invalida"
                                            else:
                                                if nova_reserva == 1:
                                                    continue
                                                elif nova_reserva == 0:
                                                    #cadastrarReserva
                                                    for horario in range (hora1,hora2,1):
                                                        hora = str(horario)
                                                        id_reserva = hora+"_"+data+"_"+predio_reserva+"_"+local_reserva
                                                        sql = "insert into reservas values('%s','%s','%s', '%s', '%s', '%s', '%d')"%(id_reserva, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, horario)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Cadastro efetuado com sucesso as %s horas" %(hora)
                                                        except:
                                                            print "[ERRO 002] Reserva j� existente para %s horas." %(hora)
                                                            db.rollback()
                                                    #cadastrarReserva
                                                else:
                                                    saida="s"
                                            saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                            saida = saida.lower()
                                            os.system("cls")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                                    if choice == 2:
                                        os.system("cls")
                                        print "\n               DELETAR RESERVA.\n"
                                        saida = None
                                        while saida <> "s":              
                                            cursor.execute("select * from reservas where professor_reserva='%s'" %(cpf))
                                            lista_reserva_ID =[]
                                            lista_predioID = []
                                            lista_localID = []
                                            lista_data = []
                                            lista_disciplinaID = []
                                            lista_hora = []
                                            
                                            for row in cursor.fetchall(): #pega ID
                                                lista_reserva_ID.append(row[0])
                                                lista_predioID.append(row[1])
                                                lista_localID.append(row[2])
                                                lista_data.append(row[3])
                                                lista_disciplinaID.append(row[4])
                                                lista_hora.append(row[6])
                                            
                                            lista_predioNOME = []
                                            lista_localNOME = []
                                            lista_disciplinaNOME = []
                                            lista_cursoNOME = []
                                        
                                            for j in range (len(lista_predioID)): #pega nome do predio
                                                cursor.execute("select * from predios where id_predio='%s'" %(lista_predioID[j]))
                                                
                                                for row in cursor.fetchall():
                                                    lista_predioNOME.append(row[1])
                                                    
                                            for j in range (len(lista_localID)): #pega nome do local
                                                cursor.execute("select * from locais where id_local='%s'" %(lista_localID[j]))
                                                
                                                for row in cursor.fetchall():
                                                    lista_localNOME.append(row[1])
                                                    
                                            for j in range (len(lista_disciplinaID)): #pega nome da disciplina
                                                cursor.execute("select * from disciplinas where id_disciplina='%s'" %(lista_disciplinaID[j]))
                                                
                                                for row in cursor.fetchall():
                                                    lista_disciplinaNOME.append(row[1])
                                                    lista_cursoNOME.append(row[2])
                                        
                                            print "                      RESERVAS.\n"
                                            print "item   ano-mes-dia    hora     predio local    Disciplina\n"  
                                            for i in range (len(lista_reserva_ID)):
                                                print "[%.2d]   %s  as  %.2d h    %s  %s    %s - %s  " %(i+1,lista_data[i],lista_hora[i],lista_predioNOME[i],lista_localNOME[i],lista_disciplinaNOME[i],lista_cursoNOME[i])
                                            
                                            danosse = input("\nDigite o item a ser excluido ou 0 para sair: ")
                                            
                                            if danosse == 0:
                                                saida = "s"
                                            else:
                                                del_reserva = lista_reserva_ID[danosse-1]
                                                sql = "delete from reservas where id_reserva='%s'" %(del_reserva)
                                                try:
                                                    cursor.execute(sql)
                                                    db.commit()
                                                    print "Reserva excluida com sucesso."
                                                except:
                                                    print "Erro na exclus�o, n�o existe reserva nesse hor�rio."
                                                    db.rollback()
                                                                                                
                                            saida = raw_input('\nDigite s para sair ou ENTER para continuar excluindo: ')
                                            saida = saida.lower()
                                            os.system("cls")
                                                
                                        print "    FINISH"
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                                    if choice == 3:
                                        os.system("cls")
                                        print "\n                  ALTERAR SENHA.\n"
                                        teste = Validacao()
                                        senha1 = teste.SENHA_Check(getpass.getpass(prompt="Digite a nova senha do usuario: "))
                                        senha2 = teste.SENHA_Check(getpass.getpass(prompt="Confirme a nova senha do usuario: "))
                                        if senha1 == senha2:
                                            editarSenha(cursor, senha1, cpf)
                                        else:
                                            print "[ERRO 003] Senhas diferentes"                            
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                            
                                    if choice == 4:
                                        os.system("cls")
                                        inicio_prof = 1
                                        print "\n                      LOG OFF.\n"
                                os.system("cls")
                    end=1
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
        
        if choice == 3:
            os.system("cls")
            inicio = 1
            print "\n             PROGRAMA FINALIZADO.\n"
            db.close()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
  