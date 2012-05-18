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


def cadastrarProfessor(cursor, id_professor, nome_professor, disciplinas, departamento_professor):
    sql = "insert into professores values('%s','%s','%s', '%s')"%(id_professor, nome_professor, disciplinas, departamento_professor)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
        
def cadastrarUsuario(cursor, usuario_CPF):
    classe = 0 #Classe 0 para professores
    senha = "UFRPE1234" 
    sql = "insert into usuarios values('%s','%s','%s')"%(usuario_CPF, senha, classe)
    cursor.execute(sql)
    db.commit()

#===============================================================================
        
print "------ CADASTRO DE PROFESSORES ------"
saida = None
while saida <> "s":
    Test = Validacao()
    id_professor = Test.CPF_Check(raw_input("Digite o CPF do professor: "))
    nome_professor = raw_input("Digite o nome do professor: ")
    departamento_professor = raw_input("Digite o departamento do professor: ")
    cadastrarProfessor(cursor, id_professor, nome_professor, "", departamento_professor)
    cadastrarUsuario(cursor,id_professor) #Add um novo usuário no DB
    saida = raw_input('Digite s para sair ou enter pra continuar: ')
    
print "------ CADASTRO EFETUADO COM SUCESSO ------"
db.close()