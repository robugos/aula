# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
#inicio do programa


import os
from login import *
from exclusao_reserva import *
from cadastro_reserva import *
from edicao_usuario import *
from Validacao import Validacao
import getpass


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
                                            cadastrarReserva(cursor, predio_reserva, local_reserva, data, disciplina_reserva, professor_reserva, hora1, hora2)
                
                        
                                            saida = raw_input('Digite s para sair ou ENTER pra continuar: ')
                                            os.system("cls")
                                        db.close()
                                        
                            #=========================================================
                            
                                    if choice == 2:
                                        os.system("cls")
                                        print "\n               DELETAR RESERVA.\n"
                                        
                                        
                                        #Printar somente as reservas do professor com detalhamento...
                                        saida = None
                                        while saida <> "s": 
                                            data = raw_input("Digite a data da reserva (0000-00-00) ")
                                            predio_reserva = raw_input("Digite o prédio da reserva ")
                                            local_reserva = raw_input("Digite o local da reserva: ")
                                            hora1 = input("Digite horário de inicio: ")
                                            hora2 = input("Digite horário de fim: ")
                                            
                                            for horario in range (hora1,hora2,1):
                                                hora = str(horario)
                                                id_reserva = hora+"_"+data+"_"+predio_reserva+"_"+local_reserva
                                            
                                                verificar_reserva = "select id_reserva from reservas where id_reserva='%s'" %(id_reserva)
                                                existe = cursor.execute(verificar_reserva)
                                            
                                                if existe < 1:
                                                    print "Reserva não existente no horário das %s horas" %(hora)
                                                    continue
                                                else:
                                                    excluirReserva(cursor, id_reserva)
                                            saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
                                                    
                                        print "------ FINISH ------"
                                        db.close()
                            
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

#=========================================================
            

        