# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
#===============================================================================
from Validacao import Validacao
#===============================================================================

class cadastro:
    def __init__(self, nome, departamento,CPF):
        self.disciplinas=[]
        self.nome = nome
        self.departamento = departamento
        self.CPF = CPF
        
    def cadastrar_disciplinas(self,disciplinas): 
        self.disciplinas.append(disciplinas)

    def BUTTONCOMMIT(self):
        cursor=db.cursor()
        sql="insert into PROFESSOR values( '%s','%s','%s' ) " %(professor.CPF,professor.nome,professor.departamento)
        cursor.execute(sql)
        
#===================================INTERAÇÃO===================================
print "            Cadastro Professor"
nome=raw_input("Nome: ")
departamento=raw_input("Departamento: ")

#=====================================CPF=======================================
CPF = raw_input("CPF: ")
Test = Validacao()
CPF = Test.CPF_Check(CPF)
#===============================================================================

professor = cadastro(nome,departamento,CPF)

#===============================================================================
print "\nDisciplinas ministradas e para finalizar PRESS ENTER >>\n"
disciplinas=None
while disciplinas!='':
    disciplinas = raw_input("Disciplinas ministradas pelo professor:")
    if disciplinas!='':
        professor.cadastrar_disciplinas(disciplinas)
    else:
        print "\nProfessor cadastrado com sucesso"
#===============================================================================
professor.BUTTONCOMMIT()
#===============================================================================