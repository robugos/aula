# -*- coding: utf-8 -*-
#===============================================================================
import MySQLdb
db = MySQLdb.connect("aula.myftp.org","yoshi","mario1234","auladb")
cursor = db.cursor()
#===============================================================================
from Validacao import *
import os
import getpass
from datetime import datetime
from Prints import *
from Search import *
#===============================================================================PRINTS
show = prints()
inicio=0
while inicio == 0:
    print "+-----------------------------------------------+"
    print "|                    AULA                       |"
    print "+-----------------------------------------------+"
    choice=input("\n1 (PESQUISA)  2 (LOGIN)  3 (UPDATE)  4 (SAIR)\n\nDigite: ")
    if choice > 4 or choice <1:
        os.system("cls")
        print "+-----------------------------------------------+"
        print "|                    AULA                       |"
        print "+-----------------------------------------------+"
        ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida.\n\tPressione ENTER para continuar.\n")
        os.system("cls")
    else:
#____________________________________________________________________SEARCH
        if choice == 1:
            os.system("cls")
            print "+-----------------------------------------------+"
            print "|                  PESQUISA                     |"
            print "+-----------------------------------------------+\n"
            pesquisa = Search()
            pesquisa.openPESQUISA()
#____________________________________________________________________SEARCH
    
                        #INICIO DO LOGIN--------->>>>>> main_PROF and main_ADM
        if choice == 2:
            os.system("cls")
            Login = Login_professor()
            end=0
            while end == 0:
                print "+-----------------------------------------------+"
                print "|                    LOGIN                      |"
                print "+-----------------------------------------------+"
                cpf = raw_input("\nDigite o login (CPF): ")
                verificar_CPF = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(cpf)
                existe = cursor.execute(verificar_CPF)
                if existe < 1:
                    os.system("cls")
                    print "+-----------------------------------------------+"
                    print "|                    LOGIN                      |"
                    print "+-----------------------------------------------+"
                    ERRO_AULA = raw_input("\n\t[ERRO 002] Usuario nao existente.\n\tPressione ENTER para continuar.\n")
                    os.system("cls")
                else:
                    Login.prof_CPF(cpf)
                    acesso = False
                    while acesso == False:
                        os.system("cls")
                        print "+-----------------------------------------------+"
                        print "|                    LOGIN                      |"
                        print "+-----------------------------------------------+"
                        senha = getpass.getpass(prompt="\nDigite sua senha: ")
                        verificar_senha = "select usuario_cpf='%s' from usuarios where senha='%s'" %(cpf,senha)
                        executar = cursor.execute(verificar_senha)
                        if executar < 1:
                            os.system("cls")
                            print "+-----------------------------------------------+"
                            print "|                    LOGIN                      |"
                            print "+-----------------------------------------------+"
                            ERRO_AULA = raw_input("\n\t[ERRO 003] Senha incorreta.\n\tPressione ENTER para continuar.\n")
                            os.system("cls")
                        else:
                            acesso = True
                            Login.userSenha(senha)
                    if acesso == True:
                        cursor.execute("SELECT * FROM usuarios where usuario_cpf='%s'" %(cpf))
                        for row in cursor.fetchall():
                            classe_user = row[2]
            
                        if classe_user == 1:
                            os.system("cls")
    
