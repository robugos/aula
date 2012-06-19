import MySQLdb
db = MySQLdb.connect("aula.myftp.org","yoshi","mario1234","auladb")
cursor = db.cursor()
import os

class prints():
    def print_log(self,CURSO):
        cursor.execute("select * from log where id_curso='%s'" %(CURSO))
        TEXT = []
        for row in cursor.fetchall():
            TEXT.append(row[1]) 
        for i in range(len(TEXT)):
            print TEXT[i]+"\n"
        print "-------------------------------------------------"    
    
    def print_disciplinas(self,CURSO):
        cursor.execute("select * from disciplinas where curso_disciplina='%s'" %(CURSO))
        lista_disciplinas_ID=[]
        lista_disciplinas_Nome=[]
        for row in cursor.fetchall():
                lista_disciplinas_ID.append(row[0])
                lista_disciplinas_Nome.append(row[1])
        print "  ID\tDISCIPLINA"
        print "-------------------------------------------------"
        for i in range (len(lista_disciplinas_ID)):
            print lista_disciplinas_ID[i]+"\t"+lista_disciplinas_Nome[i]
        print "-------------------------------------------------"
            
    def print_disciplinas_filtro(self,PERIODO):
        cursor.execute("select * from disciplinas where periodo='%s'" %(PERIODO))
        lista_disciplinas_ID=[]
        lista_disciplinas_Nome=[]
        for row in cursor.fetchall():
                lista_disciplinas_ID.append(row[0])
                lista_disciplinas_Nome.append(row[1])
        print "  ID\tDISCIPLINA"
        print "-------------------------------------------------"
        for i in range (len(lista_disciplinas_ID)):
            print lista_disciplinas_ID[i]+"\t"+lista_disciplinas_Nome[i]
        print "-------------------------------------------------"
            
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
        print "-------------------------------------------------"
        for i in range (len(lista_disciplinas_ID)):
            print lista_disciplinas_ID[i]+"    "+lista_disciplinas_curso[i]+"     "+lista_disciplinas_Nome[i]
        print "-------------------------------------------------"
        
    def print_predios(self):
        cursor.execute("select * from predios")
        lista_predios_ID=[]
        lista_predios_Nome=[]
        for row in cursor.fetchall():
            lista_predios_ID.append(row[0])
            lista_predios_Nome.append(row[1])
        print " ID\tPREDIO"
        print "-------------------------------------------------"
        for i in range (len(lista_predios_ID)):
            print lista_predios_ID[i]+"\t"+lista_predios_Nome[i]
        print "-------------------------------------------------"
            
    def print_cursos(self):                                                
        cursor.execute("select * from cursos")
        lista_cursos_ID=[]
        lista_cursos_Nome=[]
        for row in cursor.fetchall():
            lista_cursos_ID.append(row[0])
            lista_cursos_Nome.append(row[1])
        print "  ID\tCURSOS"
        print "-------------------------------------------------"
        for i in range (len(lista_cursos_ID)):
            print lista_cursos_ID[i]+"\t"+lista_cursos_Nome[i]
        print "-------------------------------------------------"
        
    def print_departamentos(self):                        
        cursor.execute("select * from departamentos")
        lista_departamentos_ID=[]
        lista_departamentos_Nome=[]
        for row in cursor.fetchall():
            lista_departamentos_ID.append(row[0])
            lista_departamentos_Nome.append(row[1])
        print "  ID\tDEPARTAMENTO"
        print "-------------------------------------------------"
        for i in range (len(lista_departamentos_ID)):
            print lista_departamentos_ID[i]+"\t"+lista_departamentos_Nome[i]
        print "-------------------------------------------------"
        
    def print_departamentos_cursos(self,DEPARTAMENTO):                        
        cursor.execute("select * from cursos where departamento_curso='%s'" %(DEPARTAMENTO))
        lista_cursos_ID=[]
        lista_cursos_Nome=[]
        for row in cursor.fetchall():
            lista_cursos_ID.append(row[0])
            lista_cursos_Nome.append(row[1])
        print "  ID\tCURSO"
        print "-------------------------------------------------"
        for i in range (len(lista_cursos_ID)):
            print lista_cursos_ID[i]+"\t"+lista_cursos_Nome[i]
        print "-------------------------------------------------"
                   
    def print_professores(self):
        cursor.execute("select * from departamentos")
        lista_departamentos_ID=[]
        lista_departamentos_Nome=[]
        for row in cursor.fetchall():
            lista_departamentos_ID.append(row[0])
            lista_departamentos_Nome.append(row[1])
        print "  ID               NOME"
        print "-------------------------------------------------"
        for i in range (len(lista_departamentos_ID)):
            print lista_departamentos_ID[i]+"\t\t"+lista_departamentos_Nome[i]
        print "-------------------------------------------------"
        departamento = raw_input('\nDigite o ID do departamento do professor: ')
        cursor.execute("select * from professores where departamento_professor='%s'" %(departamento))
        os.system('cls')
        lista_professores_ID=[]
        lista_professores_Nome=[]
        for row in cursor.fetchall():
            lista_professores_ID.append(row[0])
            lista_professores_Nome.append(row[1])
        print "    CPF          NOME"
        print "-------------------------------------------------"
        for i in range (len(lista_professores_ID)):
            print lista_professores_ID[i]+"\t"+lista_professores_Nome[i]
        print "-------------------------------------------------"
            
    def print_professores_alone(self):                                      
        cursor.execute("select * from professores")
        lista_professores_ID=[]
        lista_professores_Nome=[]
        for row in cursor.fetchall():
            lista_professores_ID.append(row[0])
            lista_professores_Nome.append(row[1])
        print "        CPF\tNOME"
        print "-------------------------------------------------"
        for i in range (len(lista_professores_ID)):
            print lista_professores_ID[i]+"\t"+lista_professores_Nome[i]
        print "-------------------------------------------------"
        
    def print_local(self,predio_reserva):
        cursor.execute("select * from locais where predio_local='%s'" %(predio_reserva))
        lista_locais_ID=[]
        lista_locais_Nome=[]
        lista_locais_Tipo=[]
        for row in cursor.fetchall():
            lista_locais_ID.append(row[0])
            lista_locais_Nome.append(row[1])
            lista_locais_Tipo.append(row[2])
        print " ID\tNOME\tTIPO"
        print "-------------------------------------------------"
        for i in range (len(lista_locais_ID)):
            print lista_locais_ID[i]+"\t"+lista_locais_Nome[i]+"\t"+lista_locais_Tipo[i]
        print "-------------------------------------------------"