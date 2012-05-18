# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_dep):
    sql = "update departamentos set id_departamento='%s' where id_departamento='%s'" %(id_novo, id_dep)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome, id_dep):
    sql = "update departamentos set nome_departamento='%s' where id_departamento='%s'" %(nome, id_dep)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarCoordenador(cursor, coordenador, id_dep):
    sql = "update departamentos set coordenador='%s' where id_departamento='%s'" %(coordenador, id_dep)
    try:
        cursor.execute(sql)
        db.commit()
        print "Coordenador editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

print "------ EDIÇÃO DE DEPARTAMENTO ------"
saida = None
while saida <> "s":
    id_dep = raw_input('Digite o id do departamento que deseja editar: ')
    verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(id_dep)
    existe = cursor.execute(verificar_dep)
    if existe < 1:
        print "ID não existente."
        continue
    else:
        opcao = input("Digite 1 (editar id), 2 (editar nome) ou 3 (editar coordenador): ")
        if opcao > 3 or opcao < 1:
            print "Opção incorreta."
            continue
        else:
            if opcao == 1:
                id_novo = raw_input("Digite o novo ID do departamento: ")
                editarID(cursor, id_novo, id_dep)
            if opcao == 2:
                nome = raw_input("Digite o novo nome do departamento: ")
                editarNome(cursor, nome, id_dep)
            if opcao == 3:
                coordenador = raw_input("Digite o nome do novo coordenador: ")
                editarCoordenador(cursor, coordenador, id_dep)
            saida = raw_input('Digite s para sair ou enter pra continuar: ')
print "------ FINISH ------"
db.close()
