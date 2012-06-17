import MySQLdb
db = MySQLdb.connect("aula.myftp.org","yoshi","mario1234","auladb")
cursor = db.cursor()
import os

class prints():
    def print_reservas_prof(self,cpf_prof): 
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
    
    def print_disciplinas(self,CURSO):
        cursor.execute("select * from disciplinas where curso_disciplina='%s'" %(CURSO))
        lista_disciplinas_ID=[]
        lista_disciplinas_Nome=[]
        for row in cursor.fetchall():
                lista_disciplinas_ID.append(row[0])
                lista_disciplinas_Nome.append(row[1])
        print "  ID      NOME"
        for i in range (len(lista_disciplinas_ID)):
            print "["+lista_disciplinas_ID[i]+"] - "+lista_disciplinas_Nome[i]
            
    def print_disciplinas_professor(self,cpf):
        cursor.execute("select * from docencia where id_professor='%s'" %(cpf))
        lista_disciplinas_ID=[]
        lista_disciplinas_Nome=[]
        lista_disciplinas_curso=[]
        for row in cursor.fetchall():
                lista_disciplinas_ID.append(row[2])
        for j in range (len(lista_disciplinas_ID)): #pega nome da disciplina
            cursor.execute("select * from disciplinas where id_disciplina='%s'" %(lista_disciplinas_ID[j]))        
            for row in cursor.fetchall():
                lista_disciplinas_Nome.append(row[1])
                lista_disciplinas_curso.append(row[2])   
        print "  ID     CURSO   DISCIPLINA\n"
        for i in range (len(lista_disciplinas_ID)):
            print "["+lista_disciplinas_ID[i]+"]   "+lista_disciplinas_curso[i]+"     "+lista_disciplinas_Nome[i]
        
    def print_predios(self):
        cursor.execute("select * from predios")
        lista_predios_ID=[]
        lista_predios_Nome=[]
        for row in cursor.fetchall():
            lista_predios_ID.append(row[0])
            lista_predios_Nome.append(row[1])
        print "  ID      NOME"
        for i in range (len(lista_predios_ID)):
            print "["+lista_predios_ID[i]+"] - "+lista_predios_Nome[i]
            
    def print_cursos(self):                                                
        cursor.execute("select * from cursos")
        lista_cursos_ID=[]
        lista_cursos_Nome=[]
        for row in cursor.fetchall():
            lista_cursos_ID.append(row[0])
            lista_cursos_Nome.append(row[1])
        print "  ID      NOME"
        for i in range (len(lista_cursos_ID)):
            print "["+lista_cursos_ID[i]+"] - "+lista_cursos_Nome[i]
        
    def print_departamentos(self):                        
        cursor.execute("select * from departamentos")
        lista_departamentos_ID=[]
        lista_departamentos_Nome=[]
        for row in cursor.fetchall():
            lista_departamentos_ID.append(row[0])
            lista_departamentos_Nome.append(row[1])
        print "  ID      NOME"
        for i in range (len(lista_departamentos_ID)):
            print "["+lista_departamentos_ID[i]+"] - "+lista_departamentos_Nome[i]
                    
    def print_professores(self):
        cursor.execute("select * from departamentos")
        lista_departamentos_ID=[]
        lista_departamentos_Nome=[]
        for row in cursor.fetchall():
            lista_departamentos_ID.append(row[0])
            lista_departamentos_Nome.append(row[1])
        print "  ID      NOME"
        for i in range (len(lista_departamentos_ID)):
            print "["+lista_departamentos_ID[i]+"] - "+lista_departamentos_Nome[i]
        departamento = raw_input('\nDigite o ID do departamento do professor: ')
        cursor.execute("select * from professores where departamento_professor='%s'" %(departamento))
        os.system('cls')
        lista_professores_ID=[]
        lista_professores_Nome=[]
        for row in cursor.fetchall():
            lista_professores_ID.append(row[0])
            lista_professores_Nome.append(row[1])
        print "    CPF          NOME"
        for i in range (len(lista_professores_ID)):
            print "["+lista_professores_ID[i]+"] - "+lista_professores_Nome[i]
            
    def print_professores_alone(self):                                      
        cursor.execute("select * from professores")
        lista_professores_ID=[]
        lista_professores_Nome=[]
        for row in cursor.fetchall():
            lista_professores_ID.append(row[0])
            lista_professores_Nome.append(row[1])
        print "    CPF          NOME"
        for i in range (len(lista_professores_ID)):
            print "["+lista_professores_ID[i]+"] - "+lista_professores_Nome[i]
            
    def print_local(self,predio_reserva):
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