############################# MAIN_ADM ################################
    
                            inicio_ADM = 0
                            while inicio_ADM == 0:
                                os.system("cls")  
                                print "+-----------------------------------------------+"
                                print "|            PAINEL DO ADMINISTRADOR            |"
                                print "+-----------------------------------------------+"
                                choicea=input("\nGerenciar:\n\n1 - Predios\n2 - Departamentos\n3 - Cursos\n4 - Disciplinas\n5 - Professores\n6 - Sair\n->")
                               
                                if choicea > 6 or choicea <1:
                                    os.system("cls")
                                    print "+-----------------------------------------------+"
                                    print "|            PAINEL DO ADMINISTRADOR            |"
                                    print "+-----------------------------------------------+"
                                    ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida.\n\tPressione ENTER para continuar.\n")
                                else:
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                                    if choicea == 1:
                                        os.system("cls")
                                        print "+-----------------------------------------------+"
                                        print "|               GERENCIAR PREDIOS               |"
                                        print "+-----------------------------------------------+"
                                        choice2=input("\nDigite:\n\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice2 > 4 or choice2 <1:
                                            os.system("cls")
                                            print "+-----------------------------------------------+"
                                            print "|               GERENCIAR PREDIOS               |"
                                            print "+-----------------------------------------------+"
                                            ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida.\n\tPressione ENTER para continuar.\n")
                                        else:
                                            saida = None
                                            while saida <> "s":
                                                if choice2 == 1:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|               ADICIONAR PREDIO                |"
                                                    print "+-----------------------------------------------+"
                                                    id_predio = raw_input('\nDigite o ID do predio ou 0 para sair: ')
                                                    if id_predio == "0":
                                                        saida = "s"
                                                        os.system('cls')
                                                    else:
                                                        os.system("cls")
                                                        print "+-----------------------------------------------+"
                                                        print "|               ADICIONAR PREDIO                |"
                                                        print "+-----------------------------------------------+"
                                                        nome_predio = raw_input("\nDigite o nome do predio: ")
                                                        sql = "insert into predios values('%s','%s')" %(id_predio, nome_predio)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Novo predio cadastrado com sucesso."
                                                        except:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|               ADICIONAR PREDIO                |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 006] Erro no cadastro.\n\tPressione ENTER para continuar.\n")
                                                            db.rollback()
                                                            
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")                   
#ADD PREDIO 100% PERFEITO by Gustavo_____________________________________________________________________
                                                if choice2 == 2:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                 EDITAR PREDIO                 |"
                                                    print "+-----------------------------------------------+\n"
                                                    show.print_predios()
                                                    
                                                    id_predio = raw_input('\nDigite o ID do predio que deseja editar ou 0 para sair: ')
                                                    if id_predio == "0":
                                                        saida = "s"
                                                        os.system('cls')
                                                    else:
                                                        verificar_predio = "select id_predio from predios where id_predio='%s'" %(id_predio)
                                                        existe = cursor.execute(verificar_predio)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                 EDITAR PREDIO                 |"
                                                            print "+-----------------------------------------------+\n"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] ID nao existente.\n\tPressione ENTER para continuar.\n")
                                                            continue
                                                        else:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                 EDITAR PREDIO                 |"
                                                            print "+-----------------------------------------------+"
                                                            opcao = input("\nDigite: 1 (EDITAR ID)    2 (EDITAR NOME)\n->")
                                                            if opcao > 2 or opcao < 1:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                 EDITAR PREDIO                 |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida.\n\tPressione ENTER para continuar.\n")
                                                                continue
                                                            else:
                                                                if opcao == 1:
                                                                    id_novo = raw_input("\nDigite o novo ID do predio: ")
                                                                    
                                                                    sql = "update predios set id_predio='%s' where id_predio='%s'" %(id_novo, id_predio)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "ID do predio editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PREDIO                 |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
            
                                                                if opcao == 2:
                                                                    nome_predio = raw_input("\nDigite o novo nome do predio: ")
                                                                    
                                                                    sql = "update predios set nome_predio='%s' where id_predio='%s'" %(nome_predio, id_predio)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Nome do predio editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PREDIO                 |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                        
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")                                                    
#EDITAR PREDIO 100% PERFEITO by Gustavo____________________________________________________________________
                                                if choice2 == 3:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                EXCLUIR PREDIO                 |"
                                                    print "+-----------------------------------------------+\n"
                                                    show.print_predios()
    
                                                    deletado = raw_input('\nDigite o ID do predio que deseja excluir ou 0 para sair: ')
                                                    if deletado == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        verificar_predio = "select id_predio from predios where id_predio='%s'" %(deletado)
                                                        existe = cursor.execute(verificar_predio)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                EXCLUIR PREDIO                 |"
                                                            print "+-----------------------------------------------+"
                                                            print "\n\t[ERRO 002] Predio nao existente.\n\tPressione ENTER para continuar.\n"
                                                        else:                                            
                                                            sql = "delete from predios where id_predio='%s'" %(deletado)
                                                            try:
                                                                cursor.execute(sql)
                                                                db.commit()
                                                                print "Predio excluido com sucesso."
                                                            except:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                EXCLUIR PREDIO                 |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao.\n\tPressione ENTER para continuar.\n")
                                                                db.rollback()
                                                            
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#EXCLUIR PREDIO 100% PERFEITO by Gustavo____________________________________________________________________
    
                                                if choice2 == 4:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                     EXIT                      |"
                                                    print "+-----------------------------------------------+"
                                                    saida = "s"
                                                    
                                                os.system("cls")
                                        
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
    
                                    if choicea == 2:
                                        os.system("cls")
                                        print "+-----------------------------------------------+"
                                        print "|            GERENCIAR DEPARTAMENTOS            |"
                                        print "+-----------------------------------------------+"
                                        
                                        choice3=input("\nDigite:\n\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice3 > 4 or choice3 <1:
                                            os.system("cls")
                                            print "+-----------------------------------------------+"
                                            print "|            GERENCIAR DEPARTAMENTOS            |"
                                            print "+-----------------------------------------------+"
                                            ERRO_AULA= raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                        else:
                                            saida = None
                                            while saida <> "s":
                                                if choice3 == 1:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|            ADICIONAR DEPARTAMENTO             |"
                                                    print "+-----------------------------------------------+"
                                                    id_departamento = raw_input('\nDigite o ID do departamento ou 0 para sair: ')
                                                    if id_departamento == "0":
                                                        saida = "s"
                                                        os.system('cls')
                                                    else:
                                                        os.system("cls")
                                                        print "+-----------------------------------------------+"
                                                        print "|            ADICIONAR DEPARTAMENTO             |"
                                                        print "+-----------------------------------------------+"
                                                        nome = raw_input("\nDigite o nome do departamento: ")
                                                        coordenador = raw_input("Digite o nome do coordenador: ")
                                                        
                                                        sql = "insert into departamentos values('%s','%s','%s')" %(id_departamento, nome, coordenador)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                            print "Departamento cadastrado com sucesso."
                                                        except:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|            ADICIONAR DEPARTAMENTO             |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 006] Erro no cadastro. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                            db.rollback()
                                                        
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#ADD DEPARTAMENTO 100% PERFEITO by Gustavo____________________________________________________________________                                               
                                                    
                                                if choice3 == 2:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|              EDITAR DEPARTAMENTO              |"
                                                    print "+-----------------------------------------------+\n"
                                                    
                                                    show.print_departamentos()
                                                    
                                                    id_dep = raw_input('\nDigite o ID do departamento ou 0 para sair: \n')
                                                    if id_dep == "0":
                                                        saida = "s"
                                                        os.system('cls')
                                                    else:
                                                        os.system('cls')
                                                        verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(id_dep)
                                                        existe = cursor.execute(verificar_dep)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|              EDITAR DEPARTAMENTO              |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] ID nao existente.\n\tPressione ENTER para continuar.\n")
                                                        else:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|              EDITAR DEPARTAMENTO              |"
                                                            print "+-----------------------------------------------+"
                                                            opcao = input("\nEDITAR:\n\n1 (ID)     2 (NOME)     3 (COORDENADOR)\n-> ")
                                                            if opcao > 3 or opcao < 1:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|              EDITAR DEPARTAMENTO              |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida.\n\tPressione ENTER para continuar.\n")
                                                            else:
                                                                if opcao == 1:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|              EDITAR DEPARTAMENTO              |"
                                                                    print "+-----------------------------------------------+"
                                                                    id_novo = raw_input("Digite o novo ID do departamento: ")
                                                                    sql = "update departamentos set id_departamento='%s' where id_departamento='%s'" %(id_novo, id_dep)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "ID editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|              EDITAR DEPARTAMENTO              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                    
                                                                if opcao == 2:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|              EDITAR DEPARTAMENTO              |"
                                                                    print "+-----------------------------------------------+"
                                                                    nome = raw_input("\nDigite o novo nome do departamento: ")
                                                                    sql = "update departamentos set nome_departamento='%s' where id_departamento='%s'" %(nome, id_dep)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Nome editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|              EDITAR DEPARTAMENTO              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        continue
                                                                        db.rollback()
                                                                    
                                                                if opcao == 3:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|              EDITAR DEPARTAMENTO              |"
                                                                    print "+-----------------------------------------------+"
                                                                    coordenador = raw_input("\nDigite o nome do novo coordenador: ")
                                                                    sql = "update departamentos set coordenador='%s' where id_departamento='%s'" %(coordenador, id_dep)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Coordenador editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|              EDITAR DEPARTAMENTO              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
    
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#EDITAR DEPARTAMENTO 100% PERFEITO by Gustavo____________________________________________________________________                                                      
                                                    
                                                if choice3 == 3:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|              EXCLUIR DEPARTAMENTO             |"
                                                    print "+-----------------------------------------------+\n"
                                                    show.print_departamentos()
                                                    deletado = raw_input('\nDigite o ID do departamento ou 0 para sair: ')
                                                    if deletado == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(deletado)
                                                        existe = cursor.execute(verificar_dep)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|              EXCLUIR DEPARTAMENTO             |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] Departamento nao existente.\n\tPressione ENTER para continuar.\n")
                                                        else:
                                                            sql = "delete from departamentos where id_departamento='%s'" %(deletado)
                                                            try:
                                                                cursor.execute(sql)
                                                                db.commit()
                                                                print "Departamento excluido com sucesso."
                                                            except:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|              EXCLUIR DEPARTAMENTO             |"
                                                                print "+-----------------------------------------------+\n"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao.Ha professores ou cursos atrelados ao departamento.\n\tPressione ENTER para continuar.\n") 
                                                                db.rollback()
                                                            
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#EXCLUIR DEPARTAMENTO 100% PERFEITO by Gustavo____________________________________________________________________ 
                                                if choice3 == 4:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                      EXIT                     |"
                                                    print "+-----------------------------------------------+"
                                                    saida = "s"
                                            
                                                os.system("cls")
                                        
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
    
                                    if choicea == 3:
                                        os.system("cls")
                                        print "+-----------------------------------------------+"
                                        print "|               GERENCIAR CURSOS                |"
                                        print "+-----------------------------------------------+"
                                        
                                        choice4=input("\nDigite:\n\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice4 > 4 or choice4 <1:
                                            os.system("cls")
                                            print "+-----------------------------------------------+"
                                            print "|               GERENCIAR CURSOS                |"
                                            print "+-----------------------------------------------+"
                                            ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n") 
                                        else:
                                            saida = None
                                            while saida <> "s":
    
                                                if choice4 == 1:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                ADICIONAR CURSO                |"
                                                    print "+-----------------------------------------------+"
                                                    
                                                    id_curso = raw_input("\nDigite o ID do curso ou 0 para sair: ")
                                                    if id_curso == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        verificar_curso = "select id_curso from cursos where id_curso='%s'" %(id_curso)
                                                        existe = cursor.execute(verificar_curso)
                                                        if existe > 0:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                ADICIONAR CURSO                |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 005] Curso ja existente.\n\tPressione ENTER para continuar.\n") 
                                                            continue
                                                        else:
                                                            nome_curso = raw_input("Digite o nome do curso: ")
                                                            os.system("cls")
                                                           
                                                            print "+-----------------------------------------------+"
                                                            print "|                ADICIONAR CURSO                |"
                                                            print "+-----------------------------------------------+\n"
                                                            show.print_departamentos()
                                                            departamento_curso = raw_input("\nDigite o ID do departamento do curso: ")
    
                                                            sql = "insert into cursos values('%s','%s','%s')"%(id_curso, nome_curso, departamento_curso)
                                                            try:
                                                                cursor.execute(sql)
                                                                db.commit()
                                                                print "Curso cadastrado com sucesso."
                                                            except:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                ADICIONAR CURSO                |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 006] Erro no cadastro.\n\tPressione ENTER para continuar.\n")
                                                                db.rollback()
                                                                                                                
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#ADICIONAR CURSO 100% PERFEITO by Gustavo____________________________________________________________________
    
                                                if choice4 == 2:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                  EDITAR CURSO                 |"
                                                    print "+-----------------------------------------------+\n"
                                                    show.print_cursos()
                                                    
                                                    id_curso = raw_input('\nDigite o ID do curso ou 0 para sair: ')
                                                    if id_curso == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        verificar_curso = "select id_curso from cursos where id_curso='%s'" %(id_curso)
                                                        existe = cursor.execute(verificar_curso)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                  EDITAR CURSO                 |"
                                                            print "+-----------------------------------------------+\n"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] Curso nao existente.\n\tPressione ENTER para continuar.\n") 
                                                        else:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                  EDITAR CURSO                 |"
                                                            print "+-----------------------------------------------+"
                                                            opcao = input("\nEDITAR:\n\n1 (ID)     2 (NOME)     3 (DEPARTAMENTO)\n-> ")
                                                            if opcao > 3 or opcao < 1:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                  EDITAR CURSO                 |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                                            else:
                                                                if opcao == 1:
                                                                    id_novo = raw_input("\nDigite o novo ID do curso: ")
                                                                    
                                                                    sql = "update cursos set id_curso='%s' where id_curso='%s'" %(id_novo, id_curso)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "ID editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                  EDITAR CURSO                 |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os itens foram inseridos corretamente ou existe disciplinas e aulas relacionadas com esse curso.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                    
                                                                if opcao == 2:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|                  EDITAR CURSO                 |"
                                                                    print "+-----------------------------------------------+"
                                                                    nome = raw_input("\nDigite o novo nome do curso: ")
                                                                    
                                                                    sql = "update cursos set nome_curso='%s' where id_curso='%s'" %(nome, id_curso)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Nome do curso editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                  EDITAR CURSO                 |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao.Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                    
                                                                if opcao == 3:
                                                                    os.system("cls")
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|                  EDITAR CURSO                 |"
                                                                    print "+-----------------------------------------------+\n"
                                                                    show.print_departamentos()
                                                                    departamento = raw_input("\nDigite o ID do novo departamento: ")
                                                                    os.system("cls")
                                                                    verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(departamento)
                                                                    existe = cursor.execute(verificar_dep)
                                                                    if existe < 1:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                  EDITAR CURSO                 |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 002] Departamento nao existente.\n\tPressione ENTER para continuar.\n")
                                                                    else:
                                                                        sql = "update cursos set departamento_curso='%s' where id_curso='%s'" %(departamento, id_curso)
                                                                        try:
                                                                            cursor.execute(sql)
                                                                            db.commit()
                                                                            print "Departamento do curso editado com sucesso."
                                                                        except:
                                                                            os.system("cls")
                                                                            print "+-----------------------------------------------+"
                                                                            print "|                  EDITAR CURSO                 |"
                                                                            print "+-----------------------------------------------+"
                                                                            ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                            db.rollback()
    
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#EDITAR CURSO 100% PERFEITO by Gustavo____________________________________________________________________
                                            
                                                if choice4 == 3:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                 EXCLUIR CURSO                 |"
                                                    print "+-----------------------------------------------+\n"
                                                    show.print_cursos()
                                                    
                                                    deletado = raw_input('\nDigite o ID do curso ou 0 para sair: ')
                                                    if deletado == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        verificar_curso = "select id_curso from cursos where id_curso='%s'" %(deletado)
                                                        existe = cursor.execute(verificar_curso)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                 EXCLUIR CURSO                 |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] Curso nao existente.\n\tPressione ENTER para continuar.\n") #Mudar esse erro e definir um padrao TESTERS
                                                            continue
                                                        else:
                                                            sql = "delete from cursos where id_curso='%s'" %(deletado)
                                                            try:
                                                                cursor.execute(sql)
                                                                db.commit()
                                                                print "Curso excluido com sucesso."
                                                            except:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                 EXCLUIR CURSO                 |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao.Verifique se existe disciplinas e aulas relacionadas com esse curso.\n\tPressione ENTER para continuar.\n") 
                                                                db.rollback()
    
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#EXCLUIR CURSO 100% PERFEITO by Gustavo____________________________________________________________________
                                     
                                                if choice4 == 4:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                     EXIT                      |"
                                                    print "+-----------------------------------------------+"
                                                    saida = "s"
                                            
                                                os.system("cls")                                                           
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                
                                    if choicea == 4:
                                        os.system("cls")
                                        print "+-----------------------------------------------+"
                                        print "|             GERENCIAR DISCIPLINAS             |"
                                        print "+-----------------------------------------------+"
                                        
                                        choice5=input("\nDigite:\n\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Sair\n->")
                                        if choice5 > 4 or choice5 <1:
                                            os.system("cls")
                                            print "+-----------------------------------------------+"
                                            print "|             GERENCIAR DISCIPLINAS             |"
                                            print "+-----------------------------------------------+"
                                            ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\t\tPressione ENTER para continuar\n")
                                        else:
                                            saida = None
                                            while saida <> "s":
                                                if choice5 == 1:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|             ADICIONAR DISCIPLINA              |"
                                                    print "+-----------------------------------------------+"
                                                    
                                                    id_disciplina = raw_input("\nDigite o ID da disciplina ou 0 para sair: ")
                                                    if id_disciplina == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        os.system("cls")
                                                        verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(id_disciplina)
                                                        existe = cursor.execute(verificar_dis)
                                                        if existe > 0:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|             ADICIONAR DISCIPLINA              |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 005] Disciplina ja existente.\n\tPressione ENTER para continuar.\n")
                                                            continue
                                                        else:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|             ADICIONAR DISCIPLINA              |"
                                                            print "+-----------------------------------------------+"
                                                            nome_disciplina = raw_input("\nDigite o nome da disciplina: ")
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|             ADICIONAR DISCIPLINA              |"
                                                            print "+-----------------------------------------------+\n"
                                                            show.print_cursos()                                          
                                                            curso_disciplina = raw_input("\nDigite o curso da disciplina: ")
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|             ADICIONAR DISCIPLINA              |"
                                                            print "+-----------------------------------------------+\n"
                                                            periodo = input("\nDigite o periodo da disciplina: ")
                                                            os.system("cls")
                                                            sql = "insert into disciplinas values('%s','%s','%s','%s')"%(id_disciplina, nome_disciplina, curso_disciplina,periodo)
                                                            try:
                                                                cursor.execute(sql)
                                                                db.commit()
                                                                print "Disciplina cadastrada com sucesso."
                                                            except:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|             ADICIONAR DISCIPLINA              |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 006] Erro no cadastro. Verifique se os itens foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                db.rollback()
                                                                                                                
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#ADICIONAR DISCIPLINA 100% PERFEITO by Gustavo____________________________________________________________________
                                                 
                                                if choice5 == 2:
                                                    os.system("cls")
                                             
                                                    print "+-----------------------------------------------+"
                                                    print "|               EDITAR DISCIPLINA               |"
                                                    print "+-----------------------------------------------+\n"
                                                    
                                                    show.print_cursos()
                                                    CURSO = raw_input("\nDigite o ID do curso da disciplina ou 0 para sair: ")
                                                    if CURSO == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        os.system("cls")
                                                        print "+-----------------------------------------------+"
                                                        print "|               EDITAR DISCIPLINA               |"
                                                        print "+-----------------------------------------------+\n"
                                                        show.print_disciplinas(CURSO)
                                                        
                                                        id_disciplina = raw_input('\nDigite o ID da disciplina que deseja editar: ')
                                                        verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(id_disciplina)
                                                        existe = cursor.execute(verificar_dis)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|               EDITAR DISCIPLINA               |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] ID nao existente. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                                        else:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|               EDITAR DISCIPLINA               |"
                                                            print "+-----------------------------------------------+"
                                                            opcao = input("\nEDITE:\n\n1 (ID)     2 (NOME)     3 (CURSO)\n-> ")
                                                            if opcao > 3 or opcao < 1:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|               EDITAR DISCIPLINA               |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                                            else:
                                                                if opcao == 1:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|               EDITAR DISCIPLINA               |"
                                                                    print "+-----------------------------------------------+"
                                                                    id_novo = raw_input("\nDigite o novo ID da disciplina: ")
    
                                                                    sql = "update disciplinas set id_disciplina='%s' where id_disciplina='%s'" %(id_novo, id_disciplina)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "ID editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|               EDITAR DISCIPLINA               |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Por favor verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
      
                                                                if opcao == 2:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|               EDITAR DISCIPLINA               |"
                                                                    print "+-----------------------------------------------+"
                                                                    nome = raw_input("\nDigite o novo nome da disciplina: ")
                                                                    sql = "update disciplinas set nome_disciplina='%s' where id_disciplina='%s'" %(nome, id_disciplina)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Nome da disciplina editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|               EDITAR DISCIPLINA               |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Por favor verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                    
                                                                if opcao == 3:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|               EDITAR DISCIPLINA               |"
                                                                    print "+-----------------------------------------------+\n"
                                                                    show.print_cursos()   
                                                                    curso = raw_input("\nDigite o id do novo curso: ")
                                                                    os.system("cls")
                                                                    verificar_curso = "select id_curso from cursos where id_curso='%s'" %(curso)
                                                                    existe = cursor.execute(verificar_curso)
                                                                    if existe < 1:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|               EDITAR DISCIPLINA               |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 002] Curso nao existente.\n\tPressione ENTER para continuar.\n")
                                                                    else:
                                                                        sql = "update disciplinas set curso_disciplina='%s' where id_disciplina='%s'" %(curso, id_disciplina)
                                                                        try:
                                                                            cursor.execute(sql)
                                                                            db.commit()
                                                                            print "Curso da disciplina editado com sucesso."
                                                                        except:
                                                                            os.system("cls")
                                                                            print "+-----------------------------------------------+"
                                                                            print "|               EDITAR DISCIPLINA               |"
                                                                            print "+-----------------------------------------------+"
                                                                            ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Por favor verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                            db.rollback()
                                        
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#EDITAR DISCIPLINA 100% PERFEITO by Gustavo____________________________________________________________________                                               
                                                
                                                if choice5 == 3:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|               EXCLUIR DISCIPLINA              |"
                                                    print "+-----------------------------------------------+\n"
                                                    
                                                    show.print_cursos()
                                                    CURSO = raw_input("\nDigite o ID do curso da disciplina ou 0 para sair: ")
                                                    if CURSO == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        os.system("cls")
                                                        print "+-----------------------------------------------+"
                                                        print "|               EXCLUIR DISCIPLINA              |"
                                                        print "+-----------------------------------------------+\n"
                                                        show.print_disciplinas(CURSO)
                                                        
                                                        deletado = raw_input('\nDigite o ID da disciplina que deseja excluir ou 0 para sair: ')
                                                        if deletado == "0":
                                                            saida = "s"
                                                            os.system('cls')
                                                        else:
                                                            verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(deletado)
                                                            existe = cursor.execute(verificar_dis)
                                                            if existe < 1:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|               EXCLUIR DISCIPLINA              |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 002] Disciplina nao existente.\n\tPressione ENTER para continuar.\n")
                                                                continue
                                                            else:
                                                                sql = "delete from disciplinas where id_disciplina='%s'" %(deletado)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                    print "Disciplina excluida com sucesso."
                                                                except:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|               EXCLUIR DISCIPLINA              |"
                                                                    print "+-----------------------------------------------+"
                                                                    ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao.\n\tPressione ENTER para continuar.\n")
                                                                    db.rollback()
                                                                                                                    
                                                                saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                                saida = saida.lower()
                                                                os.system("cls")
