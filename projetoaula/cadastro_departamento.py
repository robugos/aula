# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
#===============================================================================


class departamento():
    def __init__(self):
        self.dp_NOME = ""
        self.dp_COORDENADOR = ""
        self.dp_CODIGO = ""
        
    def set_Nome(self,nome):
        self.dp_NOME = nome

    def set_Coordenador(self,coord):
        self.dp_COORDENADOR = coord
    
    def set_Codigo(self,codigo):
        self.dp_CODIGO = codigo
    
    def BUTTONCOMMIT(self):
        cursor=db.cursor()
        sql="insert into DEPARTAMENTOS values( '%s','%s','%s' ) " %(DP.dp_CODIGO,DP.dp_NOME,DP.dp_COORDENADOR)
        cursor.execute(sql)

print "----------------Cadastro de Departamento----------------"
DP = departamento()
DP.set_Nome(raw_input("Nome do departamento: "))
DP.set_Coordenador(raw_input("Nome do Coordenador: "))
DP.set_Codigo(raw_input("Código: "))
DP.BUTTONCOMMIT()
print "------------------------ADDED---------------------------"


