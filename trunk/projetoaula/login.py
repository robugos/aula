# -*- coding: cp1252 -*-
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

class Login_professor():
    def __init__(self):
        self.profCPF = None
        self.password = None
        
    def prof_CPF(self,CPF):
        self.profCPF = CPF
        
    def userSenha(self, password): #Precisa fazer o check com o Banco de dados, ainda
        self.password = password
        
    def acessar_paginas(self):
        print self.password, self.profCPF
        
#=======================================TESTES==================================

print "          << LOGIN >>"

Login = Login_professor()

cpf = raw_input("Digite o login (CPF): ")
verificar_CPF = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(cpf)
existe = cursor.execute(verificar_CPF)
if existe < 1:
    print "Usuario não existente."
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
        Login.acessar_paginas()
