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
#===============================================================================

import os
import getpass
from login import *
from edicao_usuario import *


#FUNCAO PRINT NA TELA

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

#FUNCAO PRINT NA TELA

inicio=0
while inicio == 0:
    print "\n                         AULA.\n"
    choice=input("[1] Pesquisa  [2] Login  [3] Sair\nDigite: ")
    if choice > 3 or choice <1:
        os.system("cls")
        print "[ERRO 000] Opção inválida. Tente novamente\n"
    else:
#=========================================================
        if choice == 1:
            os.system("cls")
            print "\n                     PESQUISA.\n"

#=========================================================
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
                    print "Usuario não existente."
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
                            print "Bem vindo, ADMINISTRADOR"
    
                            #MAIN_ADM                                                            FAZER AMANHA
                            print "\n                     PAINEL DO ADMINISTRADOR.\n"
                            
                            #MAIN_ADM

                        else:
                            os.system("cls")
                            print "Bem vindo, PROFESSOR"
                            
                            #MAIN_PROF
                            inicio_prof=0
                            while inicio_prof == 0:
                                print "\n                     PAINEL DO PROFESSOR.\n"
                                choice=input("Digite:\n1 - Fazer Reserva\n2 - Deletar Reserva\n3 - Alterar senha\n4 - Sair\n->")
                                if choice > 4 or choice <1:
                                    print "[ERRO 001] Opção inválida. Tente novamente\n"
                                else:
                            
                            #=========================================================
                                    if choice == 1:
                                        os.system("cls")
                                        print "\n                   FAZER RESERVA.\n"
                                        
                                        saida = None
                                        while saida <> "s":
                                            Test = Validacao()
                                            
                                            print_predios()
                                            predio_reserva = raw_input("\n\nDigite o ID do prédio da reserva ")
                                            os.system("cls")
                                            
                                            print_local(predio_reserva)
                                            local_reserva = raw_input("\n\nDigite o ID do local da reserva: ")
                                            os.system("cls")
                                            
                                            data = raw_input("Digite a data da reserva ano-mes-dia (0000-00-00) ")
                                            os.system("cls")
                                            
                                            professor_reserva = cpf
                                            
                                            #print_disciplinas(professor_reserva)
                                            #Fazer disciplinas apenas do professor
                                            disciplina_reserva = raw_input("\n\nDigite o ID da disciplina da reserva: ")
                                
                                            os.system("cls")
                                            print "Digite a hora da reserva (funcionamento das 7 as 22 horas)\n"
                                            hora1 = input("Inicio: ")
                                            hora2 = input("Fim: ")
                                            
                                            #Fazer verificacao de horario negativo ou fora do funcionamento
                                            
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
                                                #cadastrarReserva(cursor, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, hora1, hora2)
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
                                                            print "[ERRO 002] Reserva já existente para %s horas." %(hora)
                                                            db.rollback()
                                                    #cadastrarReserva
                                                else:
                                                    saida="s"
                                            saida = raw_input('\nDigite s para sair ou ENTER pra continuar: ')
                                            saida = saida.lower()
                                            os.system("cls")
                                        
                                        
                            #=========================================================
                            
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
                                                    print "Erro na exclusão, não existe reserva nesse horário."
                                                    db.rollback()
                                                                                                
                                            saida = raw_input('\nDigite s para sair ou ENTER para continuar excluindo: ')
                                            saida = saida.lower()
                                            os.system("cls")
                                                
                                        print "    FINISH"
                                        
                                
                            #=========================================================
                            
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
                                        
                            
                            #=========================================================
                            
                                    if choice == 4:
                                        os.system("cls")
                                        inicio_prof = 1
                                        print "\n                      LOG OFF.\n"
                                        
                                os.system("cls")

                            
                            #MAIN_PROF
                    end=1

#=========================================================
        
        if choice == 3:
            os.system("cls")
            inicio = 1
            print "\n             PROGRAMA FINALIZADO.\n"
            db.close()

#=========================================================
            

        