#EXCLUIR DISCIPLINA 100% PERFEITO by Gustavo____________________________________________________________________                                                                                              
    
                                                if choice5 == 4:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                     EXIT                      |"
                                                    print "+-----------------------------------------------+"
                                                    saida = "s"
                                                os.system("cls")  
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                                    if choicea == 5:
                                        os.system("cls")
                                        print "+-----------------------------------------------+"
                                        print "|            GERENCIAR PROFESSORES              |"
                                        print "+-----------------------------------------------+"
                                        
                                        choice6=input("\nDigite:\n\n1 - Adicionar\n2 - Editar\n3 - Excluir\n4 - Disciplinas\n5 - Sair\n->")
                                        if choice6 > 5 or choice6 <1:
                                            os.system("cls")
                                            print "+-----------------------------------------------+"
                                            print "|            GERENCIAR PROFESSORES              |"
                                            print "+-----------------------------------------------+"
                                            ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente\n\tPressione ENTER para continuar.\n")
                                        else:
                                            saida = None
                                            while saida <> "s":
#FAZENDO AGORA BY GUSTAVO
#________________________________________________________________________________________________________________________
    
                                                if choice6 == 1:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|              ADICIONAR PROFESSOR              |"
                                                    print "+-----------------------------------------------+"
    
                                                    Test = Validacao()
                                                    id_professor = raw_input("\nDigite o CPF do professor ou 0 para sair: ")
                                                    if id_professor == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        os.system("cls")
                                                        
                                                        print "+-----------------------------------------------+"
                                                        print "|              ADICIONAR PROFESSOR              |"
                                                        print "+-----------------------------------------------+"
                                                        id_professor = Test.CPF_Check(id_professor)
                                                        nome_professor = raw_input("\nDigite o nome do professor: ")
                                                        os.system("cls")
                                                        
                                                        print "+-----------------------------------------------+"
                                                        print "|              ADICIONAR PROFESSOR              |"
                                                        print "+-----------------------------------------------+\n"
                                                        show.print_departamentos()    
                                                        departamento_professor = raw_input("\nDigite o departamento do professor: ")
                                                        os.system("cls")
                                                        
                                                        #Cadastra o prof
                                                    
                                                        sql = "insert into professores values('%s','%s','%s')"%(id_professor, nome_professor, departamento_professor)
                                                        try:
                                                            cursor.execute(sql)
                                                            db.commit()
                                                        except:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|              ADICIONAR PROFESSOR              |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 006] Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                            db.rollback()
                                                            
                                                        #Cadastra o usuario
                                                        
                                                        classe = 0 #Classe 0 para professores
                                                        senha = "UFRPE1234" #DEFAULT 
                                                        sql = "insert into usuarios values('%s','%s','%s')"%(id_professor, senha, classe)
                                                        cursor.execute(sql)
                                                        db.commit()
                                                           
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")                                                
#________________________________________________________________________________________________________________________
    
                                                if choice6 == 2:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                 EDITAR PROFESSOR              |"
                                                    print "+-----------------------------------------------+\n"
                                                    teste = Validacao()
                                                    show.print_professores()
                                            
                                                    id_CPF = raw_input('\nDigite o CPF do usuario ou 0 para sair: ')
                                                    if id_CPF == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        os.system("cls")
                                                        verificar_user = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(id_CPF)
                                                        existe = cursor.execute(verificar_user)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                 EDITAR PROFESSOR              |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] Usuario nao existente.\n\tPressione ENTER para continuar.\n")
                                                            continue
                                                        else:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                 EDITAR PROFESSOR              |"
                                                            print "+-----------------------------------------------+"
                                                            opcao = input("\nEDITAR:\n\n1 (CPF)   2 (NOME)   3 (SENHA)   4 (CLASSE)\n->")
                                                            if opcao > 4 or opcao < 1:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                 EDITAR PROFESSOR              |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                                            else:
                                                                if opcao == 1:
                                                                    print "\nOpcao valida apenas para professores sem reservas e disciplinas.\n"
                                                                    id_novo = teste.CPF_Check(raw_input("Digite o novo CPF do usuario: "))
                                                                    sql = "update usuarios set usuario_cpf='%s' where usuario_CPF='%s'" %(id_novo, id_CPF)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "CPF editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PROFESSOR              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                    #muda ID do USUARIO do PROFESSOR
                                                                    sql = "update professores set id_professor='%s' where id_professor='%s'" %(id_novo, id_CPF)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "CPF editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PROFESSOR              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                        
                                                                    saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                                    saida = saida.lower()
                                                                    os.system("cls")
    
    
                                                                if opcao == 2:
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|                 EDITAR PROFESSOR              |"
                                                                    print "+-----------------------------------------------+"
                                                                    novo_nome = raw_input("\nDigite o nome do professor: ")
                                                                    sql = "update professores set nome_professor='%s' where id_professor='%s'" %(novo_nome, id_CPF)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Nome editado com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PROFESSOR              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                        
                                                                    saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                                    saida = saida.lower()
                                                                    os.system("cls")
    
                                                                if opcao == 3:
                                                                    os.system("cls")
                                                                    teste = Validacao()
                                                                    print "+-----------------------------------------------+"
                                                                    print "|                 EDITAR PROFESSOR              |"
                                                                    print "+-----------------------------------------------+"
                                                                    senha1 = teste.SENHA_Check(getpass.getpass(prompt="\nDigite a nova senha do usuario: "))
                                                                    senha2 = teste.SENHA_Check(getpass.getpass(prompt="\nCONFIRME: "))
                                                                    if senha1 == senha2:
                                                                        sql = "update usuarios set senha='%s' where usuario_cpf='%s'" %(senha1, id_CPF)
                                                                        try:
                                                                            cursor.execute(sql)
                                                                            db.commit()
                                                                            print "Senha editada com sucesso."
                                                                        except:
                                                                            os.system("cls")
                                                                            print "+-----------------------------------------------+"
                                                                            print "|                 EDITAR PROFESSOR              |"
                                                                            print "+-----------------------------------------------+"
                                                                            ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                            db.rollback()
                                                                    else:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PROFESSOR              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input ("\n\t[ERRO 003] Senha incorreta.\n")
                                                                        
                                                                    saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                                    saida = saida.lower()
                                                                    os.system("cls") 
    
                                                                if opcao == 4:  
                                                                    os.system("cls")
                                                                    print "+-----------------------------------------------+"
                                                                    print "|                 EDITAR PROFESSOR              |"
                                                                    print "+-----------------------------------------------+\n"
                                                                    show.print_professores()
                                                                    id_CPF = raw_input('\nDigite o CPF do usuario que deseja editar: ')
                                                                    os.system("cls")
                                                                    verificar_user = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(id_CPF)
                                                                    existe = cursor.execute(verificar_user)
                                                                    if existe < 1:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PROFESSOR              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 002] Usuario nao existente.\n\tPressione ENTER para continuar.\n")
                                                                        continue
                                                                    else:
                                                                        os.system("cls")
                                                                        print "+-----------------------------------------------+"
                                                                        print "|                 EDITAR PROFESSOR              |"
                                                                        print "+-----------------------------------------------+"
                                                                        classe = input("\nDigite o valor da nova classe (0 ou 1): ")
    
                                                                        if classe == 1 or classe == 0:
                                                                            sql = "update usuarios set classe='%d' where usuario_cpf='%s'" %(classe, id_CPF)
                                                                            try:
                                                                                cursor.execute(sql)
                                                                                db.commit()
                                                                                print "Classe editada com sucesso."
                                                                            except:
                                                                                os.system("cls")
                                                                                print "+-----------------------------------------------+"
                                                                                print "|                 EDITAR PROFESSOR              |"
                                                                                print "+-----------------------------------------------+"
                                                                                ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                                                db.rollback()
                                                                        else:
                                                                            os.system("cls")
                                                                            print "+-----------------------------------------------+"
                                                                            print "|                 EDITAR PROFESSOR              |"
                                                                            print "+-----------------------------------------------+" 
                                                                            ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n")                               
                                                                    saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                                    saida = saida.lower()
                                                                    os.system("cls")
