# -*- coding: cp1252 -*-
#----------------------------------GustavoPereira
from VerificarCPF import Verificar

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
        
#-------------TESTES----------------------
print "          << LOGIN >>"
CPF=raw_input("CPF: ")
Test = Verificar(CPF)
password = raw_input("Senha: ")
            
Login = Login_professor()
Login.prof_CPF(Test.userCPF)
Login.userSenha(password)

Login.imprimir_dados()
        
#----------------------------------GustavoPereira