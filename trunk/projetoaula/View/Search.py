import MySQLdb
db = MySQLdb.connect("aula.myftp.org","yoshi","mario1234","auladb")
cursor = db.cursor()
from Prints import *
show = prints()
import os

class Search():
    def openPESQUISA(self):
        exits = False
        while exits == False:
            show.print_departamentos()
            DEPARTAMENTO = raw_input("\nDigite o ID do departamento ou 0 para sair: ") 
            if DEPARTAMENTO == "0":
                exits = True
            else:
                os.system("cls")
                print "+-----------------------------------------------+"
                print "|                  PESQUISA                     |"
                print "+-----------------------------------------------+"
                show.print_departamentos_cursos(DEPARTAMENTO)
                CURSO = raw_input("\nDigite o ID do curso ou 0 para sair: ")
                if CURSO == "0":
                    exits = True
                else:
                    PERIODO = input("\nDigite o periodo do curso ou 0 para sair: ")
                    if PERIODO == 0:
                        exits = True
                    else:
                        os.system("cls")
                        print "+-----------------------------------------------+"
                        print "|                  PESQUISA                     |"
                        print "+-----------------------------------------------+"
                        show.print_disciplinas_filtro(PERIODO)
                        DISCIPLINA = raw_input("\nDigite o ID da disciplina ou 0 para sair: ")
                        if DISCIPLINA == "0":
                            exits = True
                        else:
                            #Funcao filtro das reservas
                            cursor.execute("select * from disciplinas where id_disciplina='%s'" %(DISCIPLINA))
                            NOME_disc = ""
                            for row in cursor.fetchall():
                                NOME_disc = row[1]

                            cursor.execute("select * from reservas where disciplina_reserva='%s'" %(DISCIPLINA))
                            predio_ID=[]
                            local_ID=[]
                            professor_ID=[]
                            data = []
                            hora = []
                            for row in cursor.fetchall():
                                predio_ID.append(row[1])
                                local_ID.append(row[2])
                                professor_ID.append(row[5])
                                data.append(row[3])
                                hora.append(row[6])
                            
                            predio_NOME=[]
                            local_NOME=[]
                            professor_NOME=[]
                            
                            for i in range(len(predio_ID)):
                                cursor.execute("select * from predios where id_predio='%s'" %(predio_ID[i]))
                                for row in cursor.fetchall():
                                    predio_NOME.append(row[1])
                                    
                            for i in range(len(local_ID)):
                                cursor.execute("select * from locais where id_local='%s'" %(local_ID[i]))
                                for row in cursor.fetchall():
                                    local_NOME.append(row[1])
                            
                            for i in range(len(local_ID)):
                                cursor.execute("select * from professores where id_professor='%s'" %(professor_ID[i]))
                                for row in cursor.fetchall():
                                    professor_NOME.append(row[1])
                                    
                            if professor_NOME==[]:
                                print "+-----------------------------------------------+"
                                print "|                  PESQUISA                     |"
                                print "+-----------------------------------------------+"
                                print "\nNao ha reservas para %s" %(NOME_disc)
                            else:
                                os.system("cls")
                                print "+-----------------------------------------------+"
                                print "|                  PESQUISA                     |"
                                print "+-----------------------------------------------+"
                                print  "\nAula de %s\nProfessor(a) %s\n" %(NOME_disc,professor_NOME[0])
                                print "-------------------------------------------------"
                                for i in range (len(professor_ID)):
                                    DATA = data[i]
                                    DATA = str(DATA)
                                    ano,mes,dia = DATA.split("-")
                                    print "%s/%s/%s  as  %.2dh  LOCAL: %s no %s" %(dia,mes,ano,hora[i],local_NOME[i],predio_NOME[i])
                                print "-------------------------------------------------"
                                
                                SAIDA_FINAL = raw_input("\nOK: ")
        
            os.system("cls")
            exits = True
      