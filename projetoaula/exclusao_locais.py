# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def excluirLocal(cursor, deletado):
    sql = "delete from locais where id_local='%s'" %(deletado)
    try:
        cursor.execute(sql)
        db.commit()
        print "Local excluido com sucesso."
    except:
        print "Erro na exclusão"
        db.rollback()
        
#===============================================================================

print "------ EXCLUSÃO DE LOCAIS ------"
saida = None
while saida <> "s":
    deletado = raw_input('Digite o id do local que deseja excluir: ')
    verificar_local = "select id_local from locais where id_local='%s'" %(deletado)
    existe = cursor.execute(verificar_local)
    if existe < 1:
        print "Local não existente."
        continue
    else:
        excluirLocal(cursor, deletado)
        saida = raw_input('Digite s para sair ou enter para continuar excluindo: ')
print "------ FINISH ------"
db.close()