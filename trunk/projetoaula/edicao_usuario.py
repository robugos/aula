# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================
from Validacao import Validacao
#===============================================================================

def editarCPF(cursor, id_novo, id_CPF):
    sql = "update usuarios set usuario_cpf='%s' where usuario_CPF='%s'" %(id_novo, id_CPF)
    try:
        cursor.execute(sql)
        db.commit()
        print "CPF editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarSenha(cursor, senha, id_CPF):
    sql = "update usuarios set senha='%s' where usuario_cpf='%s'" %(senha, id_CPF)
    try:
        cursor.execute(sql)
        db.commit()
        print "Senha editada com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarClasse(cursor, classe, id_CPF):
    sql = "update usuarios set classe='%d' where usuario_cpf='%s'" %(classe, id_CPF)
    try:
        cursor.execute(sql)
        db.commit()
        print "Classe editada com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