#________________________________________________________________________________________________________________________
    
                                                if choice6 == 3:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                EXCLUIR PROFESSOR              |"
                                                    print "+-----------------------------------------------+"
                                
                                                    print "\nOBS: Opcao valida apenas para professores sem reservas e disciplinas.\n"
    
                                                    show.print_professores()
                                                    id_CPF = raw_input('\nDigite o CPF do professor ou 0 para sair: ')
                                                    if id_CPF == "0":
                                                        saida = "s"
                                                        os.system("cls")
                                                    else:
                                                        os.system("cls")                                                
                                                        verificar_user = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(id_CPF)
                                                        existe = cursor.execute(verificar_user)
                                                        if existe < 1:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                EXCLUIR PROFESSOR              |"
                                                            print "+-----------------------------------------------+"
                                                            ERRO_AULA = raw_input("\n\t[ERRO 002] Professor/Usuario nao existente.\n\tPressione ENTER para continuar.\n")
                                                        else:
                                                            
                                                            sql = "delete from usuarios where usuario_cpf='%s'" %(id_CPF)
                                                            try:
                                                                cursor.execute(sql)
                                                                db.commit()
                                                                print "Usuario excluido com sucesso."
                                                            except:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                EXCLUIR PROFESSOR              |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao.\n\tPressione ENTER para continuar.\n")
                                                                db.rollback()
            
                                                            sql = "delete from professores where id_professor='%s'" %(id_CPF)
                                                            try:
                                                                cursor.execute(sql)
                                                                db.commit()
                                                                print "Professor excluido com sucesso."
                                                            except:
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                EXCLUIR PROFESSOR              |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao. Ha um usuario atrelado ao professor.\n\tPressione ENTER para continuar.\n")
                                                                db.rollback()
                                              
                                                        saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                        saida = saida.lower()
                                                        os.system("cls")
