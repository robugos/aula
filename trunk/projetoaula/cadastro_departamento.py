# -*- coding: cp1252 -*-
import MySQLdb
from acesso_db import Servidor

class departamento():
    def __init__(self):
        self.dp_NOME = ""
        self.dp_COORDENADOR = ""
        self.dp_CODIGO = 0
        
    def set_Nome(self,nome):
        self.dp_NOME = nome

    def set_Coordenador(self,coord):
        self.dp_COORDENADOR = coord
    
    def set_Codigo(self):
        self.dp_CODIGO+=1
    
    def BOTAOCommit(self):
        cursor=db.cursor()
        sql="insert into DEPARTAMENTOS values( '%s','%s','%s' ) " %(self.dp_CODIGO,self.dp_NOME,self.dp_COORDENADOR)
        cursor.execute(sql)

print "----------------Cadastro de Departamento----------------"
DP = departamento()
DP.set_Nome(raw_input("Nome do departamento: "))
DP.set_Coordenador(raw_input("Nome do Coordenador: "))
DP.set_Codigo()
DP.BOTAOCommit()
print "--------------------------------------------------------"
