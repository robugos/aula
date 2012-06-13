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