#________________________________________________________________________________________________________________________
    
    
                                                if choice6 == 4:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|      GERENCIAR DISCIPLINAS DO PROFESSOR       |"
                                                    print "+-----------------------------------------------+\n"
                                                    show.print_professores()
                                                    cpf_professor = raw_input('\nDigite o CPF do professor: ')
                                                    os.system('cls')
                                                    print "+-----------------------------------------------+"
                                                    print "|      GERENCIAR DISCIPLINAS DO PROFESSOR       |"
                                                    print "+-----------------------------------------------+"
                                                    opcao_dis = input("\nDIGITE:\n\n1 (ADICIONAR)   2 (EXCLUIR)   3 (SAIR)\n->")
                                                    if opcao_dis > 3 or opcao_dis < 1:
                                                        os.system('cls')
                                                        print "+-----------------------------------------------+"
                                                        print "|      GERENCIAR DISCIPLINAS DO PROFESSOR       |"
                                                        print "+-----------------------------------------------+"
                                                        ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                                    else:
                                                        if opcao_dis == 1:
                                                            os.system('cls')
                                                            
                                                            print "+-----------------------------------------------+"
                                                            print "|             ADICIONAR DISCIPLINA              |"
                                                            print "+-----------------------------------------------+\n"
                                                            show.print_cursos()
                                                            CURSO = raw_input('\nDigite o ID do curso: ')
                                                            os.system('cls')
                                                            
                                                            saida=None
                                                            while saida <> "s":
                                                                print "+-----------------------------------------------+"
                                                                print "|             ADICIONAR DISCIPLINA              |"
                                                                print "+-----------------------------------------------+\n"
                                                                show.print_disciplinas(CURSO)
                                                                DISCIPLINA = raw_input('\nDigite o ID da disciplina: ')
                                                                os.system('cls')
                                                                id_docencia = cpf_professor+'_'+DISCIPLINA
                                                                sql = "insert into docencia values('%s','%s','%s')"%(id_docencia, cpf_professor, DISCIPLINA)
                                                                try:
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                                except:
                                                                    os.system('cls')
                                                            
                                                                    print "+-----------------------------------------------+"
                                                                    print "|             ADICIONAR DISCIPLINA              |"
                                                                    print "+-----------------------------------------------+"
                                                                    ERRO_AULA = raw_input("\n\t[ERRO 006] Erro no cadastro. O item foi digitado incorretamente ou a disciplina ja esta cadastrada.\n\tPressione ENTER para continuar.\n")
                                                                    db.rollback()
                                                                
                                                                
                                                                saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                                saida = saida.lower()
                                                                os.system("cls")
                                                        
                                                        if opcao_dis == 2: 
                                                            os.system("cls")
                                                           
                                                            print "+-----------------------------------------------+"
                                                            print "|               EXCLUIR DISCIPLINA              |"
                                                            print "+-----------------------------------------------+"
                                                            saida = None
                                                            while saida <> "s":              
                                                                cursor.execute("select * from docencia where id_professor='%s'" %(cpf_professor))
                                                                lista_disprof_ID = []
                                                                lista_disciplina_ID= []
                                                                
                                                                for row in cursor.fetchall(): #pega ID
                                                                    lista_disprof_ID.append(row[0])
                                                                    lista_disciplina_ID.append(row[2])
                                                                
                                                                lista_disciplina_NOME = []
                                                                lista_disciplina_DEP = []
                                                            
                                                                for j in range (len(lista_disciplina_ID)): #pega nome da disciplina
                                                                    cursor.execute("select * from disciplinas where id_disciplina='%s'" %(lista_disciplina_ID[j]))
                                                                    
                                                                    for row in cursor.fetchall():
                                                                        lista_disciplina_NOME.append(row[1])
                                                                        lista_disciplina_DEP.append(row[2])
    
                                                                print "\nITEM\tCURSO\tDISCIPLINA\n"
                                                                print "-------------------------------------------------"  
                                                                for i in range (len(lista_disciplina_ID)):
                                                                    print "[%.2d]\t%s\t%s" %(i+1,lista_disciplina_DEP[i],lista_disciplina_NOME[i])
                                                                print "-------------------------------------------------"
                                                                danosse = input("\nDigite o item a ser excluido ou 0 para sair: ")
                                                                
                                                                if danosse == 0:
                                                                    saida = "s"
                                                                else:
                                                                    del_disciplina = lista_disprof_ID[danosse-1]
                                                                    sql = "delete from docencia where id_docencia='%s'" %(del_disciplina)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Disciplina excluida com sucesso."
                                                                    except:
                                                                        os.system("cls")
                                                           
                                                                        print "+-----------------------------------------------+"
                                                                        print "|               EXCLUIR DISCIPLINA              |"
                                                                        print "+-----------------------------------------------+"
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao.\n\tPressione ENTER para continuar.\n")
                                                                        db.rollback()
                                                                                                                    
                                                                saida = raw_input('\nDigite (S) para sair ou ENTER para continuar excluindo: ')
                                                                saida = saida.lower()
                                                                os.system("cls")
                                                        
                                                        if opcao_dis == 3:
                                                            os.system("cls")
                                                            print "+-----------------------------------------------+"
                                                            print "|                      EXIT                     |"
                                                            print "+-----------------------------------------------+"
                                                            saida = "s"
                                                        os.system("cls") 
                                                        
