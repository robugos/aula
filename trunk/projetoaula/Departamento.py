# -*- coding: cp1252 -*-
#Made by Gustavo and Rafaella 

class departamento():
    def __init__(self):
        self.dp_NOME = ""
        self.dp_COORDENADOR = ""
        
    def set_Nome(self,nome):
        self.dp_NOME = nome

    def set_Coordenador(self,coord):
        self.dp_COORDENADOR = coord

    def Send_to_DB(self):
        #Digitar aqui as informações para enviar tudo pro banco de dados...
        #Colocar todos os selfs. 

    
DP = departamento()
DP.set_Nome(raw_input("Nome do departamento: "))
DP.set_Coordenador(raw_input("Nome do Coordenador: "))

DP.Send_to_DB()
