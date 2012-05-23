# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_local):
    sql = "update locais set id_local='%s' where id_local='%s'" %(id_novo, id_local)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome, id_local):
    sql = "update locais set nome_local='%s' where id_local='%s'" %(nome, id_local)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarTipo(cursor, tipo, id_local):
    sql = "update locais set tipo_local='%s' where id_local='%s'" %(tipo, id_local)
    try:
        cursor.execute(sql)
        db.commit()
        print "Tipo editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

print "------ EDIÇÃO DE DEPARTAMENTO ------"
saida = None
while saida <> "s":
    id_local = raw_input('Digite o id do local que deseja editar: ')
    verificar_local = "select id_local from locais where id_local='%s'" %(id_local)
    existe = cursor.execute(verificar_local)
    if existe < 1:
        print "ID não existente."
        continue
    else:
        opcao = input("Digite 1 (editar id), 2 (editar nome) ou 3 (editar tipo): ")
        if opcao > 3 or opcao < 1:
            print "Opção incorreta."
            continue
        else:
            if opcao == 1:
                id_novo = raw_input("Digite o novo ID do local: ")
                editarID(cursor, id_novo, id_local)
            if opcao == 2:
                nome = raw_input("Digite o novo nome do local: ")
                editarNome(cursor, nome, id_local)
            if opcao == 3:
                tipo = raw_input("TIPO: Sala/Laboratório/Auditório:")
                editarTipo(cursor, tipo, id_local)
            saida = raw_input('Digite s para sair ou enter pra continuar: ')
print "------ FINISH ------"
db.close()
