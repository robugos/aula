# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================


def excluirDisciplina(cursor, deletado):
    sql = "delete from disciplinas where id_disciplina='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Disciplina excluida com sucesso."
    except:
        print "Erro na exclusão."
        db.rollback()
        
#===============================================================================

print "------ EXCLUSÃO DE DISCIPLINAS ------"
saida = None
while saida <> "s":
    deletado = raw_input('Digite o id da disciplina que deseja excluir: ')
    verificar_dis = "select id_disciplina from disciplinas where id_disciplina='%s'" %(deletado)
    existe = cursor.execute(verificar_dis)
    if existe < 1:
        print "Disciplina não existente."
        continue
    else:
        excluirDisciplina(cursor, deletado)
        saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
print "------ FINISH ------"
db.close()
