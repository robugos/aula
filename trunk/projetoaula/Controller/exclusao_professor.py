# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================


def excluirProfessor(cursor, deletado):
    sql = "delete from professores where id_professor='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Professor excluido com sucesso."
    except:
        print "Erro na exclusão, há um usuário atrelado ao professor."
        db.rollback()

def excluirUsuario(cursor, deletado):
    sql = "delete from usuarios where usuario_cpf='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Usuário excluido com sucesso."
    except:
        print "Erro na exclusão."
        db.rollback()
        
#===============================================================================
