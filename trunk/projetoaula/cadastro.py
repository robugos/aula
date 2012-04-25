# -*- coding: cp1252 -*-
#=======================================================Gustavo Pereira

from VerificarCPF import Verificar

class cadastro:
    def __init__(self, nome, departamento,CPF):
        self.dados=[]
        self.dados.append(nome+"\n")
        self.dados.append(departamento+"\n")
        self.dados.append(CPF+"\n")
        
    def cadastrar_disciplinas(self,disciplina):
        self.dados.append(disciplina+" ")

    def gravar(self):
        SQL=open("Dados_Professores.txt","a")
        SQL.writelines(self.dados)
        SQL.write("\n\n")
        SQL.close()
        print "\nDados Atualizados no Banco de dados"
        
#===============================GRAVAR NO SQL==============================
print "Entre com os dados do professor."
nome=raw_input("Nome: ")
departamento=raw_input("Departamento: ")
CPF=raw_input("CPF: ")
Test = Verificar(CPF)
            
professor=cadastro(nome,departamento,Test.userCPF)

print "\nEntre com as disciplinas ministradas e para finalizar PRESS ENTER\n"
disciplina=None
while disciplina!='':
    disciplina = raw_input("Disciplinas ministradas pelo professor:")
    if disciplina!='':
        professor.cadastrar_disciplinas(disciplina)
    else:
        print "\nProfessor cadastrado com sucesso"
professor.gravar()
#=======================================================Gustavo Pereira