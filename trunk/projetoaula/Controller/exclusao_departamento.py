# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================


def excluirDepartamento(cursor, deletado):
    sql = "delete from departamentos where id_departamento='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Departamento excluido com sucesso."
    except:
        print "Erro na exclusão, há professores ou cursos atrelados ao departamento."
        db.rollback()
        
#===============================================================================
