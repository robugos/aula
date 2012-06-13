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
        