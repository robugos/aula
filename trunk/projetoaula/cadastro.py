# -*- coding: cp1252 -*-
#=======================================================Gustavo Pereira
class cadastro:
    def __init__(self, nome, departamento,cpf):
        self.dados=[]
        self.dados.append(nome+"\n")
        self.dados.append(departamento+"\n")
        self.dados.append(cpf+"\n")
        
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
cpf=raw_input("CPF (somente números): ")
ver=False
#===========Thiago, Robson e Rafaella========================#
def verificar(cpf):
    while ver == False:
        if len(cpf)==11:
            try:
                for i in cpf:
                    i=int(i)
                break
            except:
                print "CPF digitado incorretamente!"
                cpf=raw_input("CPF (somente números): ")
                verificar(cpf)
        else:
            print "CPF digitado incorretamente!"
            cpf=raw_input("CPF (somente números): ")
            verificar(cpf)
                
verificar(cpf)
#===========Thiago, Robson e Rafaella========================#
            
professor=cadastro(nome,departamento,cpf)

print "Entre com as disciplinas ministradas e para finalizar PRESS ENTER"
disciplina=None
while disciplina!='':
    disciplina = raw_input("Disciplinas ministradas pelo professor:")
    if disciplina!='':
        professor.cadastrar_disciplinas(disciplina)
    else:
        print "\nProfessor cadastrado com sucesso"
professor.gravar()
#=======================================================Gustavo Pereira