#________________________________________________________________________________________________________________________
    
                                                if choice6 == 5:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                      EXIT                     |"
                                                    print "+-----------------------------------------------+"
                                                    saida = "s"
                                                os.system("cls")  
    
#________________________________________________________________________________________________________________________
    
                               
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                             
                                    if choicea == 6:
                                        os.system("cls")
                                        print "+-----------------------------------------------+"
                                        print "|                    LOG OFF                    |"
                                        print "+-----------------------------------------------+"
                                        inicio_ADM = 1
                                        end=1
                                os.system("cls")                          
                
                
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_# MAIN PROF
                        else:
                            os.system("cls")
                            cursor.execute("select * from professores where id_professor='%s'" %(cpf))
                            nome_usuario = ""
                            for row in cursor.fetchall():
                                nome_usuario = row[1]
                            
                            inicio_prof=0
                            while inicio_prof == 0:
                                os.system("cls")
                                print "+-----------------------------------------------+"
                                print "|              PAINEL DO PROFESSOR              |"
                                print "+-----------------------------------------------+"
                                print "Bem vindo, Professor %s\n" %(nome_usuario)
                                choicep=input("\nDigite:\n\n1 - Fazer Reserva\n2 - Deletar Reserva\n3 - Alterar senha\n4 - Sair\n->")
                                if choicep > 4 or choicep <1:
                                    os.system("cls")
                                    print "+-----------------------------------------------+"
                                    print "|              PAINEL DO PROFESSOR              |"
                                    print "+-----------------------------------------------+"
                                    ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                else:
                            
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
    
