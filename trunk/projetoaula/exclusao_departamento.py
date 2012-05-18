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

print "------ EXCLUSÃO DE DEPARTAMENTO ------"
saida = None
while saida <> "s":
    deletado = raw_input('Digite o id do departamento que deseja excluir: ')
    verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(deletado)
    existe = cursor.execute(verificar_dep)
    if existe < 1:
        print "Departamento não existente."
        continue
    else:
        excluirDepartamento(cursor, deletado)
        saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
print "------ FINISH ------"
db.close()
