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
        print "Erro na exclus�o, h� um usu�rio atrelado ao professor."
        db.rollback()

def excluirUsuario(cursor, deletado):
    sql = "delete from usuarios where usuario_cpf='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Usu�rio excluido com sucesso."
    except:
        print "Erro na exclus�o."
        db.rollback()
        
#===============================================================================

print "------ EXCLUS�O DE PROFESSOR/USU�RIO ------"
saida = None
while saida <> "s":
    deletado = raw_input('Digite o id(CPF) do usu�rio que deseja excluir: ')
    verificar_user = "select usuario_cpf from usuarios where usuario_cpf='%s'" %(deletado)
    existe = cursor.execute(verificar_user)
    if existe < 1:
        print "Professor/Usu�rio n�o existente."
        continue
    else:
        excluirUsuario(cursor, deletado)
        excluirProfessor(cursor, deletado)
        saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
  
print "------ FINISH ------"
db.close()