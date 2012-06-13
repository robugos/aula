# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_curso):
    sql = "update cursos set id_curso='%s' where id_curso='%s'" %(id_novo, id_curso)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome, id_curso):
    sql = "update cursos set nome_curso='%s' where id_curso='%s'" %(nome, id_curso)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome do curso editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarDepartamento(cursor, departamento, id_curso):
    sql = "update cursos set departamento_curso='%s' where id_curso='%s'" %(departamento, id_curso)
    try:
        cursor.execute(sql)
        db.commit()
        print "Departamento do curso editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================


