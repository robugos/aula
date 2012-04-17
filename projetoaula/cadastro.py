#=======================================================Gustavo Pereira
class cadastro:
    def __init__(self, nome, departamento,):
        self.dados=[]
        self.dados.append(nome+"\n")
        self.dados.append(departamento+"\n")

    def cadastrar_disciplinas(self,disciplina):
        self.dados.append(disciplina+" ")

    def gravar(self):
        SQL=open("Dados_Professores.txt","a")
        SQL.writelines(self.dados)
        SQL.close()
        print "\nDados Atualizados no Banco de dados"
        
#===============================GRAVAR SQL==============================
print "Professor, entre com seus dados.."
nome=raw_input("Nome: ")
departamento=raw_input("Departamento: ")
professor=cadastro(nome,departamento)

print "Entre com as disciplinas ministradas e para finalizar PRESS ENTER"
disciplina=None
while disciplina!='':
    disciplina = raw_input("Disciplinas ministradas:")
    if disciplina!='':
        professor.cadastrar_disciplinas(disciplina)
    else:
        print "\nProfessor cadastrado com sucesso"
professor.gravar()
#=======================================================Gustavo Pereira
