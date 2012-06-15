# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def cadastroLocais(cursor, nome_local, id_local, tipo_local, id_predio):
    sql = "insert into locais values('%s','%s','%s','%s')" %(id_local, nome_local, tipo_local, id_predio)
    try:
        cursor.execute(sql)
        db.commit()
        print "Novo local cadastrado com sucesso."
    except:
        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

print "------ CADASTRO DE LOCAL ------"
saida = None
while saida <> "s":
    id_predio = raw_input("Digite id do prédio: ")
    id_local = raw_input("Digite o id do local: ")
    nome_local = raw_input("Digite o nome do local: ")
    tipo_local = raw_input("TIPO: Sala/Laboratório/Auditório: ")
    cadastroLocais(cursor, nome_local, id_local, tipo_local, id_predio)
    saida = raw_input('Digite s para sair ou enter pra continuar: ')
print "------ FINISH ------"
db.close()
