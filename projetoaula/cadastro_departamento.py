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
    except:
        print "ERRO"
        db.rollback()
    db.close()

print "------ CADASTRO DE DEPARTAMENTO ------"
saida = None
while exit <> "s":
    id_departamento = raw_input('Digite o id do departamento:')
    nome = raw_input("Digite o nome do departamento:")
    coordenador = raw_input("Digite o nome do coordenador:")
    cadastroDepartamento( cursor, id_departamento, nome, coordenador)
    saida = raw_input('Digite s para sair ou enter pra continuar')
print "------ FINISH ------"
