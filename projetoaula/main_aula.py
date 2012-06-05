# -*- coding: cp1252 -*-
#inicio do programa


import os
from login import *
from exclusao_reserva import *




inicio=0
while inicio == 0:
    os.system("cls")
    print "\n                         AULA.\n"
    choice=input("[1] Pesquisa  [2] Login  [3] Sair\nDigite: ")
    if choice > 3 or choice <1:
        print "[ERRO 000] Opção inválida. Tente novamente\n"
    else:
#=========================================================
        if choice == 1:
            os.system("cls")
            print "=====================PESQUISA======================"

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
                        senha = raw_input("Digite a senha: ")
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
    
                            #MAIN_ADM
                            
                            
                            
                            
                            #MAIN_ADM

                        else:
                            os.system("cls")
                            print "Bem vindo, PROFESSOR"
                            
                            #MAIN_PROF
                            inicio_prof=0
                            while inicio_prof == 0:
                                choice=input("Digite:\n1 - Fazer Reserva\n2 - Deletar Reserva\n3 - Alterar senha\n4 - Sair\n->")
                                if choice > 4 or choice <1:
                                    print "[ERRO 001] Opção inválida. Tente novamente\n"
                                else:
                            
                            #=========================================================
                                    if choice == 1:
                                        os.system("cls")
                                        print "\n                   FAZER RESERVA.\n"
                                        
                                        from cadastro_reserva import *
                                     
                                        saida = None
                                        while saida <> "s":
                                            Test = Validacao()
                                            
                                            print_predios()
                                            predio_reserva = raw_input("\n\nDigite o ID do prédio da reserva ")
                                            os.system("cls")
                                            
                                            print_local(predio_reserva)
                                            local_reserva = raw_input("\n\nDigite o ID do local da reserva: ")
                                            os.system("cls")
                                            
                                            data = raw_input("Digite a data da reserva (0000-00-00) ")
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
                                            os.system("cls")
                                            print "CADASTRO EFETUADO COM SUCESSO"
                                            saida = raw_input('Digite s para sair ou ENTER pra continuar: ')
                                            os.system("cls")
                                        db.close()
                                        
                            #=========================================================
                            
                                    if choice == 2:
                                        os.system("cls")
                                        print "=================DELETAR RESERVA==================="
                                        
                                        
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
                                        print "====================ALTERAR SENHA=================="
                            
                            
                            #=========================================================
                            
                                    if choice == 4:
                                        os.system("cls")
                                        inicio_prof = 1
                                        print "=====================LOG OFF======================="
                                        
                                os.system("cls")

                            
                            #MAIN_PROF
                    end=1

#=========================================================
        
        if choice == 3:
            os.system("cls")
            inicio = 1
            print "=================PROGRAMA FINALIZADO==============="

#=========================================================
            

        