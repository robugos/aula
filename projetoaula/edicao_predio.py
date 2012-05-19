# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_predio):
    sql = "update predios set id_predio='%s' where id_predio='%s'" %(id_novo, id_predio)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID do predio editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome_predio, id_predio):
    sql = "update predios set nome_predio='%s' where id_predio='%s'" %(nome_predio, id_predio)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome do predio editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
             
#===============================================================================

print "------ EDIÇÃO DE PREDIO ------"
saida = None
while saida <> "s":
    id_predio = raw_input('Digite o id do predio que deseja editar: ')
    verificar_predio = "select id_predio from predios where id_predio='%s'" %(id_predio)
    existe = cursor.execute(verificar_predio)
    if existe < 1:
        print "ID não existente."
        continue
    else:
        opcao = input("Digite 1 para editar o id, ou 2 para editar o nome: ")
        if opcao > 2 or opcao < 1:
            print "Opção incorreta."
            continue
        else:
            if opcao == 1:
                id_novo = raw_input("Digite o novo ID do predio: ")
                editarID(cursor, id_novo, id_predio)
            if opcao == 2:
                nome_predio = raw_input("Digite o novo nome do predio: ")
                editarNome(cursor, nome_predio, id_predio)
            saida = raw_input('Digite s para sair ou enter pra continuar: ')
print "------ FINISH ------"
db.close()
