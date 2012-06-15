# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def cadastrarDisciplina(cursor, id_disciplina, nome_disciplina, curso_disciplina):
    sql = "insert into disciplinas values('%s','%s','%s')"%(id_disciplina, nome_disciplina, curso_disciplina)
    try:
        cursor.execute(sql)
        db.commit()
        print "Disciplina cadastrada com sucesso."
    except:
        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================
        
print "------ CADASTRO DE DISCIPLINAS ------"
saida = None
while saida <> "s":
    id_disciplina = raw_input("Digite o ID da disciplina: ")
    verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(id_disciplina)
    existe = cursor.execute(verificar_dis)
    if existe > 0:
        print "Disciplina já existente."
        continue
    else:
        nome_disciplina = raw_input("Digite o nome da disciplina: ")
        curso_disciplina = raw_input("Digite o curso da disciplina: ")
        cadastrarDisciplina(cursor, id_disciplina, nome_disciplina, curso_disciplina)
        saida = raw_input('Digite s para sair ou enter pra continuar: ')
    
print "------ CADASTRO EFETUADO COM SUCESSO ------"
db.close()