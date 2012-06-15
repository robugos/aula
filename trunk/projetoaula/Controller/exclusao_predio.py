# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================


def excluirPredio(cursor, deletado):
    sql = "delete from predios where id_predio='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Predio excluido com sucesso."
    except:
        print "Erro na exclusão."
        db.rollback()
        
#===============================================================================

