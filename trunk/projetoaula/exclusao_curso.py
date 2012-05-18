# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================


def excluirCurso(cursor, deletado):
    sql = "delete from cursos where id_curso='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Curso excluido com sucesso."
    except:
        print "Erro na exclusão."
        db.rollback()
        
#===============================================================================

print "------ EXCLUSÃO DE CURSO ------"
saida = None
while saida <> "s":
    deletado = raw_input('Digite o id do curso que deseja excluir: ')
    verificar_curso = "select id_curso from cursos where id_curso='%s'" %(deletado)
    existe = cursor.execute(verificar_curso)
    if existe < 1:
        print "Curso não existente."
        continue
    else:
        excluirCurso(cursor, deletado)
        saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
print "------ FINISH ------"
db.close()
