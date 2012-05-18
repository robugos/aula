# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def cadastrarCurso(cursor, id_curso, nome_curso, departamento_curso):
    sql = "insert into cursos values('%s','%s','%s')"%(id_curso, nome_curso, departamento_curso)
    try:
        cursor.execute(sql)
        db.commit()
        print "Curso cadastrado com sucesso."
    except:
        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================
        
print "------ CADASTRO DE CURSOS ------"
saida = None
while saida <> "s":
    id_curso = raw_input("Digite o ID do curso: ")
    verificar_curso = "select id_curso from cursos where id_curso='%s'" %(id_curso)
    existe = cursor.execute(verificar_curso)
    if existe > 0:
        print "Curso já existe."
        continue
    else:
        nome_curso = raw_input("Digite o nome do curso: ")
        departamento_curso = raw_input("Digite o departamento do curso: ")
        cadastrarCurso(cursor, id_curso, nome_curso, departamento_curso)
        saida = raw_input('Digite s para sair ou enter pra continuar: ')
    
print "------ CADASTRO EFETUADO COM SUCESSO ------"
db.close()