# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_predio):
    sql = "update predios set id_predio='%s' where id_predio='%s'" %(id_novo, id_predio)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID do predio editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome_predio, id_predio):
    sql = "update predios set nome_predio='%s' where id_predio='%s'" %(nome_predio, id_predio)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome do predio editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
             
#===============================================================================

