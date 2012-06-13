# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def cadastroDepartamento(cursor, id_departamento, nome, coordenador):
    sql = "insert into departamentos values('%s','%s','%s')" %(id_departamento, nome, coordenador)
    try:
        cursor.execute(sql)
        db.commit()
        print "Departamento cadastrado com sucesso."
    except:
        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================
