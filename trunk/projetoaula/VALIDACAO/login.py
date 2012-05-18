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

class Login_professor():
    def __init__(self):
        self.profCPF = None
        self.password = None
        
    def prof_CPF(self,CPF):
        self.profCPF = CPF
        
    def userSenha(self, password): #Precisa fazer o check com o Banco de dados, ainda
        self.password = password
        
    def imprimir_dados(self):
        print self.password, self.profCPF
        
#=======================================TESTES==================================

print "          << LOGIN >>"
CPF = raw_input("CPF: ")
Test = Validacao()
CPF = Test.CPF_Check(CPF)

Login = Login_professor()
Login.prof_CPF(CPF)

password = raw_input("Senha: ")
Login.userSenha(password)

Login.imprimir_dados()
