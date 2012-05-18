# -*- coding: cp1252 -*-
#===============================================================================
from acesso_db import Servidor
DATA = Servidor()
#===============================================================================
import MySQLdb
db = MySQLdb.connect(DATA.host,DATA.user,DATA.password,DATA.database)
cursor = db.cursor()
#===============================================================================

def editarID(cursor, id_novo, id_curso):
    sql = "update cursos set id_curso='%s' where id_curso='%s'" %(id_novo, id_curso)
    try:
        cursor.execute(sql)
        db.commit()
        print "ID editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarNome(cursor, nome, id_curso):
    sql = "update cursos set nome_curso='%s' where id_curso='%s'" %(nome, id_curso)
    try:
        cursor.execute(sql)
        db.commit()
        print "Nome do curso editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
def editarDepartamento(cursor, departamento, id_curso):
    sql = "update cursos set departamento_curso='%s' where id_curso='%s'" %(departamento, id_curso)
    try:
        cursor.execute(sql)
        db.commit()
        print "Departamento do curso editado com sucesso."
    except:
        print "Erro na edição. Por favor verifique se os campos foram inseridos corretamente."
        db.rollback()
        
#===============================================================================

print "------ EDIÇÃO DE CURSO ------"
saida = None
while saida <> "s":
    id_curso = raw_input('Digite o id do curso que deseja editar: ')
    verificar_curso = "select id_curso from cursos where id_curso='%s'" %(id_curso)
    existe = cursor.execute(verificar_curso)
    if existe < 1:
        print "ID não existente."
        continue
    else:
        opcao = input("Digite 1 (editar id), 2 (editar nome) ou 3 (editar departamento): ")
        if opcao > 3 or opcao < 1:
            print "Opção incorreta."
            continue
        else:
            if opcao == 1:
                id_novo = raw_input("Digite o novo ID do curso: ")
                editarID(cursor, id_novo, id_curso)
            if opcao == 2:
                nome = raw_input("Digite o novo nome do curso: ")
                editarNome(cursor, nome, id_curso)
            if opcao == 3:
                departamento = raw_input("Digite o id do novo departamento: ")
                verificar_dep = "select id_departamento from departamentos where id_departamento='%s'" %(departamento)
                existe = cursor.execute(verificar_dep)
                if existe < 1:
                    print "Departamento não existente."
                else:
                    editarDepartamento(cursor, departamento, id_curso)
            saida = raw_input('Digite s para sair ou enter pra continuar: ')
print "------ FINISH ------"
db.close()
