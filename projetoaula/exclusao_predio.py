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

print "------ EXCLUSÃO DE PREDIO ------"
saida = None
while saida <> "s":
    deletado = raw_input('Digite o id do predio que deseja excluir: ')
    verificar_predio = "select id_predio from predios where id_predio='%s'" %(deletado)
    existe = cursor.execute(verificar_predio)
    if existe < 1:
        print "Predio não existente."
        continue
    else:
        excluirPredio(cursor, deletado)
        saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
print "------ FINISH ------"
db.close()
