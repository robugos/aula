# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def cadastroPredio(cursor):
    id_predio = raw_input('Digite o ID do predio: ')
    nome_predio = raw_input("Digite o nome do predio: ")
    sql = "insert into predios values('%s','%s')" %(id_predio, nome_predio)
    try:
        cursor.execute(sql)
        db.commit()
        print "Novo predio cadastrado com sucesso."
    except:
        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================