##### FAZER ERRO DA HORA #####
    
                                    if choicep == 1:
                                        os.system("cls")
                                       
                                        print "+-----------------------------------------------+"
                                        print "|                 FAZER RESERVA                 |"
                                        print "+-----------------------------------------------+"
                                        
                                        saida = None
                                        while saida <> "s":
                                            os.system("cls")
                                       
                                            print "+-----------------------------------------------+"
                                            print "|                 FAZER RESERVA                 |"
                                            print "+-----------------------------------------------+\n"
                                            is_today_the_future = False
                                            show.print_predios()
                                            predio_reserva = raw_input("\nDigite o ID do predio da reserva ou 0 para sair: ")
                                            if predio_reserva == "0":
                                                saida = "s"
                                                os.system("cls")
                                            else:
                                                os.system("cls")
                                                print "+-----------------------------------------------+"
                                                print "|                 FAZER RESERVA                 |"
                                                print "+-----------------------------------------------+\n"
                                                show.print_local(predio_reserva)
                                                local_reserva = raw_input("\nDigite o ID do local da reserva: ")
                                                os.system("cls")
                                                print "+-----------------------------------------------+"
                                                print "|                 FAZER RESERVA                 |"
                                                print "+-----------------------------------------------+"
                                                data = raw_input("\nDigite a data da reserva ano-mes-dia (0000-00-00) ")
                                                date = data
                                                year,month,day = date.split('-')
                                                DATARESERVA = day+"/"+month+"/"+year
                                                year,month,day = int(year),int(month),int(day)
                                                today = datetime.now()
                                                
                                                if year == today.year:                                                    
                                                    if today.month >= 1 and today.month <= 6:
                                                        if month == today.month:
                                                            if month == 1 or month == 3 or month == 5: # 31 dias
                                                                if day >= today.day and day <= 31:
                                                                    is_today_the_future = True
                                                            if month == 2:
                                                                if (year % 4) <> 0: # 28 dias
                                                                    if day >= today.day and day <= 28:
                                                                        is_today_the_future = True 
                                                                else: # 29 dias (bissexto)
                                                                    if day >= today.day and day <= 29:
                                                                        is_today_the_future = True     
                                                            else: # 30 dias
                                                                if day >= today.day and day <= 30:
                                                                    is_today_the_future = True
                                                                    
                                                        if month > today.month and month <= 6 and month >= 1:
                                                            if month == 1 or month == 3 or month == 5: # 31 dias
                                                                if day >= 1 and day <= 31:
                                                                    is_today_the_future = True
                                                            if month == 2:
                                                                if (year % 4) <> 0: # 28 dias
                                                                    if day >= 1 and day <= 28:
                                                                        is_today_the_future = True
                                                                else: # 29 dias (bissexto)
                                                                    if day >= 1 and day <= 29:
                                                                        is_today_the_future = True            
                                                            else: # 30 dias
                                                                if day >= 1 and day <= 30:
                                                                    is_today_the_future = True                                             
                                                    if today.month >= 7 and today.month <= 12:
                                                        if month == today.month:
                                                            if month == 7 or month == 8 or month == 10 or month == 12: # 31 dias
                                                                if day >= today.day and day <= 31:
                                                                    is_today_the_future = True
                                                            else: # 30 dias
                                                                if day >= today.day and day <= 30:
                                                                    is_today_the_future = True
                                                        if month > today.month and month <= 12 and month >= 7:
                                                            if month == 7 or month == 8 or month == 10 or month == 12: # 31 dias
                                                                if day >= 1 and day <= 31:
                                                                    is_today_the_future = True                                                                    
                                                            else: # 30 dias
                                                                if day >= 1 and day <= 30:
                                                                    is_today_the_future = True
                                                
                                                if is_today_the_future == True:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                 FAZER RESERVA                 |"
                                                    print "+-----------------------------------------------+\n"
                                                    professor_reserva = cpf
                                                    show.print_disciplinas_professor(professor_reserva)
                                                    
                                                    disciplina_reserva = raw_input("\n\nDigite o ID da disciplina da reserva: ")
                                        
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                 FAZER RESERVA                 |"
                                                    print "+-----------------------------------------------+"
                                                    
                                                    agora = today.hour
                                                    
                                                    print "\nDigite a hora da reserva (funcionamento das 7 as 22 horas)\n"
                                                    hora1 = raw_input("Inicio: ")
                                                    hora2 = raw_input("Fim: ")
                                                    hora1,hora2 = int(hora1),int(hora2)
                                                    print "-------------------------------------------------"
                                                    hour_future = False
                                                    if hora1 < hora2 and hora1 >=7 and hora2 < 22:
                                                        if day == today.day and month == today.month and hora1 > agora:
                                                            hour_future = True
                                                        elif day > today.day or today.month < month:
                                                            hour_future = True
                                                        else:
                                                            hour_future = False
                                                        
                                                    if hour_future == True:
                                                        count_erros = 0
                                                        nova_reserva = 0
                                                        
                                                        for horario in range (hora1,hora2,1):
                                                            hora = str(horario)
                                                            id_reserva = data+"_"+hora+"_"+predio_reserva+"_"+local_reserva
                                                            
                                                            verificar_reserva = "select id_reserva from reservas where id_reserva='%s'" %(id_reserva)
                                                            existe = cursor.execute(verificar_reserva)
                                                            if existe < 1:
                                                                print "[LIVRE]      %s horas" %(hora)
                                                                continue
                                                            else:
                                                                print "[RESERVADO]  %s horas"%(hora)
                                                                count_erros = count_erros + 1
                                                        print "-------------------------------------------------"
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
                                                                os.system("cls")
                                                                print "+-----------------------------------------------+"
                                                                print "|                 FAZER RESERVA                 |"
                                                                print "+-----------------------------------------------+"
                                                                ERRO_AULA = raw_input("\n\t[ERRO 001] Opcao invalida. Tente novamente.\n\tPressione ENTER para continuar.\n")
                                                        else:
                                                            if nova_reserva == 1:
                                                                continue
                                                            elif nova_reserva == 0:
                                                                okkkk = 0
                                                                for horario in range (hora1,hora2,1):
                                                                    hora = str(horario)
                                                                    id_reserva = data+"_"+hora+"_"+predio_reserva+"_"+local_reserva
                                                                    sql = "insert into reservas values('%s','%s','%s', '%s', '%s', '%s', '%d')"%(id_reserva, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, horario)
                                                                    try:
                                                                        cursor.execute(sql)
                                                                        db.commit()
                                                                        print "Cadastro efetuado com sucesso as %s horas" %(hora)
                                                                        okkkk+=1
                                                                    except:
                                                                        ERRO_AULA = raw_input("\n\t[ERRO 005] Reserva ja existente para %s horas.\n\tPressione ENTER para continuar.\n") %(hora)
                                                                        db.rollback()
                                                                        
                                                                if okkkk >= 1:
                                                                    CURSOAULA = ""
                                                                    DISCIPLINAAULA = ""
                                                                    
                                                                    cursor.execute("select * from disciplinas where id_disciplina='%s'" %(disciplina_reserva))
    
                                                                    for row in cursor.fetchall():
                                                                        CURSOAULA = row[2]
                                                                        DISCIPLINAAULA = row[1]
                                                                        
    
                                                                    logtexto = "%s - Prof. %s reservou aula de %s (%s)" %(DATARESERVA,nome_usuario,DISCIPLINAAULA,CURSOAULA)
                                                                    
                                                                    sql = "insert into log values('%s','%s','%s')"%(0, logtexto, CURSOAULA)
                                                                    cursor.execute(sql)
                                                                    db.commit()
                                                            else:
                                                                saida="s"
                                                    else:
                                                        os.system("cls")
                                                        print "+-----------------------------------------------+"
                                                        print "|                 FAZER RESERVA                 |"
                                                        print "+-----------------------------------------------+"
                                                        ERRO_AULA = raw_input("\n\t[ERRO 008] Impossivel fazer reservas neste horario.\n\tPressione ENTER para continuar.\n")
                                                        continue
                                                    saida = raw_input('\nDigite (S) para sair ou ENTER pra continuar: ')
                                                    saida = saida.lower()
                                                    os.system("cls")
                                                else:
                                                    saida = "s"
                                                    os.system("cls")
                                               
                                                    print "+-----------------------------------------------+"
                                                    print "|                 FAZER RESERVA                 |"
                                                    print "+-----------------------------------------------+"
                                                    ERRO_AULA = raw_input("\n\t[ERRO 008] Impossivel fazer reservas nessa data.\n\tPressione ENTER para continuar.\n")
                                                    
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                                    if choicep == 2:
                                        os.system("cls")
                                
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
                                            os.system("cls")
                                            print "+-----------------------------------------------+"
                                            print "|                DELETAR RESERVA                |"
                                            print "+-----------------------------------------------+"
                                            print "\nITEM    DATA     HORA  PREDIO LOCAL  DISCIPLINA"
                                            print "-------------------------------------------------"  
                                            for i in range (len(lista_reserva_ID)):
                                                DATA = lista_data[i]
                                                DATA = str(DATA)
                                                ano,mes,dia = DATA.split("-")
                                                NovaData = dia+"/"+mes+"/"+ano
                                                print "(%.2d) %s  %.2dh  %s  %s  %s - %s  " %(i+1,NovaData,lista_hora[i],lista_predioNOME[i],lista_localNOME[i],lista_disciplinaNOME[i],lista_cursoNOME[i])
                                            
                                            danosse = input("\nDigite o item a ser excluido ou 0 para sair: ")
                                            
                                            if danosse == 0:
                                                saida = "s"
                                            if danosse <> 0 and lista_reserva_ID <> []:
                                                del_reserva = lista_reserva_ID[danosse-1]
                                                sql = "delete from reservas where id_reserva='%s'" %(del_reserva)
                                                try:
                                                    cursor.execute(sql)
                                                    db.commit()
                                                    print "Reserva excluida com sucesso."
                                                    
                                                    up_nome_disciplina = lista_disciplinaNOME[danosse-1]
                                                    up_curso = lista_cursoNOME[danosse-1]
                                                    
                                                    DATA = lista_data[danosse-1]
                                                    DATA = str(DATA)
                                                    ano,mes,dia = DATA.split("-")
                                                    DELData = dia+"/"+mes+"/"+ano
                                                    

                                                    log_texto = "%s - Prof. %s cancelou a aula de %s (%s)" %(DELData,nome_usuario,up_nome_disciplina,up_curso)
                                                    
                                                    sql = "insert into log values('%s','%s','%s')"%(0, log_texto, up_curso)
                                                    cursor.execute(sql)
                                                    db.commit()
                                                    
                                                except:
                                                    os.system("cls")
                                                    print "+-----------------------------------------------+"
                                                    print "|                DELETAR RESERVA                |"
                                                    print "+-----------------------------------------------+"
                                                    ERRO_AULA = raw_input("\n\t[ERRO 004] Erro na exclusao. Nao existe reserva nesse horario.\n\tPressione ENTER para continuar.\n")
                                                    db.rollback()
                                                                                                
                                                saida = raw_input('\nDigite (S) para sair ou ENTER para continuar excluindo: ')
                                                saida = saida.lower()
                                                os.system("cls")
                                        
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
    
                                    if choicep == 3:
                                        os.system("cls")
                                    
                                        print "+-----------------------------------------------+"
                                        print "|                 ALTERAR SENHA                 |"
                                        print "+-----------------------------------------------+"
                                        print "\nOBS: \n1 - A senha deve ter mais que 3 e menos que 17 caracteres.\n2 - A senha deve conter apenas letras e numeros."
                                        teste = Validacao()
                                        senha1 = teste.SENHA_Check(getpass.getpass(prompt="Digite a nova senha: "))
                                        senha2 = teste.SENHA_Check(getpass.getpass(prompt="CONFIRME: "))
                                        if senha1 == senha2:
                                            
                                            sql = "update usuarios set senha='%s' where usuario_cpf='%s'" %(senha1, cpf)
                                            try:
                                                cursor.execute(sql)
                                                db.commit()
                                                Okayyy = raw_input("\nSenha editada com sucesso. Pressione ENTER ")
                                            except:
                                                os.sytem("cls")
                                                print "+-----------------------------------------------+"
                                                print "|                 ALTERAR SENHA                 |"
                                                print "+-----------------------------------------------+"
                                                ERRO_AULA = raw_input("\n\t[ERRO 007] Erro na edicao. Verifique se os campos foram inseridos corretamente.\n\tPressione ENTER para continuar.\n")
                                                db.rollback()
                                        else:
                                            os.system("cls")
                                    
                                            print "+-----------------------------------------------+"
                                            print "|                 ALTERAR SENHA                 |"
                                            print "+-----------------------------------------------+"
                                            ERRO_AULA = raw_input("\n\t[ERRO 003] Senha incorreta.\n\tPressione ENTER para continuar.\n")         
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                            
                                    if choicep == 4:
                                        os.system("cls")
                                        inicio_prof = 1
                                        print "+-----------------------------------------------+"
                                        print "|                    LOG OFF                    |"
                                        print "+-----------------------------------------------+"
                                        end = 1
                                os.system("cls")
                
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
                    
        if choice == 3:
            os.system("cls")
            print "+-----------------------------------------------+"
            print "|                    UPDATES                    |"
            print "+-----------------------------------------------+\n"
            show.print_departamentos()
            DEPARTAMENTO = raw_input("\nDigite o ID do departamento ou 0 para sair: ")
            if DEPARTAMENTO == "0":
                saida = "s"
                os.system("cls")
                continue
                
            else:
                os.system("cls")
                print "+-----------------------------------------------+"
                print "|                    UPDATES                    |"
                print "+-----------------------------------------------+\n"
                show.print_departamentos_cursos(DEPARTAMENTO)
                CURSO = raw_input("\nDigite o ID do curso ou 0 para sair: ")
                if CURSO == "0":
                    saida = "s"
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print "+-----------------------------------------------+"
                    print "|                    UPDATES                    |"
                    print "+-----------------------------------------------+\n"
                    show.print_log(CURSO)
            
            saida = raw_input('\nDigite (S) para sair ou ENTER para continuar excluindo: ')
            saida = saida.lower()
            os.system("cls")
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#
            
        if choice == 4:
            os.system("cls")
            inicio = 1
            print "+-----------------------------------------------+"
            print "|              PROGRAMA FINALIZADO              |"
            print "+-----------------------------------------------+"
            okkay = raw_input("\n\t\tPressione ENTER")
            db.close()
                    
                    
                    
            
