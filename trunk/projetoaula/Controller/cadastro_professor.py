# -*- coding: cp1252 -*-
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


def cadastrarProfessor(cursor, id_professor, nome_professor, disciplinas, departamento_professor):
    sql = "insert into professores values('%s','%s','%s', '%s')"%(id_professor, nome_professor, disciplinas, departamento_professor)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "Erro no cadastro. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
        
def cadastrarUsuario(cursor, usuario_CPF):
    classe = 0 #Classe 0 para professores
    senha = "UFRPE1234" 
    sql = "insert into usuarios values('%s','%s','%s')"%(usuario_CPF, senha, classe)
    cursor.execute(sql)
    db.commit()

#===============================================================================
        