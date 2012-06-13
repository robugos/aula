# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_dep):
    sql = "update departamentos set id_departamento='%s' where id_departamento='%s'" %(id_novo, id_dep)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome, id_dep):
    sql = "update departamentos set nome_departamento='%s' where id_departamento='%s'" %(nome, id_dep)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarCoordenador(cursor, coordenador, id_dep):
    sql = "update departamentos set coordenador='%s' where id_departamento='%s'" %(coordenador, id_dep)
    try:
        cursor.execute(sql)
        db.commit()
        print "Coordenador editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

